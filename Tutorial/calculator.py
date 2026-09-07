"""num1=float(input("enter the first no: "))
op=input("enter the operator(+,-,*,/): ")
num2=float(input("enter the second no: "))
if op=='+':
    print("result",num1+num2)
elif op=='-':
     print("result",num1-num2)
elif op=='*':
     print("result",num1*num2)
elif op=='/':
     if num2!=0:
         print("result",num1/num2)
     else:
         print("error")
else:
     print("invalid choice")

num1=float(input("enter the number"))
if num1%2==0:
     print("even number")
elif num==0:
    print("number is zero")
else:
     print("odd number")
rows = int(input("Enter the number of rows: "))

# Generate the pattern
for i in range(1, rows + 1):
    print("* " * i)

import time
timestamp=time.strftime("%H:%M:%S")
print(timestamp)
timestamp=time.strftime("%H")
print(timestamp)
timestamp=time.strftime("%M")
print(timestamp)
timestamp=time.strftime("%S")
print(timestamp)

import datetime
now=datetime.datetime.now()
print(now)

import time
t=time.strftime("%H:%M:%S")
print(t)

import datetime
t=time.strftime("%Y-%m-%d")
print(t)


for i in range(1,11):
    print(2*i)"""


import time
t=time.strftime("%H:%M:%S")
print(t)
hour=int(input("enter the hour: "))
print(hour)

if(hour>=0 and hour<12):
    print("good morning")
elif(hour>=12 and hour<17):
    print("good afternoon")
else:
    print("good eveing")
