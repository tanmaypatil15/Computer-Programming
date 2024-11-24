#Write a python program to implement List, Tuple, Dictionarieshlist=[9,'xyz',3,6,'pqr',9.5]#creat list

hlist=[9,'xyz',3,6,'pqr',9.5]#creat list
print(hlist)
hlist1=['abc',7]  #print list
print(hlist1)
hlist1[1]='hit'
print(hlist1)
print(hlist[2])
print(hlist[-1])
print(hlist+hlist1) #list concatenation
print(hlist[1:5])
print(hlist1*3)     #list repetition
hlist2=[1,2,['ab','dks'],[2.4,7.3],'hi'] #nested list
print(hlist2)
print(len(hlist))
hlist1.append('ACPCE') #List append
print(hlist1)
sublist1=['coa','aoa','graphics'] # List of subjects
sublist2=['maths4','os','python'] #another List of subjects
print(sublist1)
sublist1.extend(sublist2)
print(sublist1) #extended list
sublist1.insert(2,'java')
print("list after inserting",sublist1)
sublist2.remove('maths4')
print("list after removing",sublist2)
l=[1,1,1,2,2,2,2,2,3,3]
print(l)
print("in above list 2 occurs = ",l.count(2)) #count occurences of element
print("first elemnet of above list is",l[0])
print("list consisiting of only 1 is",l[0:3]) #slice operation
print("list consisiting of only 2 is",l[3:7])
list1=[1,2,3,4]
print(list1)
del list1[1]
print("after deletion of 2nd element ",list1)
list1[2]=['p','q','r']
print("after concatanetaion",list1) #concatenation using slice operation
del list1 #deletion of list
l1=[3,2,6,1]
print(l1)
l1.sort()  # sorting of list using sort operation
print("after sorting list is ",l1)
ht=() #empty tuple
print(ht)
ht=(1,2,3) #tuple of integers
print(ht)
ht=('ac',4,5,'pqr') #tuple of mixed values
print(ht)
ht=('ac',(2,3,4),5.6) #nested tuple
print(ht)
ht=8,4,'xyx' #tuple without parenthesis
print(ht)
a,b,c=ht #tuple unpacking
print(a)
print(b)
print(c)
print(" 2nd element", ht[1]) #accesssing element using indexing

tuph=('a','b','c','d','e','f','g')
print("tuph is",tuph)
print(tuph[2])
ntup=('sam',[9,10,11],(7,9,9)) #nested tuple
print("nutup is",ntup)
print(ntup[2][1])
print(ntup[-1]) #Accessing elements using negative indexing
print(tuph[-3])
print("after slicing of tuph",tuph[1:5]) #Accessing elements using slicing
print("elemets begining to second of tuph is",tuph[:-5])
print("element 4th to end is",tuph[3:])
print("elements beg to end is ",tuph[:])
del ntup

dic1={1:"pqr",2:"hit",3:"sam"}
print("dic1 is",dic1)
print(type(dic1))
dic2={"fname":"xyz","lname":"abc"}
print("dic 2 is",dic2)
print(dic2.keys())
print("length odf dic 2 is",len(dic2))
print(dic2.values())
dic3={"fname":["sql","rr"],"lname":"qwr"}
print("dic 3 is",dic3)
print("keys of dic3 is",dic3.keys())
print(dic3.values())
print(dic3["fname"])
print(dic3["fname"].append("sun"))
print("after appending dic 3 is ",dic3)
print(dic3.values())
print(dic3)
print(dic3["fname"].insert(1,"java"))
print(dic3)
dic3.update({"no":987654321})
print(dic3)
print(dic3.update({"no":[98765,76543,1234]}))
print(dic3)
print(dic3["no"].insert(8,6666))
print(dic3)
print(dic3.update({"lname":"wdp"}))
print(dic3) 
