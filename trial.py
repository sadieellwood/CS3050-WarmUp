from firebase_connection import Firebase


firebase = Firebase()
docs = firebase.perform_firebase_trial()

for doc in docs:
    print(doc.to_dict())