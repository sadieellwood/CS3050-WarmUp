from firebase_connection import Firebase


firebase = Firebase()
results = firebase.perform_firebase_query({'expr1': {'field': 'title', 'comparison_op': '==', 'value': "Tetsuo The Bullet Man"}, 'logical_op': 'OR', 'expr2': {'field': 'rating', 'comparison_op': '>', 'value': 4.0}})

for n in results:
    print(n)