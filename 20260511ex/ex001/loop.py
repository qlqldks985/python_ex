# 반복문(for문 & while문)
# 파이썬에 사용하는 반복문은 For 문과 while문이 있습니다.
# for문: ~ 하는 동안 ==> 회수에 의한 반복
'''
for 변수 in 범위: 
    실행구문
'''

# 1~10까지의 정수를 출력(1,3,5,7,9) 1~10까지 라는 경우에선 10이 아닌 11까지 작성해준다.
# range : 범위를 지정하는 함수값이다.
# 1~ n까지의 정수 range(1, (n+1), 1) - 시작값, 끝값, 단계 (**)
# for num in range(1, 11, 1):
#     print(f'{num} : hello')
#     print(f'hello')


# for num in range(0, 11 ,1):
#     print(f'num: {num}')
# # 0부터 10까지의 정수를 출력 # range( ) 간략화 - 단계가 1인 경우 단계를 생략할 수 있다.
# for num in range(0, 11):
#     print(f'num: {num}')
# # range( ) 간략화 - 단계가 생략되고 시작이 0이면 시작도 생략 가능하다.
# for num in range(11):       # == range(0, 11, 1)
#     print(f'num: {num}')

# quiz) 2~8사이의 짝수 출력하기

# for num in range(2, 9, 2):
#     print(f'num: {num}')

# for num in range (1, 16):
#     if (num <= 8) and (num % 2 == 0):
#             print(f'num: {num}')

# while문 ㅣ ~하는 동안 ==> 조건에 의한 반복
# for in : for ~ in 키워드 / i - item / range (1,11,1) - iterable(반복 가능한 객체) / : - 클론 / print(i) - 실행문

# 사용자가 입력한 횟수만큼 '메일 발송!' 문자열 출력하기
# num = int(input('횟수를 입력하세요: '))
# for num in range(num):
#     print(f'{num}: 메일 발송!')

# 1~10 사이의 정수를 출력하되, 정수가 3의 배수이면 '3의 배수!' 출력하기
# for num in range(1, 11):
#     if num % 3 == 0:
#         print(f'{num}: 3의 배수!')
#     else:
#         print(num)

# 사용자가 원하는 구구단을 입력하면 해당 구구단을 출력하자!
# userInputData = int(input('원하는 구구단을 입력하세요.'))
# for num in range(1,11):
#     resultStr = (f'{userInputData} * {num} = {userInputData*num}')
#     print(resultStr)

# 1~10까지 정수의 합 출력하기
# userInputInteger = int(input('정수 입력: '))

# sum = -
# for i in range(1, userInputInteger + 1):
#     sum += i
#     print(f"1부터 {userInputInteger}까지의 합 :{sum}")

# for문을 이용해서 1~100까지 정수 중에서
# 3과 7의 공배수와 최소공배수를 출력하세요.

# first = True
# for i in range(1, 101):
#     if i % 3 == 0 and i % 7 == 0 and first == True:
#         print(f'{i}는 3과 7의 최소공배수입니다.')
#         first = False
#     elif i % 3 == 0 and i % 7 == 0 :
#         print(f'{i}는 3과 7의 공배수입니다.')

# minNum = 0

# for num in range(1,101):
#     if num % 3 == 0 and num % 7 == 0:
#         print(f'3과 7의 공배수: {num}')
#         if minNum == 0: minNum = num
    
# print(f'3과 7의 최소공배수: {minNum}')

# while문 ㅣ ~하는 동안 ==> 조건에 의한 반복

# range 함수란
# 문자열을 이용한 for문(*****)
'''
지금까지 이터러블에 range() 함수를 이용한 예를 살펴봤습니다.
그런데 이터러블에는 다음과 같이 문자열도 이용할 수 있습니다.
'''

# for ch in 'Hello':
#     print(f'ch: {ch}')

# 50보다 작은 7의 배수를 출력하는 프로그램을 만드시오.
# for num in range(1, 51):
#     if num % 7 ==0:
#         print(f'num : {num}')

# num = 1
# while num < 11:
#     print(f'num: {num}')        # 여기까지만 적어놓으면 무한루프에 빠지게 된다. 그래서 num += 1을 해줘야 한다. 
#     num += 1                    # num 값에 1을 더한 후 그 결과를 다시 num에 저장

# 1부터 30까지의 정수 중 홀수와 짝수를 구분하여 출력하기
# for num in range(1, 31):

# num = 1
# while num < 31:
#     if num % 2 == 0 and num > 0:
#         print(f'{num} : 짝수')
#     else:
#         print(f'{num} : 홀수')
#     num += 1

# 구구단 3단 출력하기 by While문

# num = 3
# while num < 4:
#     for i in range(1, 10):
#         print(f'{num} * {i} = {num*i}')
#     num += 1
# -----------------------------------------------------------------------------
# timesTables = int(input('구구단 숫자를 입력하세요.'))
# num = 1
# while num < 10:
#     print(f'{timesTables} x {num} = {timesTables * num}')
#     num += 1

# 구구단 전체(2단 ~ 9단) 출력하기
# num = 1

# while num < 10:

