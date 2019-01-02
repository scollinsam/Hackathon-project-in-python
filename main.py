import bottle
from bottle import route, run, template, static_file
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


def main():
    run(host='localhost', port=7000)


if __name__ == '__main__':
    main()