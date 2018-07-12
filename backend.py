import sqlite3
class database:
    def __init__(self):
        self.conn=sqlite3.connect("books.db")
        self.curr=self.conn.cursor()
        self.curr.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text,author text,year integer,isbn integer)")
        self.conn.commit()
        


    def insert(self,title,author,year,isbn):

        self.curr.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
        self.conn.commit()



    def view(self):

        self.curr.execute("SELECT * FROM book")
        rows=self.curr.fetchall()

        return rows

    def search(self,title="",author="",year="",isbn=""):

        self.curr.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))

        rows=self.curr.fetchall()

        return rows

    def delete(self,id):


        self.curr.execute("DELETE FROM book WHERE id=?",(id,))
        self.conn.commit()

    def update(self,id,title,author,year,isbn):

        self.curr.execute("UPDATE book SET title=?,author=?,year=?,isbn=? WHERE id=?",(title,author,year,isbn,id))
        self.conn.commit()
