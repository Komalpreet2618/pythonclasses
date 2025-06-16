#question1 
l1=[4,8,16,20,32,2,12,13,17,21]
print(l1)

print("----------")

#question2
l1=[1,10,100,3,6,8]
l1.insert(2,59)
l1.append(5)
print(l1)
print(len(l1))

print("----------")

#question3
l=[2,4,6,8,10,12,14,16,18,20]
print(l[0::2])

print("----------")

#question4
l=["Gaurav",12,23,33.33,"Sharma",True]
for i in l:
    if type(i) == str:
        print(i)

print("----------")

#question5
sum=0
for i in l:
    if type(i) == int or type(i)==float:
        sum += i
print(sum)

print("----------")

#question6
f=['raman','seerat','komal','inder','hargun']
a=input("enter another friend's name:")
f.append(a)
print(f)
b=input("Enter your most important friend's name to add: ")
c=int(input("Enter the index to add the name: "))
f.insert(c,b)
print(f)
