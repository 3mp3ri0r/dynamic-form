""" ``views`` module.
"""

from datetime import timedelta

from wheezy.core.collections import attrdict
from wheezy.core.descriptors import attribute
from wheezy.web.handlers import BaseHandler

from models import Registration


class SignupHandler(BaseHandler):

    @attribute
    def model(self):
        return attrdict({
            'HP': [''],
        })

    def get(self, registration = None):
        query = self.request.query
        registration = registration or Registration()
        print(self.model)
        if 'HP' in query:
            self.model['HP'].append('')
        return self.render_response(
            'signup.html',
            account=registration.account,
            phone=registration.phone,
            model=self.model)

    def post(self):
        registration = Registration()
        if (not self.try_update_model(registration) &
                self.try_update_model(self.model)):
            print("Masmasssss!!!!!!!!!!!!!")
            registration.account.password = ''
            return self.get(registration)
        print("Masuk!!!!!!!!!!!!!")
        print(registration.account.username)
        print(self.model.HP[0])
        print(self.model.HP[1])
        return self.see_other_for('signup')
