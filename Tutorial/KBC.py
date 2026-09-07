print("WELCOME TO KOUN BANEGA CORERPATI\n\n")
questions=[{"question":"which planet known as red planet?",
           "option":["1.earth","2.jupiter","3.sun","4.mars"],
           "answer":4
            },
    {"question":"what is the capital of india?",
    "option":["1.chenni","2.delhi","3.mumbai","4.nagput"],
    "answer":2
     },
    {"question":"how many colours are there rainbow?",
    "option":[1.5,2.6,3.7,4.8],
    "answer":3
     },
    {"question":"what is the capital of maharashtra?",
    "option":["1.pune","2.nashik","3.nagpur","4.mumbai"],
    "answer":3
     },
    {"question":"which planet closet to sun?",
    "option":["1.earth","2.mars","3.venus","4.mercury"],
    "answer":4
     },
    {"question":"what does cows drink?",
    "option":["1.water","2.tea","3.juice","4.milk"],
    "answer":1
     },
    {"question":"which bird is the national bird of india?",
    "option":["1.sparrow","2.peacock","3.parrot","4.eagle"],
    "answer":2
     },
    {"question":"what is 5*5?",
    "option":[1.12,2.45,3.25,4.33],
    "answer":3
     },
    {"question":"which of these is a fruit?",
    "option":["1.potato","2.onion","3.carrot","4.mango"],
    "answer":4
     },
    {"question":"which is a smallest state in india by area?",
    "option":["1.sikkim","2.goa","3.manipur","4.tripura"],
    "answer":2
     },
    {"question":"which of the following is not a programming language?",
    "option":["1.lotus","2.python","3.java","4.html"],
    "answer":1
     },
    {"question":"what is the currency of japan?",
    "option":["1.won","2.yen","3.yuan","4.ringgit"],
    "answer":2
     },
    {"question":"what is the chemical symbol of gold?",
    "option":["1.gd","2.go","3.au","4.ag"],
    "answer":3
     },
    {"question":"in which year did india win its first cricket world cup?",
    "option":[1.1975,2.1983,3.1987,4.1992],
    "answer":2
     },
    {"question":"how many days are there in leap year?",
    "option":[1.364,2.366,3.365,4.367],
    "answer":2
    }
]
levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000]
prize=0
for i,q in enumerate(questions):
    print(f"Question for Rs. {levels[i]}")
    print(q["question"])
    for opt in q["option"]:
        print(opt)
    answer=int(input("enter you answer(1-4)or 0 for quit: "))
    if answer==0:
        prize=levels[i-1]
        print("you have quit game")
        break
    if answer==q["answer"]:
            print(f"your answer is correct,you have won {levels[i]}")
    else:
        print(f"your answer is wrong,\nCorrect answer was {q["answer"]}")
        break
    
    if(i==4):
        prize=10000
    elif(i==9):
        prize=320000
    elif(i==14):
        prize=10000000
    else:
        print("congratulation!")
