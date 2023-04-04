month=int(input("Enter the month: "))
day=int(input("Enter the day of the month: "))
year=int(input("Enter the year in two digit format: "))
if(month>12 or month<0):
   print("Error: Invalid Month Input")
elif(day>31 or day<0):
  print("Error: Invalid day Input")
elif(year>99 or year<0):  
   print("Error: Invalid year Input")
else:
  print("successful you  have entered correct date ")
  print("date:",month,"/",day,"/",year)