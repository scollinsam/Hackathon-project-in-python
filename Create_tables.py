# import mysql.connector
import pymysql
import psycopg2
import subprocess
import urllib.parse as urlparse
import os

proc = subprocess.Popen('heroku config:get DATABASE_URL -a my-heroku-app', stdout=subprocess.PIPE, shell=True)
db_url = proc.stdout.read().decode('utf-8').strip() + '?sslmode=require'

def create_mysql_db(db_name):
    mydb = psycopg2.connect(db_url)

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
    val = (category,)
    mycursor.execute(sql, val)
    mydb.commit()
    return


def create_course(name, user, lat, lon, time_to_meet, hrs, url, category, num_participants):
    """Create an entry in courses"""
    create_url(url)
    create_category(category)

    mydb = connection()
    mycursor = mydb.cursor()

    sql = """INSERT IGNORE INTO course(name, user_id, longitude, latitude,
                                        time_to_meet, hrs_per_week, url_id, 
                                        category_id, num_participants) VALUES (%s, 
                                        (SELECT ID FROM users WHERE username=%s),
                                        %s, %s, %s, %s,
                                        (SELECT url_id FROM url WHERE url=%s),
                                        (SELECT category_id FROM category WHERE name=%s),
                                        %s) """

    val = (name, user, lon, lat, time_to_meet, hrs, url, category, num_participants)
    mycursor.execute(sql, val)
    mydb.commit()
    return


def create_url(url):
    """Creates new entry in url if the url does not exist yet"""
    mydb = connection()

    mycursor = mydb.cursor()
    sql = """INSERT IGNORE INTO url(url) VALUES(%s)"""
    val = (url,)
    mycursor.execute(sql, val)
    mydb.commit()
    return


def connection():
    return psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
            )
    # return psycopg2.connect(host='127.0.0.1', user='root', passwd='16769thSQL', database='matching')
    # return pymysql.connect(host='db4free.net',
    #                          user='elliotw',
    #                          password='rootless',
    #                          db='matching',
    #                          charset='utf8',
    #                          autocommit=True,
    #                          cursorclass=pymysql.cursors.DictCursor)


def course_page(course_id):
    dico = dict()
    SHOW_A_COURSE = "select * from course where id =" + str(course_id)
    MAIL = """select email from
    users inner join course on users.id = course.user_id
    where course.id = """ + str(course_id)

    cnx = connection()
    cur = cnx.cursor()
    cur.execute(SHOW_A_COURSE)
    course = cur.fetchall()
    cur.execute(MAIL)
    mail = cur.fetchall()
    course[0]['mail'] = mail[0]['email']

    print(course)
    # dico['id'] = course[0]
    # dico['name'] = course[1]
    # dico['user_id'] = course[2]
    # dico['longitude'] = course[3]
    # dico['latitude'] = course[4]
    # dico['time_to_meet'] = course[5]
    # dico['hrs_per_week'] = course[6]
    # dico['url_id'] = course[7]
    # dico['category_id'] = course[8]
    # dico['num_participants'] = course[9]
    # dico['mail'] = mail

    return dico

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
                       num_participants INT,
                       FOREIGN KEY (user_id) REFERENCES users(id),
                       FOREIGN KEY (url_id) REFERENCES url(url_id) ON DELETE CASCADE,
                       FOREIGN KEY (category_id) REFERENCES category(category_id) ON DELETE CASCADE                       
                       """)
    # create_mysql_table('user_course', 'id INT AUTO_INCREMENT PRIMARY KEY, user_id INT, course_id INT, '
    #                                   'FOREIGN KEY (user_id)'
    #                                   'REFERENCES users(id), FOREIGN KEY (course_id) REFERENCES course(id)')
main()