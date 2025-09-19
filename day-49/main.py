print("HIGH SCORE TABLE\n")
f = open("high.scores", "r")
contents = f.readline().split("\n")
f.close()

highScore = 0
name = None

for row in contents:
    data = row.split()
    if data !=[]:
        if int(data[1]) > highScore:
            highScore = data[1]
            name = data[0]
print("The winner is", name, "with", highScore)