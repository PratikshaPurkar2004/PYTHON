import random
questions=[["which planet known as red planet?","earth","jupiter","sun","mars",4],
    ["what is the capital of india?","chenni","delhi","mumbai","nagput",2],
    ["how many colours are there rainbow?",5,6,7,8,3],
    ["what is the capital of maharashtra?","pune","nashik","nagpur","mumbai",4],
    ["which planet closet to sun?","earth","mars","venus","mercury",4],
    ["what does cows drink?","water","tea","juice","milk",1],
    ["which bird is the national bird of india?","sparrow","peacock","parrot","eagle",2],
    ["what is 5*5?",12,45,25,33,3],
    ["which of these is a fruit?","potato","onion","carrot","mango",4],
    ["which is a smallest state in india by area?","sikkim","goa","manipur","tripura",2],
    ["which of the following is not a programming language?","lotus","python","java","html",1],
    ["what is the currency of japan?","won","yen","yuan","ringgit",2],
    ["what is the chemical symbol of gold?","gd","go","au","ag",3],
    ["in which year did india win its first cricket world cup?",1975,1983,1987,1992,2],
    ["how many days are there in leap year?",364,366,365,367,2]
]
levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000]
prize=0
for i in range(0,len(questions)):
    question=questions[i]
    print(f"\nQuestion for Rs. {levels[i]}")
    print(f"A.{question[1]}             B.{question[2]}")
    print(f"C.{question[3]}             D.{question[4]}")
    reply=int(input("choose your answer(1,2,3,4)or 0 to quite : "))
    if reply==0:
        prize=levels[i-1]
        break
    if(reply==question[-1]):
        print(f"correct answer,you have won Rs.{levels[i]}")
    else:
        print("wrong answer,game over!")
        break
    if(i==4):
        prize=10000
    elif(i==9):
        prize=320000
    elif(i==14):
        prize=10000000
    else:
        print("congratulation!")
