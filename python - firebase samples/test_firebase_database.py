
from firebase import firebase
firebase = firebase.FirebaseApplication('https://pytest-b592f.firebaseio.com', None)
new_user = 'vx'

result = firebase.post('/users', {'Three':'hello'})
#result = firebase.post('/users', new_user, {'print': 'pretty'}, {'X_FANCY_HEADER': 'VERY FANCY'})
# result = firebase.get('/users', None)
print (result)