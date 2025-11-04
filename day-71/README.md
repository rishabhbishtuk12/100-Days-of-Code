# It's Called Hashing

One of the big issues with storing usernames and passwords in a database is what happens if we're hacked?

If those passwords are stored as text, our users' security is compromised. Probably across multiple sites because they ignored our advice and used the same password for everything!!!!!

## Hashing

In reality, organizations don't store your actual password. They store a hash of your password. A hash is produced by turning your password into a sequence of numbers, then passing it though a hashing algorithm (some mathematical process that is very difficult to reverse engineer). The data spit out of this hashing algorithm is what's stored instead of your actual password.

👉 So let's do it. I'm using the built-in `hash` function to create a numerical hash of the password.

```py
password = "baldy1"
password = hash(password)
print(password)

# This will output a really long number
```

Play around with different strings on line 1 and notice how the hash number completely changes.

# Oooh, Salty!

Hashing is great, but enterprising hackers have created their own database containing hashes of pretty much every word and common password around.

So chances are, if you use a common password or everyday word, then there's a hash of it sitting around on the internet somewhere just waiting for a reverse lookup.

To help combat this, we can generate a random value and append it to the end of your password before hashing. This random value is called a salt.

👉 Let's salt our password hash from before.

```py
from replit import db
password = "Baldy1"
salt = 10221
newPassword = f"{password}{salt}" # append the salt
newPassword = hash(newPassword) # hash the lot
print(newPassword)
```
