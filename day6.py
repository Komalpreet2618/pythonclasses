#list comprehension

#question1
l1=['coder','roots','python','DS','june','defender','may']
s=[i for i in l1 if len(i)<4]
print(s)

print("--------")

#question2
l2=['even' if i%2==0 else 'odd' for i in range(20)]
print(l2)

print("--------")

#question3
l3=[i for i in range(1,1000)if i%7==0]
print (l3)

print("--------")

#question4
l4=['I am Komal','I am doing Btech']
spaces=0
for i in l4:
    spaces += i.count(' ')
print("Total number of spaces in the list:",spaces)

print("--------")

#question5
a=[1,2,3,4]
b=[2,3,4,5]
common=[i for i in a for j in b if i==j]
print(common)
