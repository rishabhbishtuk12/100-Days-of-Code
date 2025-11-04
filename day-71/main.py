import db



ans = input("Password: ")
salt = db.salt
newPassword = f'{ans}{salt}'
newPassword = hash(newPassword)

if newPassword == db.newPassword:
    print("Login successful")