import sqlite3
def create_mysql_db(db_name):
    mydb = mysql.connector.connect(host='localhost', user='root', passwd='rootless')

    mycursor = mydb.cursor()

    mycursor.execute("CREATE DATABASE IF NOT EXISTS thingiverse")
    sql = "CREATE DATABASE IF NOT EXISTS %s"
    val = (db_name)
    mycursor.execute(sql % val)


def create_mysql_table(table_name, column_names):
    mydb = mysql.connector.connect(host='localhost', user='root', passwd='rootless', database='thingiverse')

    mycursor = mydb.cursor()
    sql = "CREATE TABLE IF NOT EXISTS %s (%s)"
    val = (table_name, column_names)
    mycursor.execute(sql % val)


def main():
    create_mysql_db()

    create_mysql_table('creators', 'id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) UNIQUE')

why does this not work?