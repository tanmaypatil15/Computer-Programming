#To Find The Armstrong Numbers.
print("Enter the Number : ")
num =int(input())

order = len(str(num))

# initialize sum
sum = 0

temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** order
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
