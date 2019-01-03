import bottle
from bottle import route, run, template, static_file, post, request, get, jinja2_view
import os
import json
from functools import partial
bottle.TEMPLATE_PATH.insert(0, os.getcwd())

# the partial makes it possible to write less verbose decorators to choose the html file
view = partial(jinja2_view, template_lookup=['templates'])
info = {}

@route('/')
def index():
    return template("index.html")


@route('/style.css')
def css():
    return static_file("style.css", root='css')


@route('/group/group_page.css')
def css():
    print("css called")
    return static_file("group_page.css", root='css')


@route('/script.js')
def js():
    return static_file("script.js", root='js')

@route('/groups.js')
def js():
    return static_file("groups.js", root='js')

@route('/group/<name>')
@view('group_page.html')
def greet(name='Stranger'):
    name_r = "Data Science NLP"
    organiser_r = "Simono"
    level_r = "Beginner"
    location_r = "rothschild area"
    frequency_r = "6h/week"
    return {'name': name_r, 'organiser': organiser_r, 'level':level_r, 'location':location_r, 'frequency':frequency_r}
    # return template('Hello {{name}}, how are you?', name=name)

@get('/form_input')
def send_input():
    category = request.GET.dict['categories'][0]
    print(category)
    address = request.GET.dict['address'][0]
    distance = request.GET.dict['distance'][0]
    hours = request.GET.dict['hours'][0]
    info["category"] = category
    info["address"] = address
    info["distance"] = distance
    info["hours"] = hours
    print(info)
    return template("groups.html")

@route('/set_input')
def show_groups():
    print("in function")
    return json.dumps(info)


def main():
    run(host='localhost', port=7000)

if __name__ == '__main__':
    main()