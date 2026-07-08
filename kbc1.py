print("Welcome to KBC ")

qutions =[
    ["What is the capital of India?","Mumbai","Delhi","Chennai","Kolkata",2],
    ["Which planet is known as the Red Planet?","Earth","Venus","Mars","Jupiter",3],
    ["Who is known as the Father of Computers?","Charles Babbage","Elon Musk","Bill Gates","Steve Jobs",1],
    ["Which language is used for Python programming?","Binary","English-like syntax","HTML","Java only",2],
    ["How many continents are there in the world?","5","6","7","8",3],
    ["Which company created Python?","Google","Microsoft","Apple","Python Software Foundation",4],
    ["Who wrote the Indian National Anthem?","Mahatma Gandhi","Rabindranath Tagore","APJ Abdul Kalam","Subhash Chandra Bose",2],
    ["Which is the smallest prime number?","0","1","2","3",3],
    ["Which country is famous for the Eiffel Tower?","Italy","France","Germany","Japan",2],
    ["Who discovered gravity?","Einstein","Newton","Tesla","Edison",2]
]

Level =[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,]

for i in range(0,len(qutions)):
    qution = qutions[i]
    print(f"Qution for Rs.{Level[i]}")
    print(qution[0])
    print(f"1.{qution[1]}          2.{qution[2]}")
    print(f"3.{qution[3]}          4.{qution[4]}")  
    replay = int(input("Enter a number between (1 to 4):-"))
    if (replay == qution[5]):
       print(f"the your ans is correct,and you the price pole {Level[i]}")
       i += 1

    elif (replay == 0):
       print("you are plase the butten of quit")
       print(f"the todel amound of win is {Level[i]}")
       break

    else:
       print("the your ans is wrong")
       print(f"the todel amound of win is {Level[i]}")
       break
