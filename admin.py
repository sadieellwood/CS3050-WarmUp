import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json
import sys


#get arg w/ json file
filename = sys.argv[1]

#converting reading in json data
try: 
    with open(filename) as f:
        movie_data = json.load(f)

    #intialize app
    cred = credentials.Certificate("warmup-project-6eac2-firebase-adminsdk-fbsvc-0dc17a627a.json")
    app = firebase_admin.initialize_app(cred)
    db = firestore.client()

    for movie in movie_data:
        db.collection("movies").add(movie)

except FileNotFoundError:
    print("file not found.")






