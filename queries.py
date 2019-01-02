import math
import pymysql
import Create_tables
from address_to_lat_long import address_to_coordinates

KM_TO_DEG_LTD = 110.574
KM_TO_DEG_LON = 111.320


def convert_km_to_deg_longitutde(longitude_km, latitude_km):
    latitude_deg = latitude_km / KM_TO_DEG_LTD
    return longitude_km / (KM_TO_DEG_LON * math.cos(latitude_deg))


def convert_km_to_deg_latitude(latitude_km):
    return latitude_km / KM_TO_DEG_LTD


def query_courses(address, user_category, user_distance, user_hrs_week):
    user_location_latitude, user_location_longitude = address_to_coordinates(address)
    max_long = user_location_longitude + convert_km_to_deg_longitutde(user_distance, user_location_latitude)
    min_long = user_location_longitude - convert_km_to_deg_longitutde(user_distance, user_location_latitude)

    max_lat = user_location_latitude + convert_km_to_deg_latitude(user_distance)
    min_lat = user_location_latitude - convert_km_to_deg_latitude(user_distance)

    mydb = Create_tables.connection()
    mycursor = mydb.cursor()

    sql = """SELECT course.id, course.name
    FROM course INNER JOIN category ON course.category_id=category.category_id
    WHERE (category.name="%s") and
    (course.longitude BETWEEN %f and %f) and 
    (course.latitude BETWEEN %f and %f) and 
    (course.hrs_per_week<=%d)"""
    values = (user_category, min_long, max_long, min_lat, max_lat, user_hrs_week)

    mycursor.execute(sql % values)

    res = mycursor.fetchall()
    return res

print(query_courses('Dizengoff Center, Tel-Aviv', 'Machine Learning', 450, 10))

def course_page(course_id):
    dico = dict()
    SHOW_A_COURSE = "select * from course where id =" + str(course_id)
    MAIL = """select email from
    users inner join course on users.id = course.user_id
    where course.id = """ + str(course_id)

    cnx = Create_tables.connection()
    cur = cnx.cursor()
    cur.execute(SHOW_A_COURSE)
    course = cur.fetchall()
    cur.execute(MAIL)
    mail = cur.fetchall()
    course[0]['mail'] = mail[0]['email']

    return course