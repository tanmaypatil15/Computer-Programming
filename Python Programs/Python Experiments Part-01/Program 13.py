# Program to display the Fibonacci sequence up to n-th
#term where n is provided by the user

nterms = int(input("Enter The Value :"))
n1 = 0
n2 = 1
count = 0

# check if the number of terms is valid
if nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence upto",nterms,":")
   while count < nterms:
       print(n1,end=' , ')
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
