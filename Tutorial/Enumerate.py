#Enumerate:get the value and index when looping through a list
"""fruits=["apple","banana","orange","watermelon"]
for index,fruit in enumerate(fruits,start=1):
    print(index,fruit)


i=0
for fruit in fruits:
    print(i,fruit)
    i+=1"""


nums=[1,2,3]
squares=[x**2 for x in nums]
print(squares)
