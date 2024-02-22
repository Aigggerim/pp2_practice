from datetime import datetime, timedelta

#get current date and time
curent_datetime = datetime.now()
print(f"current date and time: {curent_datetime }")


# second example
#get current date and time
today = datetime.now()

#calculate yesterday
yesterday = today - timedelta(days=1)
#calculate tomorrow
tomorrow = today + timedelta(days=1)

#print results
print("Yesterday:", yesterday.strftime("%Y-%m-%d"))
print("Today:", today.strftime("%Y-%m-%d"))
print("Tomorrow:", today.strftime("%Y-%m-%d"))




