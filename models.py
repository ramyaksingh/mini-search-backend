from app import db
import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(32), nullable=False)
    bookmarks = db.Column(db.String(5000), nullable=True)

    def __repr__(self):
            return self.username

    def __init__(self, username=None, email=None, password=None, bookmarks=''):

        self.username = username
        self.email = email
        self.password = password
        self.bookmarks = bookmarks

    def editPreferences(self, bookmarks=''):

        self.bookmarks = ''

        for bookmark in bookmarks:
            self.bookmarks += bookmark
            self.bookmarks += ","

    def parsePreferences(self, preference):

        if (preference == "") :
            return []

        preference_array = preference.split(',')

        return preference_array

class Stats(db.Model) :
    numID = db.Column(db.Integer, primary_key=True)
    counter =  db.Column(db.Integer, nullable=False)

    def __repr__(self):
            return self.numID + " " + self.counter

    def __init__(self, id=1, counter=0):

        self.numID=id
        self.counter=counter
    
