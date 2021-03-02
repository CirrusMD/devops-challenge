from bottle import route, run, template
import socket

@route('/healthcheck')

def healthcheck():
    return template('<b>host: {{hostname}}</b>', hostname=socket.gethostname())

run(host='0.0.0.0', port=8080)
