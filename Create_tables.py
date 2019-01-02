import mysql.connector

def create_mysql_db(db_name):
    mydb = mysql.connector.connect(host='localhost', user='root', passwd='rootless')

    mycursor = mydb.cursor()

    sql = "CREATE DATABASE IF NOT EXISTS %s"

    val = (db_name)

    mycursor.execute(sql % val)


def create_mysql_table(table_name, column_names):
    mydb = mysql.connector.connect(host='localhost', user='root', passwd='rootless', database='matching')

    mycursor = mydb.cursor()
    sql = "CREATE TABLE IF NOT EXISTS %s (%s)"
    val = (table_name, column_names)
    mycursor.execute(sql % val)


def main():
    create_mysql_db('matching')

    create_mysql_table('users',
                                 """id INT AUTO_INCREMENT PRIMARY KEY, 
                                 username VARCHAR(255) UNIQUE, 
                                 email VARCHAR(255) UNIQUE""")
    create_mysql_table('url', 'url_id INT AUTO_INCREMENT PRIMARY KEY, url VARCHAR(255) UNIQUE')

    create_mysql_table('category', 'category_id INT AUTO_INCREMENT PRIMARY KEY, name varchar(100)')

    # create_mysql_table('user_course', 'id INT AUTO_INCREMENT PRIMARY KEY, user_id INT, course_id INT, '
    #                                   'FOREIGN KEY (user_id)'
    #                                   'REFERENCES users(id), FOREIGN KEY (course_id) REFERENCES courses(id)')


main()