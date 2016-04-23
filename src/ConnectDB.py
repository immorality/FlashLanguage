from mysql.connector import MySQLConnection
from mysql.connector import Error


class ConnectDB:
    def __init__(self):
        pass

    def iter_row(self, cursor, size=10):
        while True:
            rows = cursor.fetchmany(size)
            if not rows:
                break
            for row in rows:
                yield row

    def getUsers(self):
        testList = []

        try:
            conn = MySQLConnection(host='localhost', database='mydb', user='root', password='root')
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users")
            # rows = cursor.fetchall()

            # print rows

            for row in self.iter_row(cursor, 10):
                testList += row
                print row

            if conn.is_connected():
                print "Connected to database"

        except Error as e:
            print e

        finally:
            cursor.close()
            conn.close()

        return testList

    def insert_new(self, user, password):
        query = "INSERT INTO users(name, password) " \
                "VALUES(%s,%s)"
        args = (user, password)

        try:
            conn = MySQLConnection(host='localhost', database='mydb', user='root', password='root')
            cursor = conn.cursor()
            cursor.execute(query, args)

            if cursor.lastrowid:
                print "Last row id: ", cursor.lastrowid
            else:
                print "Last row is not found"

            conn.commit()

        except Error as error:
            print error

        finally:
            cursor.close()
            conn.close()

    def insertEnglishWord(self, word):
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


def main():
    connection = ConnectDB()
    print connection.getUsers()
    # insert_new("John", "1q2w3e4r")


if __name__ == '__main__':
    main()
