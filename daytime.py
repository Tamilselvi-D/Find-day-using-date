 #method 1
import datetime
from datetime import date
import calendar
import random
class Method1:
    def findDay(date):
        day,month,year=(int(i) for i in date.split(' '))
        born = datetime.date(year,month,day)
        return born.strftime("%A")

#method2
class Method2:    
    def findDay(date):
        day ,month , year = (int(i)for i in date.split(' '))
        dayNumber=calendar.weekday(year , month , day)
        days =["Monday"," Tuesday", "Wednesday", "Thursday" , "Friday" , "Saturday"]
        return (days[dayNumber])


#method 3
class Method3:    
    def findDay(date):
        born = datetime.datetime.strptime(date, '%d %m %Y').weekday()
        return (calendar.day_name[born])


date=input("Enter your Date:(day month year)")
method = random.randint(1,3)
print(method)
if(method==1):
    print(Method1.findDay(date))
elif(method==2):
    print(Method2.findDay(date))
else:
    print(Method3.findDay(date))
