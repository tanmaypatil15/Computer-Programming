#WAP for file handling to read the text from first file and write in another file. 
f1=input("Enter file name from which text is to be copied: ")
f2=input("Enter file name to which text is to be copied: ")
with open(f1, 'r') as f:
    r=f.read()
with open(f2, 'w') as f:
    f.write(r)
print("Text copied in file",f2,"is:")
with open(f2, 'r') as f:
    print(f.read())
