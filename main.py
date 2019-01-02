import bottle
from bottle import route, run, template, static_file, post, request
import os
bottle.TEMPLATE_PATH.insert(0, os.getcwd())

@route('/')
def index():
    return template("index.html")


@route('/style.css')
def css():
    return static_file("style.css", root='css')


@route('/script.js')
def js():
    return static_file("script.js", root='js')


@post('/form_input')
def send_input():
    result_dict = []
    category = request.POST.get("categories")
    address = request.POST.get("address")
    distance = request.POST.get("distance")
    hours = request.POST.get("hours")
    return

def main():
    run(host='localhost', port=7000)


if __name__ == '__main__':
    main()