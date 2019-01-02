import mysql.connector

def create_mysql_db(db_name):
    mydb = mysql.connector.connect(host='localhost', user='root', passwd='rootless')

    mycursor = mydb.cursor()

    sql = "CREATE DATABASE IF NOT EXISTS %s"

    val = (db_name)

    mycursor.execute(sql % val)


def create_mysql_table(table_name, column_names):
    mydb = connection()

    mycursor = mydb.cursor()
    sql = "CREATE TABLE IF NOT EXISTS %s (%s)"
    val = (table_name, column_names)
    mycursor.execute(sql % val)


def create_user(username, email):
    """Creates new entry in Users table"""
    mydb = connection()

    mycursor = mydb.cursor()
    # sql = """INSERT IGNORE INTO users(username, email) VALUES (%s, %s)"""
    val = (username, email)
    mycursor.execute("""INSERT IGNORE INTO users(username, email) VALUES (%s, %s)""", val)
    mydb.commit()
    return


def create_category(category):
    """Creates new entry in Category table"""
    mydb = connection()

    mycursor = mydb.cursor()
    sql = """INSERT IGNORE INTO category(name) VALUES (%s)"""
    val = category
    mycursor.execute(sql % val)
    return


def create_course(name, user, lon, lat, time_to_meet, hrs, url, category):
    """Create an entry in courses"""
    create_url(url)
    create_category(category)

    mydb = connection()
    mycursor = mydb.cursor()


    sql = """INSERT IGNORE INTO course(name, user_id, longitude, latitude,
                                        time_to_meet, hrs_per_week, url_id, 
                                        category_id) VALUES (%s, 
                                        (SELECT ID FROM users WHERE username=%s),
                                        %s, %s, %s, %s,
                                        (SELECT url_id FROM url WHERE url=%s)
                                        (SELECT category_id FROM category WHERE name=%s)) """
    val = name, user, lon, lat, time_to_meet, hrs, url, category
    mycursor.execute(sql % val)
    return


def create_url(url):
    """Creates new entry in url if the url does not exist yet"""
    mydb = connection()

    mycursor = mydb.cursor()
    sql = """INSERT IGNORE INTO url(url) VALUES(%s)"""
    val = url
    mycursor.execute(sql % val)
    return

def connection():
    return mysql.connector.connect(host='localhost', user='root', passwd='rootless', database='matching')

def main():
    create_mysql_db('matching')

    create_mysql_table('users',
                       """id INT AUTO_INCREMENT PRIMARY KEY,
                       username VARCHAR(255) UNIQUE,
                       email VARCHAR(255) UNIQUE""")
    create_mysql_table('url', 'url_id INT AUTO_INCREMENT PRIMARY KEY, url VARCHAR(255) UNIQUE')

    create_mysql_table('category', 'category_id INT AUTO_INCREMENT PRIMARY KEY, name varchar(100) UNIQUE')
    create_mysql_table('course',
                       """id INT AUTO_INCREMENT PRIMARY KEY,
                       name VARCHAR(255),
                       user_id INT,
                       longitude FLOAT(10, 7),
                       latitude FLOAT(10, 7),
                       time_to_meet VARCHAR(255),
                       hrs_per_week INT,
                       url_id INT,
                       category_id INT,
                       FOREIGN KEY (user_id) REFERENCES users(id),
                       FOREIGN KEY (url_id) REFERENCES url(url_id) ON DELETE CASCADE,
                       FOREIGN KEY (category_id) REFERENCES category(category_id) ON DELETE CASCADE                       
                       """)
    # create_mysql_table('user_course', 'id INT AUTO_INCREMENT PRIMARY KEY, user_id INT, course_id INT, '
    #                                   'FOREIGN KEY (user_id)'
    #                                   'REFERENCES users(id), FOREIGN KEY (course_id) REFERENCES course(id)')
    #

main()