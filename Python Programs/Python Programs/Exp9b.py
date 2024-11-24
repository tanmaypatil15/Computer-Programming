#WAP to append data to the existing file and then display the data in the file.
f1=input("Enter the name of the file from which data is to be appended.: ")
f2=input("Enter the name of the file to which data is to be appended.: ")
with open(f1, 'r') as f:
    a=f.read()
with open(f2, 'r') as f:
    print("Before appending:\n",f.read())    
with open(f2, 'a') as f:
    f.write(a)
with open(f2, 'r') as f:
    print("After appending:\n",f.read())    
