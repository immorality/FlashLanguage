
from mysql.connector import MySQLConnection
from mysql.connector import Error


def connect():
    try:
        conn = MySQLConnection(host='localhost', database='mydb', user='root', password='root')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        row = cursor.fetchone()

        while row is not None:
            print row
            row = cursor.fetchone()

        if conn.is_connected():
            print "Connected to database"

    except Error as e:
        print e

    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    connect()