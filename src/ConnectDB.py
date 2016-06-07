#
#
#not actually now, but i keep it on, because maybe i'll use it later
#
#

from mysql.connector import MySQLConnection
from mysql.connector import Error

class ConnectDB:
    def __init__(self):
        pass

    def getAllUsers(self):

        try:
            conn = MySQLConnection(host='localhost', database='mydb', user='root', password='root')
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users")
            rows = cursor.fetchall()
            return rows
        except Error as error:
            print error
        finally:
            cursor.close()
            conn.close()


    def addEnglishWord(self, word):
        query = "INSERT INTO english(word) " \
                "VALUES(%s)"
        args = (word)

        try:
            conn = MySQLConnection(host='localhost', database='mydb', user='root', password='root')
            cursor = conn.cursor()
            cursor.execute(query, args)

            conn.commit()

        except Error as error:
            print error

        finally:
            cursor.close()
            conn.close()

    def addNewUser(self, user, password):
        query = "INSERT INTO users(name, password) " \
                "VALUES(%s, %s)"

        args = (user, password)
        try:
            conn = MySQLConnection(host='localhost', database='mydb', user='root', password='root')
            cursor = conn.cursor()
            cursor.execute(query, args)

            conn.commit()

        except Error as error:
            print error

        finally:
            cursor.close()
            conn.close()

def main():
    connection1 = ConnectDB()
    print connection1.getAllUsers()
    #connection1.addNewUser("Dorian", "fffuuu")


if __name__ == '__main__':
    main()
