import sqlite3

#establishes a connection to DataBase, creats a file where its stored
conn = sqlite3.connect('food.db')
cur = conn.cursor()

# makes a products table
cur.execute("""CREATE TABLE IF NOT EXISTS Products(
            product_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT,
            price REAL NOT NUll);
            """)
# makes a sales table 
cur.execute("""CREATE TABLE IF NOT EXISTS Sales(
            sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER,
            quantity INTEGER,
            sale_date TEXT NOT NULL,
            FOREIGN KEY (product_id) REFERENCES Products(product_id));""")


conn.commit()
conn.close()