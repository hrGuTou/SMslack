import MySQLdb
from Firebase_cred import Firebase_cred
from firebase_admin import db

Firebase_cred.initial()
root = db.reference()
user = root.child("User")
message = root.child("Message")


def insINFO(data):
    name = data["Name"]
    email = data["Email"]
    sex = data["Sex"]
    teamName = data["Team Name"]
    projectName = data["Project Name"]
    projectStatus = data["Project Status"]
    phoneNum = data["PhoneNumber"]

    try:
        user.child(phoneNum).set({
            "Name":name,
            "Email": email,
            "Sex":sex,
            "Team Name":teamName,
            "Project Name":projectName,
            "Project Status":projectStatus,
            "Phone Number": phoneNum
        })

    except Exception as e:
        print(e)


if __name__ == "__main__":
    data = {'Name': 'GG', 'Email': 'hrgutou@gmail.com', 'Sex': 'M', 'Team Name': 'on9', 'Project Name': 'smslack', 'Project Status': 'I', 'PhoneNumber': '+13476680632'}
    insINFO(data)
