# Write a program to find the largest number from the given three numbers. 

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if(a>b and a>c):
    print(a)
elif(b>a and b>c):
    print(b)
else:
    print(c)