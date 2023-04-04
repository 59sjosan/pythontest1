month=int(input("Enter the month: "))
day=int(input("Enter the day of the month: "))
year=int(input("Enter the year in two digit format: "))
if(month>12):
  print("Error:Invalid Month Input")
elif(day>31):
  print( "Error: Invalid Day Input")
elif(year>20):
  print("Error: Invalid Year Input")
else:
  print(month,"/", day,"/", year)
  print("Success: Congratulations! you entered the correct date.")