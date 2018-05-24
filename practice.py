# 문제1. 키보드로 정수 수치를 입력 받아 그것이 3의 배수인지 판단하세요
"""
실행 결과:

수를 입력하세요: hello
정수가 아닙니다.

Process finished with exit code 0

수를 입력하세요: 10
3의 배수가 아닙니다.

Process finished with exit code 0

수를 입력하세요: 129
3의 배수 입니다.

Process finished with exit code 0
"""
num = input('수를 입력하세요: ')
if num.isdigit():
    num = int(num)
    if num%3 != 0:
        print('3의 배수가 아닙니다.')
    else:
        print('3의 배수 입니다.')
else:
    print('정수가 아닙니다.')

# 문제2. 키보드로 정수 수치를 입력 받아 짝수인지 홀수 인지 판별하는 코드를 작성하세요.
"""
실행 결과: 

수를 입력하세요: 5
홀수

Process finished with exit code 0

수를 입력하세요: 10
짝수

Process finished with exit code 0
"""
num = input('수를 입력하세요: ')
if num.isdigit():
    num = int(num)
    if num%2 != 0:
        print('홀수입니다.')
    else:
        print('짝수입니다.')
else:
    print('정수가 아닙니다.')

# 문제3. 파이썬 경로명 s = '/usr/local/bin/python' 에서 각각의 디렉토리 경로명을 분리하여 출력하세요.
"""
실행 결과: 
‘usr’, ‘local’, ‘bin’, ‘python’

또, 디렉토리 경로명과 파일명을 분리하여 출력하세요.

실행 결과: 
‘/usr/local/‘bin’, ‘python’
"""
s = '/usr/local/bin/python'
print(s.strip('/').split('/'))
print(s.rsplit('/', 1))

# 문제4. 다음과 같은 텍스트에서 모든 태그를 제외한 텍스트만 출력하세요.
s = """
<html>
    <body style='background-color:#ffff'>
        <h4>Click</h4>
        <a href='http://www.python.org'>Here</a>
        <p>
        	To connect to the most powerful tools in the world.
        </p>
    </body>
</html>"""
"""
실행 결과: 
Click
Here
    To connect to the most powerful tools  in the world.
"""
start = 2
end = 0
while True:
    end = s.find('>', end)
    start = s.find('<', start)
    print(str(end) + ':' + str(start))
    if start == -1 or end == -1:
        break
    start += 1
    end += 1
    s += s[end:start-1]
print(s)


# 문제6. 주어진 리스트 데이터를 이용하여 3의 배수의 개수와 배수의 합을 구하여 출력형태와 같이 출력하세요.
"""
실행 결과
주어진 리스트에서 3의 배수의 개수=> 6
주어진 리스트에서 3의 배수의 합=> 150
"""
l = [1, 3, 5, 7, 9, 11, 13, 15]
count = 0
sum = 0
for i in l:
    if i%3 == 0:
        count += 1
        sum += i

print('주어진 리스트에서 3의 배수의 개수=> '+ str(count))
print('주어진 리스트에서 3의 배수의 합=> ' + str(sum))

# 문제7. 키보드에서 정수로 된 돈의 액수를 입력 받아 오만 원권, 만원 권, 오천 원권,
# 천원 권, 500원짜리 동전, 100원짜리 동전, 50원짜리 동전, 10원짜리 동전, 1원짜리 동전
# 각 몇 개로 변환 되는지 작성하시오.
"""
실행결과
금액: 67879

50000원 : 1개
10000원 : 1개
5000원: 1개
1000원: 2개
500원: 1개
100원: 3개
50원:1개
10원:2개
5원:1개
1원:4개
"""
change = [50000, 10000, 5000, 1000, 500, 100, 50, 10, 5, 1]
result = []
money = input('금액: ')
money = int(money)
for ch in change:
    result.append(int(money / ch))
    money = money % ch

for i in range(0, len(change)):
    print(str(change[i]) + "원: " + str(result[i]))


