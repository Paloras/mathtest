import random
import time
import math
import json

name = input("이름을 입력해주세요:")
fail = 0
score = 0
callist=["^","*","-","+","/","√"]
timee=[]
timing=0
timescore=0
for i in range(1,11):
    if fail>10:
        print("너무많은 실패를 하였습니다.")
        break
    num1 = random.randint(-100,100)
    cal1 = random.choice(callist)
    num2 = random.randint(-100,100)
    if num1 ==0:
        num1=1
    if num2==0:
        num2=1
    if cal1 == "^":
        if num1>10 or num1<0:
            num1=10
        if num2>10 or num2<0:
            num2=10
        answer= num1**num2
        start= time.time()+13
        while True:
            if fail>10:
                print("너무많은 실패를 하였습니다.")
                break
            x=input(f"{num1}^{num2}의 값은?")
            try:
                if int(x)==answer:
                    break
            except ValueError:
                pass
            fail+=1
        end = time.time()
        timing =end-start
        timee.append(timing)
        print(f"걸린시간 : {end-start}초")
    elif cal1 == "*":
        answer= num1*num2
        start= time.time()+8
        while True:
            if fail>10:
                print("너무많은 실패를 하였습니다.")
                break
            x=input(f"{num1}X{num2}의 값은?")
            try:
                if int(x)==answer:
                    break
            except ValueError:
                pass
            fail+=1
        end = time.time()
        timing =end-start
        timee.append(timing)
        print(f"걸린시간 : {end-start}초")
    elif cal1 == "/":
        answer= num1/num2
        start= time.time()
        while True:
            if fail>10:
                print("너무많은 실패를 하였습니다.")
                break
            x=input(f"{num1}÷{num2}의 값은?")
            try:
                if int(x)==round(answer):
                    break
            except ValueError:
                pass
            fail+=1
        end = time.time()
        timing =end-start
        timee.append(timing)
        print(f"걸린시간 : {end-start}초")
    elif cal1 == "+":
        answer= num1+num2
        start= time.time()
        while True:
            if fail>10:
                print("너무많은 실패를 하였습니다.")
                break
            x=input(f"{num1}+{num2}의 값은?")
            try:
                if int(x)==answer:
                    break
            except ValueError:
                pass
            fail+=1
        end = time.time()
        timing =end-start
        timee.append(timing)
        print(f"걸린시간 : {end-start}초")
    elif cal1 == "-":
        answer= num1-num2
        start= time.time()
        while True:
            if fail>10:
                print("너무많은 실패를 하였습니다.")
                break
            x=input(f"{num1}-{num2}의 값은?")
            try:
                if int(x)==answer:
                    break
            except ValueError:
                pass
            fail+=1
        end = time.time()
        timing =end-start
        timee.append(timing)
        print(f"걸린시간 : {end-start}초")
    elif cal1 == "√":
        if num1<0:
            num1=100
        answer= math.sqrt(num1)
        start= time.time()
        while True:
            if fail>10:
                print("너무많은 실패를 하였습니다.")
                break
            x=input(f"√{num1}의 값은?")
            try:
                if int(x)==round(answer):
                    break
            except ValueError:
                pass
            fail+=1
        end = time.time()
        print(f"걸린시간 : {end-start}초")
        timing =end-start
        timee.append(timing)
    if timing < 5:
        score +=100
    elif timing >=5 and timing <12:
        score+=80
    elif timing >=12 and timing<16:
        score+=50
    elif timing >=16 and timing<30:
        score+=20
    elif timing >=30 and timing<50:
        score+=10
    elif timing >=50:
        score-=10
times=0
for i in timee:
    times+=i
timescore = times/10
if fail < 10:    
    if timescore<3:
        score+=1000
    elif timescore>=3 and timescore<5:
        score+=800
    elif timescore>=5 and timescore<10:
        score+=600
    elif timescore>=10 and timescore<20:
        score+=350
    elif timescore>=20 and timescore<40:
        score+=100
    else:
        score-=100
    with open(f'./rank.json', 'r', encoding="utf-8") as f:
        rank = json.load(f)
    code = oct(random.randint(0,10000000000))
    rank[code]={}
    rank[code]["name"]=name
    rank[code]["score"]=score
    rank[code]["timescore"]=timescore
    with open(f'./rank.json', 'w') as s:
        json.dump(rank, s, indent=4)
    print(f"총점: {score}점/2000점\n평균 통과시간: {timescore}초\n")
else:
    print(f"총점: 0점/2000점\n평균 통과시간: {timescore}초\n")
rank = []
r = ""
xad=1
with open(f'./rank.json', 'r', encoding="utf-8") as f:
    money = json.load(f)
for i in money:
    rank.append([str(money[i]["name"]), int(money[i]['score']), float(money[i]['timescore'])])
rank = list(reversed(sorted(rank, key=lambda x:x[1])))
a=1
for i in rank:
    if a > 10:
        break
    r+=f'{a}위 {i[0]}. {i[1]}점 평균통과시간:{i[2]}초\n'
    a += 1
for i in rank:
    if name in r:
        break
    else:
        if i[0]==name:
            r+=f'{xad}위 {i[0]}. {i[1]}점 평균통과시간:{i[2]}초\n'
        else:
            xad +=1
print(r)
time.sleep(1000)