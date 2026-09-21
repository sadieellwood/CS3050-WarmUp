import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud.firestore_v1.base_query import FieldFilter, Or

class Firebase:

    collection = "movies"
    cred = credentials.Certificate("warmup-project-6eac2-firebase-adminsdk-fbsvc-0dc17a627a.json")
    app = firebase_admin.initialize_app(cred)
    db = firestore.client()

    def perform_firebase_query(self, query_spec: dict):
        #construct query
        query = self.db.collection(self.collection).where(
        filter=Or(
                [
                    FieldFilter("rating", ">", 6.7),
                    FieldFilter("title", "==", "One Breath"),
                ]
            )
        )

        docs = query.get()
        return docs

    def perform_firebase_trial(self):
        #construct query
        query = self.db.collection(self.collection).where(
        filter=Or(
                [
                    FieldFilter("rating", ">", 6.7),
                    FieldFilter("title", "==", "One Breath"),
                ]
            )
        )

        docs = query.get()
        return docs