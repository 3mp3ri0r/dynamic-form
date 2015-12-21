""" ``urls`` module.
"""

from wheezy.routing import url
from wheezy.web.handlers import file_handler

from views import SignupHandler


all_urls = [
    url('', SignupHandler, name='signup'),
    url('static/{path:any}',
        file_handler(root='static/'),
        name='static')
]
