import psycopg2 as pg2

def create_table():
    conn=pg2.connect(database='data3' ,user='postgres' ,password='abhith78' )
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store(item TEXT,price REAL,quantity INT)")


    conn.commit()
    conn.close()

def insert(item,price,quantity):
    conn=psycopg2.connect("lite.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?)",(item,price,quantity))
    conn.commit()
    conn.close()

def view():
    conn=psycopg2.connect("lite.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows
def delete(item):
    conn=psycopg2.connect("lite.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?",(item,))
    conn.commit()
    conn.close()

def update(item,price,quantity):
    conn=psycopg2.connect("lite.db")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=?,price=? WHERE item=?",(quantity,price,item))
    conn.commit()
    conn.close()

create_table()
print(view())
