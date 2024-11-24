#To Print The Reverse Of The Numbers.
print("Reverse of the Number")
reverse = " "
num = input("Enter the Numeric Values :")
for i in range(len(num), 0, -1):
    reverse += num[i-1]
print("Reversed Numbers are ",int(reverse))
