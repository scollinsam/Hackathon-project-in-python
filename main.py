import queries
import bottle
from bottle import route, run, template, static_file, post, request, get, jinja2_view
from jinja2 import Template
import os
import json
bottle.TEMPLATE_PATH.insert(0, os.getcwd())

info = {}


dummy_data = [{"category": "front end", "address": "18 Shoken Street", "distance": "0km", "hours": "8+"},
              {"category": "back end", "address": "18 Shoken Street", "distance": "0km", "hours": "8+"},]

@route('/')
def index():
    return template("index.html")


@route('/style.css')
def css():
    return static_file("style.css", root='css')

@route('/groups.css')
def css():
    return static_file("groups.css", root='css')


@route('/script.js')
def js():
    return static_file("script.js", root='js')

@route('/groups.js')
def js():
    return static_file("groups.js", root='js')


@get('/form_input')
@jinja2_view('groups.html')
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
    run(host='localhost', port=7000)

if __name__ == '__main__':
    main()