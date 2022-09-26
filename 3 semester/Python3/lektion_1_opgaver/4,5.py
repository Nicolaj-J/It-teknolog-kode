from datetime import datetime

now = datetime.now()

print("This is the hour of day: ", now.hour)
if(input("Are you biking: ") == "Yes" and now.hour < 8 and now.hour > 18):
    print("Turn on light")
else:
    print("You dont have to turn on light")