from firebase_connection import Firebase
import json
import sys


#get arg w/ json file
filename = sys.argv[1]

#converting reading in json data
try: 
    with open(filename) as f:
        movie_data = json.load(f)

    #intialize app
    firebase = Firebase()

    for movie in movie_data:
        firebase.db.collection(firebase.collection).add(movie)

except FileNotFoundError:
    print("file not found.")






