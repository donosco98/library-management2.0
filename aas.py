import psycopg2
usern='postgres'
db='data1'
pass1='abhith'
conn=psycopg2.connect("dbname=db ,user=wsern, password='abhith', host=127.0.0.1")
cur=conn.cursor()


conn.commit()
conn.close()