#     num2 = 1
#     str = ''
#     while num2 < 10:
#         str += f'{num2} x {num} = {num2 * num} \t'
#         num2 += 1
 
#     print(str)
#     num += 1

# 역순 구구단(9단 ~ 2단) 출력하기
# num = 9
# while num > 1:
#     num2 = 1
#     while num2 < 10:
#         print(f'{num} x {num2} = {num * num2}', end = " ")
#         num2 += 1
#     print()
#     num -= 1

# while문과 if문을 이용해서 0~100까지 정수 중 3과 8의 공배수와 최소공배수 출력하기
# num = 1         # 반복문의 시작(초기값)
# minNum = 0     # 최소공배수 저장할 변수

# while num <= 100:

#     if num % 3 == 0 and num % 8 == 0:
#         if minNum == 0:
#             minNum = num  # 24 저장
#             print(f'3과 8의 최소공배수: {minNum}')  # 첫 번째 공배수는 최소공배수로만 출력
#         else:
#             print(f'3과 8의 공배수: {num}')  # 나머지 공배수 출력
            
#     num += 1

# 현재 온도는 30.0도이다.
# 에어컨 온도 설정을 위해서 '희망 온도'를 입력한다.
# 에어컨의 냉방 기능이 동작하면 온도를 체크할 때마다 0.1도씩 내려간다.
# 현재 온도가 희망 온도에 도달하면 에어컨의 냉방 기능이 종료된다.
# currentTemp = 30.0
# hopeTemp = float(input('희망 온도 입력: '))

# while hopeTemp < currentTemp:
#     print(f'현재 온도: {currentTemp:.1f}도')
#     currentTemp -= 0.1

# print(f'희망 온도에 도달했습니다. 냉방 기능 종료!')

# 반복문 내 실행 제어( break, continue) # break : 반복문을 완전히 종료시키는 제어문 / continue : 반복문 내에서 continue를 만나면 그 이후의 코드는 실행하지 않고 다시 반복문의 처음으로 돌아간다.
# continue를 이용해서 1부터 10까지의 정수 중 홀수만 출력하는 프로그램을 만들어 봅시다.

# for num in range(1, 11):
#     if num % 2 == 0:
#         continue
#     print(f'num: {num}')

# count = 1
# for num in range(10):
#     print(f"num: {num}")
#     count += 1
#     if count > 5:
#         break       # 한달 동안 쓸 수 있는 할인쿠폰을 5장으로 제한하는 경우에 break를 이용할 수 있다. 5장 이상이 되면 break로 반복문을 빠져나오게 된다.

# break: 반목분에서 break를 만나면 '실행을 중단하고 반복문을 빠져'나옵니다.
# 1부터 10까지의 정수를 더하되, 결과가 30 이상이 될 때 정수를 찾는 프로그램을 만들어 봅시다.

# num = 1
# sum = 0

# while num < 11:
#     sum += num
#     if sum >= 30:
#         print(f'num: {num}')
#         break
#     num += 1

# print(f'sum: {sum}')    #55

# for~else 키워드
'''
for문에 else 키워드를 사용하는 경우 , else 이하의 구문은 for문의 반복 업무를 모두 완료하고 난 후 실행됩니다.
'''

# 1부터 5까지 정수를 출력하고 반복문이 끝나면 완료 메시지를 출력하자! 는 else 없어도 댐 ㅇㅇ...
# for num in range(1, 6):
#     print(f'num: {num}')
# else:
#     print('완료!')

# pass 키워드
# for num in range(1, 10):
#     pass

# quiz)
'''
삼각형의 넓이 구하기
가로와 세로 길이의 변화에 따른 삼각형의 넓이를 구하는 프로그램을 만들어 보자.
단, 가로 길이는 1부터 2의 배수로 증가하고
세로 길이는 1부터 3의 배수로 증가하며,
삼각형의 넓이가 150보다 크면 프로그램을 종료한다.
'''

# count = 1
# maxArea = 150

# while True:
#     result = ((count * 2) * (count * 3)) / 2
#     if result > 150: break
#     print(f'삼각형의 넓이는: {result}')
#     count += 1

'''
직사각형의 넓이 구하기
가로와 세로 길이의 변화에 따른 직사각형의 넓이를 구하는 프로그램을 만들어 보자.
단, 가로 길이는 2부터 3의 배수로 증가하고
세로 길이는 2부터 4의 배수로 증가하며,
직사각형의 넓이가 200 이상이 되면 프로그램을 종료한다.
'''

# count = 2
# maxArea = 200

# while True:
#     result = (count * 3) * (count * 4)
#     if result >= maxArea: break
#     print(f'직사각형의 넓이는: {result}')
#     count += 1  

'''
별(*) 피라미드를 출력하는 프로그램을 만들어 보자.
첫 번째 줄부터 20번째 줄까지 각 줄에 별(*)의 개수를 증가시키면서 출력한다.
단, 홀수 줄은 ★를 사용하고 짝수 줄은 ☆를 사용한다.
각 줄의 별 개수가 15개 이상이 되면 프로그램을 종료한다.
'''

for num in range(1, 20):
    if num % 2 == 1:
        print('★' * num)
    else:
        print('☆' * num)
    if num >= 15: break