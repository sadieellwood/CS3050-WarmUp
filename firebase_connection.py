import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud.firestore_v1.base_query import FieldFilter, Or


class Firebase:

    cred = credentials.Certificate(
        "warmup-project-6eac2-firebase-adminsdk-fbsvc-0dc17a627a.json"
    )
    app = firebase_admin.initialize_app(cred)
    collection = firestore.client().collection("movies")

    """
    Takes a dictionary containing the query specs and returns a dictionary of the firebase query results
    """

    def perform_firebase_query(self, query_spec: dict):
        if "OR" in query_spec.values():

            query = self.collection.where(
                filter=Or([
                    FieldFilter(
                        query_spec["expr1"]["field"],
                        query_spec["expr1"]["comparison_op"],
                        query_spec["expr1"]["value"],
                    ),
                    FieldFilter(
                        query_spec["expr2"]["field"],
                        query_spec["expr2"]["comparison_op"],
                        query_spec["expr2"]["value"],
                    ),
                ])
            )

        else: 

            query = self.collection.where(filter=FieldFilter(
                query_spec["expr1"]["field"],
                query_spec["expr1"]["comparison_op"],
                query_spec["expr1"]["value"],
            ))

            if "AND" in query_spec.values():
                query = query.where(filter=FieldFilter(
                    query_spec["expr2"]["field"],
                    query_spec["expr2"]["comparison_op"],
                    query_spec["expr2"]["value"],
                ))

        # convert query results to a list of dictionaries, each dictionary containing the info on a single doc
        results = query.get()

        response = []
        for document in results:
            response.append(document.to_dict())

        return response

    def perform_firebase_trial(self):
        # construct query
        """
        query = self.db.collection(self.collection).where(
                filter=Or(
                        [
                            FieldFilter("rating", ">", 6.7),
                            FieldFilter("title", "==", "One Breath"),
                        ]
                    )
                )
        """

        query = (
            self.db.collection(self.collection)
            .where(filter=FieldFilter("rating", "==", 5))
            .get()
        )

        return query
