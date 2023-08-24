from datetime import datetime
import time

dt = datetime(2018, 1, 1)
print(dt)
dtn = datetime.now()
print(dtn)
# convert string to datetime
dts = datetime.strptime("2018/01/01", "%Y/%m/%d")
print(dtn)

# from time object
dtt = datetime.fromtimestamp(time.time())
print(dtt)

print(f"{dtt.year}/ {dtt.month}")

# datetime to string
print(dtt.strftime("%Y/%m"))
