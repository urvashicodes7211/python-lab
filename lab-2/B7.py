'''Write a program to find the largest number from the given three numbers using the 
ternary operator. '''

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

print(a if a>b and a>c else b if b>a and b>c else c)