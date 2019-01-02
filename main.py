import bottle
from bottle import route, run, template, static_file, post, request, get
import os
import json
bottle.TEMPLATE_PATH.insert(0, os.getcwd())

info = {}

@route('/')
def index():
    return template("index.html")


@route('/style.css')
def css():
    return static_file("style.css", root='css')


@route('/script.js')
def js():
    return static_file("script.js", root='js')

@route('/groups.js')
def js():
    return static_file("groups.js", root='js')


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