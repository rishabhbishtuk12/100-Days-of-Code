class character:
    name = None
    health = 100
    magicPoints = 100

    def __init__(self, name):
        self.name = name
    
    def print(self):
        print(f"Name: {self.name}\nHP: {self.health}\nMP: {self.magicPoints}")
    
    def setStats(self,health,magicPoints):
        self.health = health
        self.magicPoints = magicPoints
    
class player(character):
    nickName = None
    lives = 3

    def __init__(self,nickName):
        name = "Player"
        self.nickName = nickName

    def print(self):
        print(f"Nick Name: {self.nickName}\nLives: {self.lives}")
    
    def alive(self):
        if self.lives > 0:
            print(f"{self.nickName} lives on!")
            return True
        else:
            print(f"{self.nickName} lives Off!")
            return False

class enemy(character):
    type: None
    strength : None

    def __init__(self,name, type,strength):
        self.name = name
        self.type = type
        self.strength = strength

    def print(self):
        print(f"{self.name}\nHP: {self.health}\n MP: {self.magicPoints}\nType: {self.type}\nStrength: {self.strength}")

class orc(enemy):
    speed = None

    def __init__(self,speed):
        self.name = "Orc"
        self.type = "Type"
        self.speed = speed
        self.strength = 200

    def print(self):
        print(f"{self.name}\n HP: {self.health}\n MP: {self.magicPoints}\nType: {self.type}\nStrength: {self.strength}\nSpeed: {self.speed}")

class vampire(enemy):
    day = True

    def __init__(self,day):
        self.name = "Vampire"
        self.type = "Vampire"
        self.strength = 150
        self.day = day

    def print(self):
        print(f"{self.name}\nHP: {self.health}\nMP: {self.magicPoints}\nType: {self.type}\nStrength: {self.strength}\nDay: {self.day}")

print("🌟Generic RPG🌟")
print()
print("Player\n")
cha = character("Rishabh ")
cha.print()
ian = player("Ian the mighty")
ian.print()
ian.alive()

print()
sharron = orc(250)
gary = orc(205)

sharron.print()
print()
gary.print()
print()
eric = vampire(False)
eric.print()