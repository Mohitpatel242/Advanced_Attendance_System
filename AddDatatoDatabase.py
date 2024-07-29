import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Connecting the Firebase database to project
cred = credentials.Certificate("serviceAccountKey.json")   # used json file as database
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendacerealtime-80089-default-rtdb.firebaseio.com/"  # RealTime database URL from Firebase Project to connect the database
})

ref = db.reference('Students')

data = {
    "242005":
        {
            "name": "Mohit Patel",
            "major": "Robotics",
            "starting_year": 2024,
            "total_attendance": 0,
            "standing": "M",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        }
}

# Sending the data to Realtime firebase database
for key, value in data.items():
    ref.child(key).set(value)
