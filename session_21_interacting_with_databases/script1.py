import sqlite3


# Create the table stablishing connection with the database
def create_table():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

# Insert some values to the table stablishing connection with the database
def insert(item, quantity,price):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    #cur.execute("INSERT INTO store VALUES ('Wine Glass', 8,10.5)")
    cur.execute("INSERT INTO store VALUES (?,?,?)",(item,quantity,price))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows # Rows is returned as a Python list

def delete(item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?",(item,))
    conn.commit()
    conn.close()

def update(quantity,price,item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?",(quantity,price,item))
    conn.commit()
    conn.close()

delete("Coffee Cup")
print(view())
insert("Coffee Cup",10,5)
print(view())
update(11,6,"Coffee Cup")
print(view())