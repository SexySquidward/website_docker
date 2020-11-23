import mysql.connector
from mysql.connector import errorcode

def conn_to_db():
    try:
        db = mysql.connector.connect(
            host="192.168.1.8",
            user="root",
            password="pepsilover111",
            database="test"
        )
        # determines success of connection and any difficulties
        print("Connection Successful")
        return db
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    return db
        # exit program if error

def sumbit_tester(FN,LN,age):
    database = conn_to_db()
    cursor = database.cursor()
    sql = 'INSERT INTO testers (Firstname,Lastname,Age) VALUES (%s, %s,%s)'
    val = (FN,LN,age)
    cursor.execute(sql,val)
    database.commit()
    database.close()
    print(cursor.rowcount, "record inserted.")

def Pull_Tester():
    database = conn_to_db()
    cursor = database.cursor()
    cursor.execute("SELECT * FROM testers")
    results = cursor.fetchall()
    return results
