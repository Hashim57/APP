
import mysql
import mysql.connector
import unittest




mydb= mysql.connector.connect(
        port = "33066",
        user= "root",
        password ="insecure",
        database = "Database1")
print(mydb)
mycursor = mydb.cursor()



mycursor.execute("Select id, name FROM person" )
rows = mycursor.fetchall()

for row in rows:
        print("ID -" + str(row[0]) + ", Name -" + row[1] )

sql = "INSERT INTO person (id, name) VALUES (%s, %s)"

val = ("27", "Paul")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")


mycursor.close()

if __name__ == "__main__":
    unittest.main()