#문제 8. 키보드에서 5개의 정수를 입력 받아 리스트에 저장하고 평균을 구하는 프로그램을 작성하시오
"""
실행결과
> 1
> 2
> 3
> 4
> 5
평균: 3.0
"""
list = []
count = 5
sum = 0
while count > 0:
    count -= 1
    num = int(input("정수를 입력하세요: "))
    list.append(num)
    sum += num

print('평균: '+ str(sum/5))

#문제9. 문자열을 입력 받아, 해당 문자열을 문자 순서를 뒤집어서 반환하는 함수 reverse(s)을 작성하세요.
"""
실행결과
입력> Java Programming!
결과> !gnimmargorP avaJ
"""
def reverse(s):
    string = ''
    for i in range(len(s)-1, -1, -1):
        string += s[i]
    print(string)
    return string

string = input("입력> ")
reverse(string)


# 문제12
# 반복문을 이용하여 369게임에서 박수를 쳐야 하는 경우의 수를 순서대로 화면에
# 출력해보세요. 1부터 99까지만 실행하세요.
"""
실행 결과: 
3 짝
6 짝
9 짝
13 짝
16 짝
19 짝
23 짝
26 짝
29 짝
30 짝
31 짝
32 짝
33 짝짝
34 짝
35 짝
36 짝짝
37 짝
"""
count = int(input("반복 횟수> "))
for i in range(1, count+1):
    index = len(str(i))
    num = int(str(i)[index-1])
    if num == 3 or num == 6 or num == 9:
        print(i)


# 문제13. 숫자를 입력 받아서 아래와 같은 실행결과가 나타나도록 코드를 완성하세요.
"""
a. 입력 받은 숫자가 홀수인 경우에는, 0 부터 입력 값까지 홀수의 합을 출력합니다.
- 예제 : 입력이 7 이면 16을 출력 ( 1 + 3 + 5 + 7 = 16 ) 
b. 입력 받은 숫자가 짝수인 경우에는, 0 부터 입력 값까지 짝수의 합을 출력합니다.
- 예제 : 입력이 10 이면 30을 출력 ( 2 + 4 + 6 + 8 + 10 = 30 )
"""
"""
실행 결과: 

숫자를 입력하세요: 7
결과 값 : 16

숫자를 입력하세요: 10
결과 값 : 30

숫자를 입력하세요: 11
결과 값 : 36
"""
num = int(input('숫자를 입력하세요: '))
if num % 2 == 0:
    cnt = int(num / 2)
    sum = ((1+num)*cnt + cnt)/2
    print(int(sum))
else:
    cnt = int((num+1) / 2)
    sum = ((1+num+1)*cnt - cnt)/2
    print(int(sum))

# 문제14
# 숨겨진 카드의 수를 맞추는 게임입니다. 1-100까지의 임의의 수를 가진 카드를 한 장 숨기고
# 이 카드의 수를 맞추는 게임입니다. 아래의 화면과 같이 카드 속의 수가 57인 경우를 보면 수를
# 맞추는 사람이 40이라고 입력하면 "더 높게", 다시 75이라고 입력하면 "더 낮게" 라는 식으로 범위를
# 좁혀가며 수를 맞추고 있습니다. 게임을 반복하기 위해 y/n이라고 묻고 n인 경우 종료됩니다.
"""
수를 결정하였습니다. 맞추어 보세요
1-100
1>>40
더 높게
2>>50
더 높게
50-100
3>>75
50-75
4>>64
더 낮게
50-64
5>>55
더 높게
55-64
6>>60
더 낮게
55-60
7>>57
맞았습니다.
다시 하시겠습니까(y/n)>>n
"""
import random
repeat = 'y'
while repeat == 'y':
    i = 1
    num = random.randint(1, 100)
    print('수를 결정하였습니다. 맞추어 보세요')
    while True:
        select = int(input(str(i)+'>>'))
        i += 1
        if select == num:
            repeat = input('맞았습니다. 다시 하시겠습니까(y/n)>> ')
            break
        elif select < num:
            print('더 높게')
        else:
            print('더 낮게')