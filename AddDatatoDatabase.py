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
        },
    "321654":
        {
            "name": "Murtaza Hassan",
            "major": "Robotics",
            "starting_year": 2017,
            "total_attendance": 7,
            "standing": "M",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "852741":
        {
            "name": "Emly Blunt",
            "major": "Economics",
            "starting_year": 2021,
            "total_attendance": 12,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "963852":
        {
            "name": "Elon Musk",
            "major": "Physics",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        }
}

# Sending the data to Realtime firebase database
for key, value in data.items():
    ref.child(key).set(value)