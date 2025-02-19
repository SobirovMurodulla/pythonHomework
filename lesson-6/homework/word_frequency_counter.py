import os
import re
from collections import Counter

def create_sample_file():
    print("sample.txt does not exist. Please type in a paragraph to create the file.")
    content = input("Enter text: ")
    with open('sample.txt', 'w') as file:
        file.write(content)

def read_file():
    if not os.path.exists('sample.txt'):
        create_sample_file()
    with open('sample.txt', 'r') as file:
        return file.read()

def count_word_frequency(text):
    # Remove punctuation and convert to lowercase
    text = re.sub(r'[^\w\s]', '', text).lower()
    words = text.split()
    return Counter(words)

def display_and_save_report(word_counts, total_words, top_n):
    print(f"Total words: {total_words}")
    print(f"Top {top_n} most common words:")
    for word, count in word_counts.most_common(top_n):
        print(f"{word} - {count} times")

    with open('word_count_report.txt', 'w') as file:
        file.write("Word Count Report\n")
        file.write(f"Total Words: {total_words}\n")
        file.write(f"Top {top_n} Words:\n")
        for word, count in word_counts.most_common(top_n):
            file.write(f"{word} - {count}\n")


text = read_file()
word_counts = count_word_frequency(text)
total_words = sum(word_counts.values())

top_n = int(input("Enter the number of top common words to display: "))
display_and_save_report(word_counts, total_words, top_n)
