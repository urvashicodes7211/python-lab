'''Write a program to calculate electricity bill based on the following criteria.  
Take the units from the user.  
i. First 1 to 50 units - Rs. 2/unit  
ii. Next 50 to 100 units - Rs. 3.5/unit  
iii. Next 100 to 200 units - Rs. 5.5/unit  
iv. above 200 units - Rs. 8/unit. '''

units = float(input("Enter units : "))
if(units <= 50):
    print("bill : ",units*2)
elif(units <= 100):
    print("bill : ",(units-50)*3.5 + 50*2)
elif(units <= 200):
    print("bill : ",(units-100)*5.5 + 50*3.5 + 50*2)
else:
    print("bill : ",(units-200)*8 + 100*5.5 + 50*3.5 + 50*2)