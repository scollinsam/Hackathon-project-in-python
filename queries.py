import math
import mysql.connector

KM_TO_DEG_LTD = 110.574
KM_TO_DEG_LON = 111.320
def convert_km_to_deg(longitude_km, latitude_km):
    latitude_deg = latitude_km / KM_TO_DEG_LTD
    longitude_deg = longitude_km / (KM_TO_DEG_LON * math.cos(latitude_deg))
    return {"longitude_deg": longitude_deg, "latitude_deg": latitude_deg}

def query_courses(user_location, user_category, user_distance, user_hrs_week):
    mydb = mysql.connector.connect(host='localhost', user='root', passwd='rootless')
    mycursor = mydb.cursor()

    sql = """SELECT id, name
    FROM course INNER JOIN category ON course. 
    WHERE location=%s and """
    mycursor
