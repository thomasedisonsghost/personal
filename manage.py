'''
to run server:
python manage.py
'''

# Set the path
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

from werkzeug.wsgi import DispatcherMiddleware

from blueprints.blueprint import BLUE

from business_logic.app_maker import make_app



BASE_APP = make_app(BLUE)

APP_LAYOUT = {

}

if __name__ == "__main__":
    APPLICATION = DispatcherMiddleware(BASE_APP, APP_LAYOUT)
    HTTP_SERVER = HTTPServer(WSGIContainer(APPLICATION))
    HTTP_SERVER.listen(80)
    IOLoop.instance().start()
