import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('roster.db')
cursor = conn.cursor()

# Create the Roster table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
''')

# Insert data into the Roster table
cursor.executemany('''
INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)
''', [
    ('Benjamin Sisko', 'Human', 40),
    ('Jadzia Dax', 'Trill', 300),
    ('Kira Nerys', 'Bajoran', 29)
])

# Update the Name of Jadzia Dax to Ezri Dax
cursor.execute('''
UPDATE Roster
SET Name = 'Ezri Dax'
WHERE Name = 'Jadzia Dax'
''')

# Retrieve and display the Name and Age of all characters where the Species is Bajoran
cursor.execute('''
SELECT Name, Age
FROM Roster
WHERE Species = 'Bajoran'
''')
bajoran_characters = cursor.fetchall()
print("Bajoran Characters:", bajoran_characters)

# Remove all characters aged over 100 years from the table
cursor.execute('''
DELETE FROM Roster
WHERE Age > 100
''')

# Add a new column called Rank to the Roster table
cursor.execute('''
ALTER TABLE Roster
ADD COLUMN Rank TEXT
''')

# Update the data with the new Rank values
cursor.executemany('''
UPDATE Roster
SET Rank = ?
WHERE Name = ?
''', [
    ('Captain', 'Benjamin Sisko'),
    ('Lieutenant', 'Ezri Dax'),
    ('Major', 'Kira Nerys')
])

# Retrieve all characters sorted by their Age in descending order
cursor.execute('''
SELECT * FROM Roster
ORDER BY Age DESC
''')
sorted_characters = cursor.fetchall()
print("Characters sorted by Age:", sorted_characters)

# Commit the changes and close the connection
conn.commit()
conn.close()