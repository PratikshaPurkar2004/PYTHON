import random
l=input("enter a string: ")
word=l.split(" ")

if len(word)>=3:
    word=word[1:]+word[0]#remove 1st letter and append at last
    print(word)
    random_char=''.join(random.choices("hello",k=3))#append random 3 element at start and end of string
    word=random_char+word+random_char
    print(word)
else:
    word=word[::-1]
    print(word)
if len(word)<3:
    word=word[::-1]
    print(word)
else:
    word=word[3:-3]#remove random 3 character from start and end
    print(word)
    word=word[-1]+word[:-1]#remove last element and append to the beginning
    print(word)
    

     

