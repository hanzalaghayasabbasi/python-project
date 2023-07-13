#Factorial and Fabonnaci

#Factorial
n=int(input("Enter number to find factorial \t :"))

def funct(n):
  if(n==0 or n==1):
    return 1
  else:
    return n*funct(n-1)
    #Factorial of 5
    # 5*24=120
    # 4*6=24
    # 3*2=6
    # 2*1=2
    # 1*1=1

k=funct(n)
print("Factorial of number is ",n," = ",k)



# Fabonnaci


def recursion(n):
   if n <= 1:
       return n
   else:
       return(recursion(n-1) + recursion(n-2))


nterms=int(input("Enter a number to find fabaconni series \t: "))

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recursion(i))
   





