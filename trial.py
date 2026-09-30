from firebase_connection import Firebase
from datetime import datetime, timezone


firebase = Firebase()
# print(datetime.fromisoformat("2015-05-13T20:00:00-04:00"))
thedate = datetime.fromisoformat("2010-10-15" + " 00:00:00").replace(tzinfo=timezone.utc)
results = firebase.perform_firebase_query({'expr1': {'field': 'date', 'comparison_op': '==', 'value': thedate}})

for n in results:
    print(n)



#datetime.fromisoformat("string")