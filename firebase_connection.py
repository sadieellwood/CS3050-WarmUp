import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud.firestore_v1.base_query import FieldFilter, Or

def intialize_connection():
    #intialize connection to the app
    cred = credentials.Certificate("warmup-project-6eac2-firebase-adminsdk-fbsvc-0dc17a627a.json")
    app = firebase_admin.initialize_app(cred)
    db = firestore.client()

    return db


def getData():
    collection = db.collection(COLLECTION)

    query = collection.where(
    filter=Or(
            [
                FieldFilter("rating", ">", 6.7),
                FieldFilter("title", "==", "One Breath"),
            ]
        )
    )

    docs = query.get()
    return docs
