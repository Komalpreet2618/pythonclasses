#string task

#question 1
str1=input("enter st1:")
print (len(str1))
if len(str1)<2:
    print("not a valid string")
else: 
    print ("new string:",str1[0:2]+str1[len(str1)-2:len(str1)+1])

#question 3
str1=input("Enter str1:")
if len(str1)<3:
    print(str1)
elif str1.endswith("ing"):
    print(str1+"ly")
else:
  print(str1+"ing")

#question 2
str1=input("Enter str1:")
str2=input("Enter str2:")
print("concatenated string:",str2[0:1]+str1[1:len(str1)+1],str1[0:1]+str2[1:len(str2)+1])
print("program complete")
