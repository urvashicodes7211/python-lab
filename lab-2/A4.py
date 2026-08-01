"""Write a program to display the day's name according to the number given by the 
user. """

n = int(input("Enter number of day: "))
if(n==1):
    print("Sunday")
elif(n==2):
    print("Monday")
elif(n==3):
    print("Tuesday")
elif(n==4):
    print("Wednesday")
elif(n==5):
    print("Thursday")
elif(n==6):
    print("Friday")
elif(n==7):
    print("Saturday")
else:
    print("Enter valid number of day")