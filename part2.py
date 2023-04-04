RED='red'
BLUE='blue'
YELLOW='yellow'
Col1=input("Enter the first primary color in lower case letters:")
Col2=input("Enter the second primary color in lower case letters:")
if Col1==RED:
    if Col2==BLUE:
        print("Purple")
    elif Col2==YELLOW:
        print("Orange")
    elif Col2==RED:
        print("ERROR: The two colours you entered are same")
    else:
        print("ERROR: Invalid Colour2")
elif Col1==BLUE:
    if Col2==RED:
        print("Purple")
    elif Col2==YELLOW:
        print("Green")
    elif Col2==BLUE:
        print("ERROR: The two colours you entered are same")
    else:
        print("ERROR: Invalid Colour2")
elif Col1==YELLOW:
    if Col2==BLUE:
        print("Green")
    elif Col2==RED:
        print("Orange")
    elif Col2==YELLOW:
        print("ERROR: The two colours you entered are same")
    else:
        print("ERROR: Invalid Colour2")
else:
    print("ERROR: Invalid Color1")