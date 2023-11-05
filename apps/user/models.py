from apps.base.utils import db

class User():
    username = None
    email = None
    firstName = None
    lastName = None
    firebaseId = None
    fields = ["firebaseId", "username", "email", "firstName", "lastName"]

    def __init__(self, username, email, firstName, lastName, firebaseId) -> None:
        self.username = username
        self.email = email
        self.firstName = firstName
        self.lastName = lastName
        self.firebaseId = firebaseId

    def doc(self):
        return {
            "username": self.username,
            "email": self.email,
            "firstName": self.firstName,
            "lastName": self.lastName,
            "fullName": self.firstName + "-" + self.lastName,
            "firebaseId": self.firebaseId
        }
    
    def is_valid(self):
        if not all(getattr(self, field) for field in self.fields):
            return False
        else:
            return True
        
UserCollection = db["users"]