from flask import Flask
# import config
from free_fair.rest_service import free_fair

server = Flask(__name__)

server.register_blueprint(free_fair, url_prefix='/freeFairs')


@server.route('/')
def init():
    return 'Hello world ha'


if __name__ == '__main__':
    server.run(host='0.0.0.0')

