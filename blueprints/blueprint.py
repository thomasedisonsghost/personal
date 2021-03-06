import os

from flask import Blueprint, request, redirect, render_template, send_from_directory
from flask.views import MethodView


BLUEPRINT = Blueprint('admin', __name__, template_folder='templates')


class Index(MethodView):
    '''class for index page'''

    def get(self):
        '''get'''
        return render_template('index.html')


class Favicon(MethodView):
    '''class for index page'''

    def get(self):
        '''get'''
        return send_from_directory(os.path.join(BLUEPRINT.root_path, 'static'),
                               '/images/A.ico', mimetype='image/vnd.microsoft.icon')


class Wildcard(MethodView):
    '''class for providing whatever template is requested'''

    def get(self, page):
        '''get'''
        return render_template(page+'.html')

# Register the urls
BLUEPRINT.add_url_rule('/', view_func=Index.as_view('index'))
BLUEPRINT.add_url_rule('/favicon.ico', view_func=Favicon.as_view('favicon.ico'))
BLUEPRINT.add_url_rule('/<page>', view_func=Wildcard.as_view('wildcard'))

BLUE = BLUEPRINT
