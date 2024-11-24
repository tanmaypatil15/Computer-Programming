with open("sample.txt",'r') as f:
    print("Before reversal: ",f.read())
f = open("sample.txt", "r")
s = f.read()
f.close()
f = open("reverse.txt", "w+")
f.write(s[::-1])
f.close()
with open("reverse.txt",'r') as f:
    print("After reverse:",f.read())
