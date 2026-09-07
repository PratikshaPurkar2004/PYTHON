"""n=int(input("enter the no: "))
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
for i in range(n):
    print(fibonacci(i))


def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
n=int(input("enter the no: "))
print(fibonacci(n))"""

def fibonacci(n):
    fib=[0]*(n)
    fib[0]=0
    fib[1]=1
    for i in range(2,n):
        fib[i]=fib[i-1]+fib[i-2]
    return fib
n=int(input("enter the no: "))    
print(fibonacci(n))
    

        
