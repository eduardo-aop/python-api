from flask import Flask
from app.src.free_fair.rest_service import free_fair
import app.src.imports.service

server = Flask(__name__)

server.register_blueprint(free_fair, url_prefix='/freeFairs')


@server.route('/')
def init():
    return 'Hello world ha'


if __name__ == '__main__':
    # entries = os.listdir()
    # print(entries)
    server.run(host='0.0.0.0')

