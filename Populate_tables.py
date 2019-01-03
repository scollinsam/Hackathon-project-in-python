from Create_tables import *
import numpy as np

# create_user(username, email)
# def create_course(name, user, lat, lon, time_to_meet, hrs, url, category, num_participants)

create_user('Elliot', 'elliot@gmail.com')
create_user('Sam', 'sam@gmail.com')
create_user('Simon', 'simon@gmail.com')
create_user('Mattan', 'drMattan@gmail.com')
create_user('Gabriel', 'gabs@gmail.com')

# create_category('Machine Learning')
# create_course('Machine Learning for Kids', 'Elliot', 32.0878125, 34.7816723, 'weekend', 3,
#               'https://www.coursera.org/learn/machine-learning/home/welcome', 'Machine Learning', 4)
# create_course('Creative Writing the plot', 'Mattan', 32.0878125, 34.7816723, 'weekday', 8,
#               'https://www.coursera.org/learn/craft-of-plot?specialization=creative-writing', 'Humanities', 3)
# create_course('Coding', 'Sam', 32.0878125, 34.7816723, 'weeknight', 4,
#               'https://www.coursera.org/learn/html?specialization=web-design', 'Computer Science', 5)
#
# create_course('Pandas for Kids', 'Sam', 32.0878125, 34.7816723, 'weeknight', 4,
#               'https://www.coursera.org/learn/html?specialization=web-design', 'Data Science', 5)
time_to_meet = ['weeknight', 'weekday', 'weekend']
categories = ["front-end", "back-end", "entrepreneurship", "data-science",
              "accounting", "investment-strategy", "net-security"]

create_course('Jinja', 'Mattan', 32.0597122, 34.7596126, time_to_meet[np.random.randint(0, len(time_to_meet))],
              np.random.randint(1, 11), 'https://www.coursera.org/lecture/gcp-fundamentals-aws/concepts-part-1-8DZRv',
              categories[0], np.random.randint(3, 11))
create_course('MySQL', 'Elliot', 32.0597122, 34.7596126, time_to_meet[np.random.randint(0, len(time_to_meet))],
              np.random.randint(1, 11), 'https://www.mysqlcourse.co.il',
              categories[1], np.random.randint(3, 11))
create_course('Clickbait 101', 'Simon', 32.0597122, 34.7596126, time_to_meet[np.random.randint(0, len(time_to_meet))],
              np.random.randint(1, 11), 'https://www.youwillneverbelieveit.com',
              categories[2], np.random.randint(3, 11))
create_course('Time Serious', 'Gabriel', 32.0597122, 34.7596126, time_to_meet[np.random.randint(0, len(time_to_meet))],
              np.random.randint(1, 11), 'https://www.timemachine.com',
              categories[3], np.random.randint(3, 11))
create_course('Doing your own taxes', 'Mattan', 32.0597122, 34.7596126, time_to_meet[np.random.randint(0, len(time_to_meet))],
              np.random.randint(1, 11), 'https://www.turbotax.com',
              categories[4], np.random.randint(3, 11))
create_course('Value Investing', 'Elliot', 32.0597122, 34.7596126, time_to_meet[np.random.randint(0, len(time_to_meet))],
              np.random.randint(1, 11), 'https://www.buffet.com',
              categories[5], np.random.randint(3, 11))
create_course('Fraud Prevention for IT', 'Simon', 32.0597122, 34.7596126, time_to_meet[np.random.randint(0, len(time_to_meet))],
              np.random.randint(1, 11), 'https://www.dontclickthis.com',
              categories[6], np.random.randint(3, 11))

create_course('HTML5', 'Mattan', 32.0728258,34.7789535, time_to_meet[np.random.randint(0, len(time_to_meet))],
              np.random.randint(1, 11), 'https://www.coursera.org/learn/html',
              categories[0], np.random.randint(3, 11))
create_course('Server-Side Development', 'Elliot', 32.0728258,34.7789535, time_to_meet[np.random.randint(0, len(time_to_meet))],
              np.random.randint(1, 11), 'https://www.coursera.org/learn/server-side-nodejs',
              categories[1], np.random.randint(3, 11))
create_course('Spotting the Opportunity', 'Simon', 32.0728258,34.7789535, time_to_meet[np.random.randint(0, len(time_to_meet))],
              np.random.randint(1, 11), 'https://www.coursera.org/learn/wharton-entrepreneurship-opportunity',
              categories[2], np.random.randint(3, 11))
create_course('Big Data with Spark', 'Gabriel', 32.0728258,34.7789535, time_to_meet[np.random.randint(0, len(time_to_meet))],
              np.random.randint(1, 11), 'https://www.coursera.org/learn/big-data-machine-learning?specialization=big-data',
              categories[3], np.random.randint(3, 11))
create_course('Intro to Financial Accounting', 'Elliot', 32.0728258,34.7789535, time_to_meet[np.random.randint(0, len(time_to_meet))],
              np.random.randint(1, 11), 'https://www.coursera.org/learn/wharton-accounting',
              categories[4], np.random.randint(3, 11))
create_course('Risk Management', 'Simon', 32.0728258,34.7789535, time_to_meet[np.random.randint(0, len(time_to_meet))],
              np.random.randint(1, 11), 'https://www.coursera.org/learn/portfolio-selection-risk-management',
              categories[5], np.random.randint(3, 11))
create_course('Computer Network Security', 'Gabriel', 32.0728258,34.7789535, time_to_meet[np.random.randint(0, len(time_to_meet))],
              np.random.randint(1, 11), 'https://www.coursera.org/specializations/computer-network-security',
              categories[6], np.random.randint(3, 11))
