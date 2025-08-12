userName = input("What is your name? ")

if userName == "Kevin" or userName == "kevin":
  print("Hello, " + userName + "!")
  dayOfTheWeek = input("What day of the week is it? ")
  if dayOfTheWeek == "Monday" or dayOfTheWeek == "monday":
    print("Have a great start to your week!", userName)
  if dayOfTheWeek == "Tuesday" or dayOfTheWeek == "tuesday":
    print("Today is Tuesday! and you will have a great day!", userName)
  if dayOfTheWeek == "Wednesday" or dayOfTheWeek == "wednesday":
    print("What a wonderful Wednesday!", userName)
  if dayOfTheWeek == "Thursday" or dayOfTheWeek == "thursday":
    print("Thursday is almost Friday!", userName)
  if dayOfTheWeek == "Friday" or dayOfTheWeek == "friday":
    print("Yay! It's Friday!")
elif userName == "John" or userName == "john":
  print("Hello, " + userName + "!")
  dayOfTheWeek = input("What day of the week is it? ")
  if dayOfTheWeek == "Monday" or dayOfTheWeek == "monday":
    print("Monday's are a great day to start fresh!", userName)
  if dayOfTheWeek == "Tuesday" or dayOfTheWeek == "tuesday":
    print("Tuesday's are great for productivity!", userName)
  if dayOfTheWeek == "Wednesday" or dayOfTheWeek == "wednesday":
    print("Wednesday, halfway through the week, keep it up!", userName)
  if dayOfTheWeek == "Thursday" or dayOfTheWeek == "thursday":
    print("Thursday, almost there!", userName)
  if dayOfTheWeek == "Friday" or dayOfTheWeek == "friday":
    print("TGIF!")
else:
  print("Hello, " + userName + "! I hope you have a great day!")
