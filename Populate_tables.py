from Create_tables import *

# create_user(username, email)
# def create_course(name, user, lon, lat, time_to_meet, hrs, url, category, num_participants)

create_user('Elliot', 'elliot@gmail.com')
create_user('Sam', 'sam@gmail.com')
create_user('Simon', 'simon@gmail.com')
create_user('Mattan', 'drMattan@gmail.com')

create_category('Machine Learning')
create_course('Machine Learning for Kids', 'Elliot', 32.0878125, 34.7816723, 'weekend', 3,
              'https://www.coursera.org/learn/machine-learning/home/welcome', 'Machine Learning', 4)
create_course('Creative Writing the plot', 'Mattan', 32.0878125, 34.7816723, 'weekday', 8,
              'https://www.coursera.org/learn/craft-of-plot?specialization=creative-writing', 'Humanities', 3)
create_course('Coding', 'Sam', 32.0878125, 34.7816723, 'weeknight', 4,
              'https://www.coursera.org/learn/html?specialization=web-design', 'Computer Science', 5)
