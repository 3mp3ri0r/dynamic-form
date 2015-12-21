""" ``views`` module.
"""

from datetime import timedelta

from wheezy.web.handlers import BaseHandler

from models import Registration


class SignupHandler(BaseHandler):

    def get(self, registration = None):
        registration = registration or Registration()
        return self.render_response(
            'signup.html',
            account=registration.account,
            phone=registration.phone)

    def post(self):
        registrasi = Registrasi()
        if (not self.try_update_model(registration)):
            registration.account.password = ''
            return self.get(registration)
        return self.see_other_for('signup')
