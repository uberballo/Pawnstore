from flask_login import AnonymousUserMixin
class Anonymous(AnonymousUserMixin):
    def __init__(self):
      self.username = 'Guest'
      self.role = ['GUEST']
    
    def roles(self):
        return self.role