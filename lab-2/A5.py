'''Write a program to perform addition, subtraction, multiplication, and division of two 
numbers based on user input.'''

print("1 . addition")
print("2 . subtraction")
print("3 . multiplication")
print("4 . division")
n = int(input("Enter number of opration: "))
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

if(n == 1):
    print(a+b)
elif(n == 2):
    print(a-b)
elif(n == 3):
    print(a*b)
elif(n == 4):
    if b != 0:
        print("Division =", a / b)
    else:
        print("Division by zero is not possible.")
else:
    print("Enter valid number of opration : ")