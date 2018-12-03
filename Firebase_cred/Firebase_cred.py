import firebase_admin
from firebase_admin import credentials

firebase_certificate_path = ""  # Your Firebase certificate json file location
database_url = "" # Your Firebase database url

def initial():
    cred = credentials.Certificate(firebase_certificate_path)
    firebase_admin.initialize_app(cred, {
        'databaseURL': database_url
    })
