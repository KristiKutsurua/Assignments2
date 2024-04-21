import sqlite3


conn = sqlite3.connect('deposits.db')

conn.execute('''
CREATE TABLE IF NOT EXISTS Deposits (
    DepositID INTEGER PRIMARY KEY AUTOINCREMENT,
    DepOwnerName TEXT,
    DateOfBirth DATE,
    City TEXT,
    StreetName TEXT,
    DepositAmount REAL,
    Interest REAL,
    Comission REAL,
    Total REAL
);
''')


conn.execute('''
INSERT INTO Deposits (DepOwnerName, DateOfBirth, City, StreetName)
VALUES 
('John Doe', '1990-05-15', 'Tbilisi', 'Rustaveli Street'),
('Jane Doe', '1985-07-20', 'Batumi', 'Gorgasali Street'),
('Alan Smithee', '1992-02-10', 'Chicago', 'Michigan Ave');
''')

conn.execute('''
INSERT INTO Deposits (DepOwnerName, DateOfBirth, DepositAmount, Comission, Total)
VALUES 
('Davit Davitauri', '1988-04-25', 2000, 50, 2050),
('Alice Smith', '1995-01-30', 3000, 100, 3100),
('John Doe', '1998-09-05', 1200, 40, 1240),
('David Miller', '1980-11-12', 1800, 60, 1860),
('Eva Davis', '1993-06-18', 1500, 50, 1550);
''')

print("\nAll depositors:")
cursor = conn.execute('SELECT * FROM Deposits')
for row in cursor:
    print(row)

print("\nDepositors with deposit less than 1500:")
cursor = conn.execute('SELECT * FROM Deposits WHERE DepositAmount < 1500')
for row in cursor:
    print(row)

print("\nDepositors living in Tbilisi at Rustaveli Street:")
cursor = conn.execute('SELECT * FROM Deposits WHERE City = "Tbilisi" AND StreetName = "Rustaveli Street"')
for row in cursor:
    print(row)


print("\nDepositors living in Batumi at Gorgasali street with deposit between 1000 and 2000:")
cursor = conn.execute('''
SELECT * 
FROM Deposits 
WHERE City = "Batumi" 
AND StreetName = "Gorgasali street" 
AND DepositAmount > 1000 
AND DepositAmount < 2000;
''')
for row in cursor:
    print(row)


print("\nDepositors with names starting with 'D':")
cursor = conn.execute('SELECT * FROM Deposits WHERE DepOwnerName LIKE "D%"')
for row in cursor:
    print(row)

conn.execute('DELETE FROM Deposits')

cursor = conn.execute('SELECT * FROM Deposits')
rows = cursor.fetchall()

if len(rows) == 0:
    print("\nTable 'Deposits' has been cleaned successfully.")
else:
    print("\nFailed to clean the table.")

conn.execute('DROP TABLE IF EXISTS Deposits')

conn.close()
