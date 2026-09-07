"""def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return factorial(n-1)*n
n=int(input("enter the no: "))
print(factorial(n))

def fibonacci(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
n=int(input("enter the no: "))
for i in range(0,n):
    print(fibonacci(i))"""

def is_prime(n):
    if n<=1:
        is_prime=False
    for i in range(2,n):
        if(n%i==0):
            break
    print("no is prime",n)
print(is_prime(6))

