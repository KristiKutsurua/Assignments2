import sqlite3
from datetime import datetime

conn = sqlite3.connect('sales_database.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE Customers (
    CustomerID INTEGER PRIMARY KEY,
    FullName VARCHAR(255),
    Email VARCHAR(255),
    Phone VARCHAR(50)
)
''')

cursor.execute('''
CREATE TABLE Sales (
    SaleID INTEGER PRIMARY KEY,
    CustomerID INTEGER,
    ProductName VARCHAR(255),
    Quantity FLOAT,
    UnitPrice FLOAT,
    SaleDate TIMESTAMP,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
)
''')

customers_data = [
    ('John Doe', 'john.doe@example.com', '123-456-7890'),
    ('Jane Doe', 'jane.doe@example.com', '987-654-3210'),
    ('Alice Smith', 'alice.smith@example.com', '555-123-4567'),
    ('Bob Johnson', 'bob.johnson@example.com', '777-888-9999'),
    ('Eve Brown', 'eve.brown@example.com', '111-222-3333'),
    ('Mike Davis', 'mike.davis@example.com', '444-555-6666')
]

cursor.executemany('''
INSERT INTO Customers (FullName, Email, Phone) VALUES (?, ?, ?)
''', customers_data)

sales_data = [
    (1, 'Laptop', 2, 1200.50, datetime.now()),
    (2, 'Phone', 3, 800.75, datetime.now()),
    (3, 'Tablet', 1, 500.25, datetime.now()),
    (4, 'Smartwatch', 2, 250.50, datetime.now()),
    (5, 'Headphones', 4, 100.00, datetime.now()),
    (6, 'Keyboard', 1, 75.50, datetime.now()),
    (7, 'Mouse', 3, 25.75, datetime.now())
]

cursor.executemany('''
INSERT INTO Sales (CustomerID, ProductName, Quantity, UnitPrice, SaleDate) VALUES (?, ?, ?, ?, ?)
''', sales_data)

conn.commit()

cursor.execute('''
SELECT SUM(Quantity * UnitPrice) AS TotalRevenue FROM Sales
''')
total_revenue = cursor.fetchone()[0]
print(f'Total Revenue: ${total_revenue:.2f}')

cursor.execute('''
SELECT AVG(Quantity * UnitPrice) AS AverageSales FROM Sales
''')
average_sales = cursor.fetchone()[0]
print(f'Average Sales: ${average_sales:.2f}')

cursor.execute('''
SELECT c.FullName, s.ProductName, s.Quantity, s.UnitPrice, s.SaleDate
FROM Customers c
JOIN Sales s ON c.CustomerID = s.CustomerID
''')
print('\nCustomers with Sales:')
for row in cursor.fetchall():
    print(row)

cursor.execute('''
SELECT c.FullName
FROM Customers c
LEFT JOIN Sales s ON c.CustomerID = s.CustomerID
WHERE s.SaleID IS NULL
''')
print('\nCustomers without Sales:')
for row in cursor.fetchall():
    print(row[0])

cursor.execute('''
SELECT ProductName, SUM(Quantity) AS TotalQuantity
FROM Sales
GROUP BY ProductName
''')
print('\nSold Products and Quantities:')
for row in cursor.fetchall():
    print(row)

cursor.execute('''
SELECT c.FullName, s.ProductName, s.Quantity, s.UnitPrice, s.SaleDate
FROM Customers c
LEFT JOIN Sales s ON c.CustomerID = s.CustomerID
ORDER BY c.FullName
''')
print('\nCustomers and Their Sales:')
for row in cursor.fetchall():
    print(row)

conn.close()