print("who many sec is in this year")

sec = 60
min = 60
hr = 24
fdays = 28
day1 = 30
day = 31

daySec = sec*min*hr
month = (7*day) + (4*day1) + 28

lYear = input ("Is it a Leap year ? ")
if lYear == "yes" or lYear == "Yes" or lYear == "YES" :
  month = month + 1
  total = daySec * month

  print("There are ", total , "seconds in this year ")
elif lYear == "No" or lYear == "no" or lYear == "NO":
  total = daySec * month
  print("There are ", total , "seconds in this year ")
else:
  print("Whatt.. ?")