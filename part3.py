def convertSalary(a,b):
    if b.lower()=='canada':
        a*=1.55
        if a<64000:
            return 'You will be poor in '+b+' with a salary of '+str(a)+' CAD'
        else:
            return 'You will be rich in '+b+' with a salary of '+str(a)+' CAD'
    if b.lower()=='usa':
        if a<56516:
          return 'You will be poor in '+b+' with a salary of '+str(a)+' US Dollars'
        else:
          return 'You will be rich in '+b+' with a salary of '+str(a)+' US Dollars'
    if b.lower()==' uk':
        if a<35423:
          return 'You will be poor in '+b+' with a salary of '+str(a)+' Pound Sterling'
        else:
           return 'You will be rich in '+b+' with a salary of '+str(a)+' pound sterling' 
    if b.lower()==' cambodia':
         if a<5649856:  
           return 'You will be poor in '+b+' with a salary of '+str(a)+' Cambodian Riel'
         else:
            return 'You will be rich in '+b+' with a salary of '+str(a)+' Cambodian Rel'

money=float(input("Please enter your salary in Germany:"))
country=input("Enter the country you want to migrate to:")
print(convertSalary(money,country))