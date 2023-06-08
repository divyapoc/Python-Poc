import datetime as dt

d = dt.date.today()
print(d)

d1 = dt.datetime.today()
print(d1)
print(d1.time())

d2 = dt.datetime(2023,3,1)
print(d2)

year = dt.datetime(2023,1,1)
current = dt.datetime.now()
print("days left=",year-current)

#strftime Method - converts date object into readable string

d4 = dt.datetime(2023,3,1)
print(d4.strftime("%Y"))  #full year
print(d4.strftime("%B")) # full month
print(d4.strftime("%A"))  # day

