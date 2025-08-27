class Credential:
    def __init__(self, site, username, password):
        self.site = site
        self.username = username
        self.password = password

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.credentials = []

