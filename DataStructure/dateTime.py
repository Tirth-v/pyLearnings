from time import time, ctime, localtime
from datetime import datetime, timedelta,date

epoch = time()
print(epoch)

et = ctime()
print(et)
lt = localtime()
print(lt)
print(lt.tm_year)

a = datetime(year = 2022, month = 3, day = 31)
print(a)

dt = datetime(year = 2021, month = 5, day = 20, hour = 15, minute = 35)
print(dt)

dt = datetime(2022,1,31)
print(dt)

dt = (2016, 5, 31, 15, 35)
print(dt)

print(datetime.now())
print(datetime.today())
print(datetime.today().hour)
td = timedelta(days = 10)
d = date.today()
print("Today date:{}, Next date:{}".format(d, d+td))

