from datetime import datetime, timedelta

dt1 = datetime(2018, 1, 1) + timedelta(1)
dt2 = datetime.now()

duration = dt2 - dt1
print(duration)
print("days", duration.days)
print("seconds", duration.seconds)
print("Total seconds", duration.total_seconds())
