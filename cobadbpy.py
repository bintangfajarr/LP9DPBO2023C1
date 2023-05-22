import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_cobapy",
)

dbcursor=mydb.cursor()
sql="INSERT INTO testing(id_test,nama) VALUES (%s, %s)" 
val = (2,"bintang")
dbcursor.execute(sql,val)
mydb.commit()
print(dbcursor.rowcount,"record inserted")

dbcursor=mydb.cursor()
dbcursor.execute("SELECT * FROM testing")
myresult=dbcursor.fetchall()
for x in myresult:
    print(x)

dbcursor = mydb.cursor()
sql = "DELETE FROM testing WHERE nama='bintang'"
dbcursor.execute(sql)
mydb.commit()
print(dbcursor.rowcount,"record deleted")