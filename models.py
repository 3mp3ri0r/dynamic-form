""" ``models`` module.
"""

from datetime import datetime


class Account(object):
    username = ''
    email = ''
    password = ''
    address = ''
    birthdate = str(datetime.now().strftime("%Y-%m-%d"))


class Phone(object):
    
    def __init__(self):
        self.phone = []


class Registration(object):
    
    def __init__(self):
        self.account = Account()
        self.phone = Phone()
