import queries, address_to_lat_long
import bottle
from bottle import route, run, template, static_file, post, request, get, jinja2_view
import os
import sys
from sys import argv
import json
from functools import partial
# bottle.TEMPLATE_PATH.insert(0, os.getcwd())
# print((0, os.getcwd()))
path = sys.path[0]
# the partial makes it possible to write less verbose decorators to choose the html file
view = partial(jinja2_view, template_lookup=['templates'])
info = {}


dummy_data = [{"category": "front end", "address": "18 Shoken Street", "distance": "0km", "hours": "8+"},
              {"category": "back end", "address": "18 Shoken Street", "distance": "0km", "hours": "8+"},]

@get('/')
def index():
    print(path)
    return template(path + "/templates/index.html")


@route('/css/<css_file>')
def css(css_file):
    print("css called")
    return static_file(css_file, root='css')


@get('/group')
@view('group_page.html')
def greet():
    course_id = request.GET.dict['group_id'][0]
    print(course_id)
    course_return = queries.course_page(course_id)
    print(course_return)
    print(course_return["latitude"])
    print(float(course_return["latitude"]))
    address = address_to_lat_long.coordinates_to_address(float(course_return["latitude"]),
                                                         float(course_return["longitude"]))
    return {"course": course_return, "address": address[0]['formatted']}


@get('/form_input')
@view('groups.html')
def send_input():
    category = request.GET.dict['categories'][0]
    print(category)
    address = request.GET.dict['address'][0]
    print(address)
    distance = request.GET.dict['distance'][0]
    print(distance)
    hours = request.GET.dict['hours'][0]
    print(hours)
    db_return = queries.query_courses(address, category, int(distance), int(hours))
    print(db_return)
    return {"groups": db_return}

@route('/set_input')
def show_groups():
    print('in func')
    print(send_input()[1])
    return json.dumps(send_input()[1])


def main():
    run(host='127.0.0.1', port=5432)

if __name__ == '__main__':

    main()