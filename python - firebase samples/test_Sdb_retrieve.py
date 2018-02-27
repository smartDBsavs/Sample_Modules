import pyrebase

config = {
  "apiKey": "apiKey",
  "authDomain": "smartdoorbell-9ecf1.firebaseapp.com",
  "databaseURL": "https://smartdoorbell-9ecf1.firebaseio.com/",
  "storageBucket": "smartdoorbell-9ecf1.appspot.com"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()
all_users = db.child("Registration Details").get()
for user in all_users.each():
    print(user.key())
    print(user.val()) 
