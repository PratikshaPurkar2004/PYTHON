"""num=int(input("enter the no: "))
if num<=1:
    print("no is not prime")
else:
    for i in range(2,num):
        if(num%i==0):
            print("no is not prime")
            break
    print("no is prime")"""

        
"""def is_prime(n):
    if n<=1:
        is_prime=False
    for i in range(2,n):
        if n%i==0:
            break
    print(n,"no is prime")
is_prime(20)"""


        
num=int(input("enter the no: "))
if num>1:
    for i in range(2,num):
        if num%i==0:
            print("not prime")
            break
        else:
            print("prime")
else:
    print("not prime")
