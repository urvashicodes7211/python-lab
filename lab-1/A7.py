'''Write a program to take 4 subjects' marks from the user and calculate total  
marks & Percentage.'''

m1 = float(input ("Enter mark 1: "))
m2 = float(input ("Enter mark 2: "))
m3 = float(input ("Enter mark 3: "))
m4 = float(input ("Enter mark 4: "))

totalMark = m1+m2+m3+m4

print("total Mark: ",totalMark)
print("Percentage : ",((totalMark)*100)/400)