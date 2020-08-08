# Python program to display the Fibonacci sequence.
xterms = int(input("Enter the number of terms to be printed : "))
# first two terms.
x1, x2 = 0, 1
count = 0
# check if the number of terms is valid.
if xterms <= 0:
   print("Invalid number \nPlease enter a positive integer")
elif xterms == 1:
   print("Fibonacci sequence upto",xterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < xterms:
       print(x1)
       xth = x1 + x2
       # update values
       x1 = x2
       x2 = xth
       count += 1
print("DONE !")
print("THANK YOU !")

