from random import *

lotto = []
for i in range(0,7):
    lotto.append(choice(range(1, 45+1)))

score = 0
numbers = []
for i in range(0,7):
    a = int(input("숫자를 입력해주세요 >> "))
    numbers.append(a)
    if lotto[i]==numbers[i] :
        score += 1

if score == 7 :
    print("당첨을 축하합니다.")
else :
    print("꽝!", score, "개 맞추셨습니다.")