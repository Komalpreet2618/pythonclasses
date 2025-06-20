#Question1
t1=(6,9,0,3,'python',3,17,'python',55,'true','false',6)
print("Original tuple:", t1)
t1=set(t1) 
t1=tuple(t1)     
print("After removing duplicates:", t1)

print("-------------------------------------------")

#Question2
l1=[[11,12,13],[14,15,16],[17,18,19]]
l1=[j for i in l1 for j in i]
print("Flattened list:", l1)

print("-------------------------------------------")

#Question3
t2=(7,56,34,23,16,48,90,88)
t2=sorted(t2)
print("Min=", t2[0])
print("Max=", t2[-1])

print("-------------------------------------------")

#Question4
l2=[(i,i**3) for i in range(1,6)]
print("Required list", l2)