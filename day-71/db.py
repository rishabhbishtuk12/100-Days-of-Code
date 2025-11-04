password = "Baldy1"
salt = 10221
newPassword = f'{password}{salt}'
newPassword = hash(newPassword)