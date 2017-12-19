import pyrebase

config = {
  "apiKey": "apiKey",
  "authDomain": "pytest-b592f.firebaseapp.com",
  "databaseURL": "https://pytest-b592f.firebaseio.com/",
  "storageBucket": "pytest-b592f.appspot.com"
}

firebase = pyrebase.initialize_app(config)

#db = firebase.database()
#db.child("/users").child("Morty")


storage = firebase.storage()
# as admin
storage.child("wxample.jpg").put("C:\\Users\\Lenovo\\Anaconda3\\desert.jpg")

#storage.child("/home/vjk/Documents/batman vs superman.png")