''' Write a program to convert Celsius to Fahrenheit and vice versa.  
(Hint- F ((9*C/5)+32). '''

c = float(input("Enter Celsius: "))
f = (9 * c / 5) + 32
print("Fahrenheit:", f)

f = float(input("Enter Fahrenheit: "))
c = (f - 32) * 5 / 9
print("Celsius:", c)