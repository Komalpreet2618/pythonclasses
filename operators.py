#question 1
name= input("name:")
Class =input("class:")
section = input ("section:")
COA= int (input("Marks in COA:"))
DM= int (input("Marks in DM:"))
DAA= int (input("Marks in DAA:"))
UHV= int (input("Marks in UHV:"))
OS= int (input("Marks in OS:"))
total= COA+DM+DAA+UHV+OS
percentage= total/5
print ("percentage of student is:",percentage)

#question 2
a= int(input("a:"))
b= int(input("b:"))
c= int(input("c:"))
sum= a+b+c
print ("sum:",sum)

#question 3
a= int(input("a:"))
square= a*a
print("square of given number:",square)

#question 4
temp= input("temperature in celsius:")
temp=float(temp)
print(temp)
temp= (temp*9/5)+32
print("temperature in fahrenheit is:",temp)

#question 5
a= int(input("a:"))
b= int(input("b:"))
c= a//b
print ("quotient:",c)
d=a%b
print("remainder:",d)
