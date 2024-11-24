a=input("Enter 1st String :\n")
b=input("Enter 2nd String :\n")


print(set(a))
c=set(a)
print(set(b))
d=set(b)

print("Interaction of 1st and 2nd ",c.intersection(d))

print("Difference of 2 Set",c.difference(d))

print("Union of 2 Sets ",c.union(d))

print("Symmetric Difference of 2 Sets ",c.symmetric_difference(d))

