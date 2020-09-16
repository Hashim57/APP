
import mysql.connector




def db():
    return mysql.connector.connect(
        port = "33066",
        user= "root",
        password ="insecure",
        database = "Database1"
    )



def query(mydb: object, sql: str):
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    return mycursor.fetchall()

def update(mydb: object, sql: str):
    mycursor =mydb.cursor()
    mycursor.execute(sql)
    mydb.commit()

    mycursor.close()

# mycursor.execute("SELECT * from person")


# myresult= mycursor.fetchall()
# for row in myresult:
#     print(row[0], row[1])

# mycursor.execute("SELECT * from drink")


# myresult= mycursor.fetchall()
# for row in myresult:
#     print(row[0], row[1])


# mycursor.execute("SELECT * from prefs")


# myresult= mycursor.fetchall()
# for row in myresult:
#     print(row[0], row[1])




# def write_to_mysql_table(dict_from_app):
    
#     list_of_tuples = [(x, y) for x, y in dict_from_app.items()]
#     write_to_table = "INSERT INTO person (person_id, name) VALUES (%s, %s)"
#     write_to_table = "INSERT INTO drink (drink_id, name) VALUES (%s, %s)"
#     write_to_table = "INSERT INTO prefs (person_id, drink_id) VALUES (%s, %s)"
#     mycursor.executemany(write_to_table, list_of_tuples)



# mydb.commit()



