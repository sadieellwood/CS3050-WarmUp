from firebase_connection import Firebase
import json
import sys

# get arg w/ json file
filename = sys.argv[1]

# converting reading in json data
try:
    with open(filename) as f:
        movie_data = json.load(f)

    # intialize app
    firebase = Firebase()

    currentCollection = firebase.collection.stream()

    # if there are docs in the collection, delete them
    for doc in currentCollection:
        doc.reference.delete()

    # add movies from json
    for movie in movie_data:
        firebase.collection.add(movie)

except FileNotFoundError:
    print("file not found.")
