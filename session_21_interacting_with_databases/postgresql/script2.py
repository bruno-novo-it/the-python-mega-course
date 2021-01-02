# pip3 install psycopg2

import psycopg2


# Create the table stablishing connection with the database
def create_table():
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgres' host='127.0.0.1' port='5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

# Insert some values to the table stablishing connection with the database
def insert(item, quantity,price):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgres' host='127.0.0.1' port='5432'")
    cur = conn.cursor()
    #cur.execute("INSERT INTO store VALUES ('Wine Glass', 8,10.5)")
    cur.execute("INSERT INTO store VALUES (%s,%s,%s)",(item,quantity,price))
    conn.commit()
    conn.close()

def view():
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgres' host='127.0.0.1' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows # Rows is returned as a Python list

def delete(item):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgres' host='127.0.0.1' port='5432'")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s",(item,))
    conn.commit()
    conn.close()

def update(quantity,price,item):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgres' host='127.0.0.1' port='5432'")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s",(quantity,price,item))
    conn.commit()
    conn.close()

create_table()
delete("Coffee Cup")
print(view())
insert("Coffee Cup",10,5)
print(view())
update(11,6,"Coffee Cup")
print(view())