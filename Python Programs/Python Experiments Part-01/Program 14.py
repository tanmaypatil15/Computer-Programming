num1 = int(input("Enter First Number  : "))
num2 = int(input("Enter Second Number : "))

print("Enter which operation would you like to perform?")
ch = input("Enter any of these char for specific operation +,-,*,/: ")
result = 0

if ch == '+':
    print("Addition :")
    result = num1 + num2
elif ch == '-':
    print("Subtraction :")
    result = num1 - num2
elif ch == '*':
    print("Multiplication :")
    result = num1 * num2
elif ch == '/':
    print("Division :")
    result = num1 / num2
else:
    print("Input character is not recognized!")

print(num1, ch , num2, ":", result)
