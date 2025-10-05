import datetime,os,time

while True:
    os.system("clear")
    print("Event Countdown")
    today = datetime.date.today()
    day = int(input("Day : "))
    month = int(input("Month : "))
    year = int(input("Year : "))
    diff = datetime.date(year, month, day)
    mydate = (diff-today)
    mydate = mydate.days
    print()
    if today < diff:
        print(f"{mydate} days to go")
    elif today > diff:
        print(f"😭😭😭😭😭😭😭 You missed it by {mydate} days!")
    else:
        print("🥳🥳🥳🥳🥳🥳🥳 Today!")
    time.sleep(1)