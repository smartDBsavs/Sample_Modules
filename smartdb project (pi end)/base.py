import sys
import pyrebase

config = {
  "apiKey": "apiKey",
  "authDomain": "pytest-b592f.firebaseapp.com",
  "databaseURL": "https://pytest-b592f.firebaseio.com/",
  "storageBucket": "pytest-b592f.appspot.com"
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

#db = firebase.database()
#db.child("/users").child("Morty")

storage = firebase.storage()
# as admin
storage.child(sys.argv[1]).put(sys.argv[1])
print ("File upload success")
