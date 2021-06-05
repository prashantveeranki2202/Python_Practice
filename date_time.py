import datetime

# Defining variables #

today_date=datetime.date.today()
yesterday_date=today_date-datetime.timedelta(days=1)
lastweek_date=today_date-datetime.timedelta(days=7)

str3=str(input("Enter the day: ")).strip()

# Defining the function to compare the input as today, yesterday, lastweek and returns the date

def my_function1(str2):
  str1=str2
  if str1=="today":
    return(today_date)
  elif str1=="yesterday":
    return(yesterday_date)
  elif str1=="lastweek":
    return(lastweek_date)
  else:
    return

output=my_function1(str3)
print(output)




