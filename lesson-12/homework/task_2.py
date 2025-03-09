import requests
from bs4 import BeautifulSoup
import sqlite3
import csv

def scrape_jobs():
    url = 'https://realpython.github.io/fake-jobs'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    jobs = []

    for job_element in soup.find_all('div', class_='card-content'):
        title = job_element.find('h2', class_='title').text.strip()
        company = job_element.find('h3', class_='company').text.strip()
        location = job_element.find('p', class_='location').text.strip()
        description_element = job_element.find('div', class_='description')
        description = description_element.text.strip() if description_element else 'No description available'
        application_link = job_element.find('a', class_='card-footer-item')['href']
        jobs.append((title, company, location, description, application_link))

    return jobs


def create_database():
    conn = sqlite3.connect('jobs.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY,
            title TEXT,
            company TEXT,
            location TEXT,
            description TEXT,
            application_link TEXT,
            UNIQUE(title, company, location)
        )
    ''')
    conn.commit()
    conn.close()

def save_jobs_to_database(jobs):
    conn = sqlite3.connect('jobs.db')
    cursor = conn.cursor()

    for job in jobs:
        cursor.execute('''
            INSERT OR IGNORE INTO jobs (title, company, location, description, application_link)
            VALUES (?, ?, ?, ?, ?)
        ''', job)
        cursor.execute('''
            UPDATE jobs
            SET description = ?, application_link = ?
            WHERE title = ? AND company = ? AND location = ?
        ''', (job[3], job[4], job[0], job[1], job[2]))

    conn.commit()
    conn.close()

def incremental_load():
    jobs = scrape_jobs()
    save_jobs_to_database(jobs)

def filter_jobs(location=None, company=None):
    conn = sqlite3.connect('jobs.db')
    cursor = conn.cursor()
    query = 'SELECT * FROM jobs WHERE 1=1'
    params = []

    if location:
        query += ' AND location = ?'
        params.append(location)
    if company:
        query += ' AND company = ?'
        params.append(company)

    cursor.execute(query, params)
    results = cursor.fetchall()
    conn.close()
    return results

def export_to_csv(filtered_jobs, filename='filtered_jobs.csv'):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['title', 'company', 'location', 'description', 'application_link']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for job in filtered_jobs:
            writer.writerow({
                'title': job[1],
                'company': job[2],
                'location': job[3],
                'description': job[4],
                'application_link': job[5]
            })

if __name__ == '__main__':
    create_database()
    incremental_load()
    filtered_jobs = filter_jobs(location='Remote', company='Real Python')
    export_to_csv(filtered_jobs)