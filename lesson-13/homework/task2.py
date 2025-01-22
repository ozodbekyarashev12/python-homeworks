import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('library.db')
cursor = conn.cursor()

# Step 1: Create the table for Books
cursor.execute('''
CREATE TABLE IF NOT EXISTS Books (
    Title TEXT,
    Author TEXT,
    Year_Published INTEGER,
    Genre TEXT
)
''')

# Step 2: Insert Data into the Books table
cursor.execute('''
INSERT INTO Books (Title, Author, Year_Published, Genre) VALUES
('To Kill a Mockingbird', 'Harper Lee', 1960, 'Fiction'),
('1984', 'George Orwell', 1949, 'Dystopian'),
('The Great Gatsby', 'F. Scott Fitzgerald', 1925, 'Classic')
''')

# Commit the changes
conn.commit()

# Step 3: Update Data (Change the Year_Published of 1984 to 1950)
cursor.execute('''
UPDATE Books
SET Year_Published = 1950
WHERE Title = '1984'
''')

# Commit the changes
conn.commit()

# Step 4: Query Data (Retrieve Title and Author where Genre is 'Dystopian')
cursor.execute('''
SELECT Title, Author FROM Books WHERE Genre = 'Dystopian'
''')

# Fetch and display the results
print("Dystopian Books:")
for row in cursor.fetchall():
    print(f"Title: {row[0]}, Author: {row[1]}")

# Step 5: Delete Data (Remove books published before 1950)
cursor.execute('''
DELETE FROM Books WHERE Year_Published < 1950
''')

# Commit the changes
conn.commit()

# Step 6: Bonus Task (Add a new column 'Rating' and update the data)
cursor.execute('''
ALTER TABLE Books ADD COLUMN Rating REAL
''')

# Update the Rating for each book
cursor.execute('''
UPDATE Books SET Rating = 4.8 WHERE Title = 'To Kill a Mockingbird'
''')
cursor.execute('''
UPDATE Books SET Rating = 4.7 WHERE Title = '1984'
''')
cursor.execute('''
UPDATE Books SET Rating = 4.5 WHERE Title = 'The Great Gatsby'
''')

# Commit the changes
conn.commit()

# Step 7: Advanced Query (Retrieve all books sorted by Year_Published in ascending order)
cursor.execute('''
SELECT Title, Author, Year_Published FROM Books ORDER BY Year_Published ASC
''')

# Fetch and display the results
print("\nBooks sorted by Year Published (Ascending):")
for row in cursor.fetchall():
    print(f"Title: {row[0]}, Author: {row[1]}, Year Published: {row[2]}")

# Close the connection
conn.close()
