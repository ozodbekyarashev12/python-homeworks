import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('roster.db')
cursor = conn.cursor()

# Step 1: Create the table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
''')

# Step 2: Insert Data
cursor.execute('''
INSERT INTO Roster (Name, Species, Age) VALUES
('Benjamin Sisko', 'Human', 40),
('Jadzia Dax', 'Trill', 300),
('Kira Nerys', 'Bajoran', 29)
''')

# Commit the changes
conn.commit()

# Step 3: Update Data (change Jadzia Dax to Ezri Dax)
cursor.execute('''
UPDATE Roster
SET Name = 'Ezri Dax'
WHERE Name = 'Jadzia Dax'
''')

# Commit the changes
conn.commit()

# Step 4: Query Data (Retrieve Name and Age for Bajoran species)
cursor.execute('''
SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'
''')

# Fetch and display the results
print("Bajoran Characters:")
for row in cursor.fetchall():
    print(f"Name: {row[0]}, Age: {row[1]}")

# Step 5: Delete Data (Remove characters aged over 100)
cursor.execute('''
DELETE FROM Roster WHERE Age > 100
''')

# Commit the changes
conn.commit()

# Step 6: Bonus Task (Add a new column 'Rank' and update it)
cursor.execute('''
ALTER TABLE Roster ADD COLUMN Rank TEXT
''')

# Update the Rank for each character
cursor.execute('''
UPDATE Roster SET Rank = 'Captain' WHERE Name = 'Benjamin Sisko'
''')
cursor.execute('''
UPDATE Roster SET Rank = 'Lieutenant' WHERE Name = 'Ezri Dax'
''')
cursor.execute('''
UPDATE Roster SET Rank = 'Major' WHERE Name = 'Kira Nerys'
''')

# Commit the changes
conn.commit()

# Step 7: Advanced Query (Retrieve all characters sorted by Age in descending order)
cursor.execute('''
SELECT Name, Species, Age FROM Roster ORDER BY Age DESC
''')

# Fetch and display the results
print("\nCharacters sorted by Age (Descending):")
for row in cursor.fetchall():
    print(f"Name: {row[0]}, Species: {row[1]}, Age: {row[2]}")

# Close the connection
conn.close()
