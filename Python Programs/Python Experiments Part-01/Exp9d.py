f1=input("Enter the file of which content is to be copied: ")
f2=input("Enter the file to which content is to be copied: ")
with open(f1, 'r') as a:
    with open(f2, "w") as b:
        for line in a:
            b.write(line)
with open(f2, "r") as b:
    print("Contents copied are:")
    print(b.read())
