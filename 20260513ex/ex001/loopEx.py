#quiz) 369 게임 만들기
'''
친구들까지 많이 하는 369 게임을 만들어봅시다. 1부터 99까지 1씩 증가하면서 숫자에 3, 6, 9가 들어 있을때마다 숫자와 함께 '짝'을 출력합시다.
'''
'''
6 -> 짝
33 -> 짝짝
99 -> 짝짝
'''
# for num in range(1, 100):

#     if num <= 9:                # 1의 단위
#         if num % 3 == 0:
#             # print(f'{num}, 짝!')
#             print(num, ', 짝!', end='')
#         else:
#             print(num, end='')
#     else:                       # 10의 단위 
#         # print(f'{num}')       # 12 > 1, 2 : 16 > 1, 6 : 99 > 9, 9
#         # printStr = str(num)
#         print(num, end='')

#         firstNum = num // 10    # 15 > 15 // 10 -> 1
#         secondNum = num % 10    # 15 > 15 % 10  -> 5, 30 > 0

#         if firstNum % 3 == 0:
#             # print(f'짝!')
#             # printStr += ', 짝!'
#             print(', 짝!', end='')

#         if secondNum % 3 == 0 and secondNum != 0:
#             # print(f'짝!')
#             # printStr += ', 짝!'
#             print(', 짝!', end='')
        
#     print()

# quiz) 열차 교차 시간 알아내기
'''
대역에는 3개 노선의 열차가 오전 9시부터 오후 6시까지 교차 운행한다.
3대의 열차가 교차하는 시간을 구해 열차 충돌 사고를 막으세요.
(단 매일 오전 9시에 대전역에서 모든 열차가 출발한다.)
----------------------------------------------------
A열차: 첫차 오전 9시 ㅣ 마지막차 오후 6시 ㅣ 운행 간격 10분 
B열차: 첫차 오전 9시 ㅣ 마지막차 오후 6시 ㅣ 운행 간격 25분 
C열차: 첫차 오전 9시 ㅣ 마지막차 오후 6시 ㅣ 운행 간격 30분 
----------------------------------------------------
'''

trainA = 10
trainB = 25
trainC = 30

# for n in range(1,541):
#     if n % trainA == 0 and n % trainB == 0 and n % trainC == 0:
#         print('trainA <-> trainB <-> trainC')
#         # print(9+n // 60, end='')        # 시
#         # print('시',end='')
#         # print( n % 60, end='')          # 분
#         # print('분')
#         print(f'{9 + n // 60}시 {'00' if n % 60 == 0 else str(n % 60)}분')

#     elif n % trainA == 0 and n % trainB == 0:
#         print('trainA <-> trainB')
#         # print(9+n // 60, end='')        # 시
#         # print('시',end='')
#         # print( n % 60, end='')          # 분
#         # print('분')
#         print(f'{9 + n // 60}시 {'00' if n % 60 == 0 else str(n % 60)}분')


#     elif n % trainB == 0 and n % trainC == 0:
#         print('trainB <-> trainC')
#         # print(9+n // 60, end='')        # 시
#         # print('시',end='')
#         # print( n % 60, end='')          # 분
#         # print('분')
#         print(f'{9 + n // 60}시 {'00' if n % 60 == 0 else str(n % 60)}분')


#     elif n % trainC == 0 and n % trainA == 0:
#         print('trainC <-> trainA')
#         # print(9+n // 60, end='')        # 시
#         # print('시',end='')
#         # print( n % 60, end='')          # 분
#         # print('분')
          # msgStr = '00' if n % 60 == 0 else str(n % 60)
#         print(f'{9 + n // 60}시 {msgStr}분')

# quiz) 로그인 기능 만들기
'''
시스템 관리자(administrator) 로그인 기능을 만들어 봅시다.
관리자가 암호를 입력하고 로그인을 시도할 때 암호가 틀렸다면 '암호를 다시 확인하세요!'를 출력하고
다시 암호를 물어봅니다. 
5회 이상 로그인에 실패하면 '로그인 실패!! 횟수 초과!!!' 메시지를 출력하고 종료합니다.
암호가 올바르다면 '로그인 됐습니다.'를 출력하고 종료합니다. 올바른 암호는 'dwac1234'입니다.  
'''

# ADMIN_PW = 'dwac1234'
# count = 1

# while True:

#     if count > 5:
#         print('누구야 너 로그인 실패!!!')
#         break

#     inputPw = input('관리자 암호를 입력하세요: ')

#     if inputPw != ADMIN_PW:
#         print('X --> 암호를 다시 확인하세요.')
#         count += 1

#     elif inputPw == ADMIN_PW:
#         input('O --> 로그인 성공!!')
#         break

# quiz)
'''
사용자가 입력한 양수를 이용해 팩토리얼 값을 구하는 프로그램을 만드시오. 팩토리얼(factorial, !) n!은 1부터 양의 정수 n까지의 모든 정수를 곱한 값을 말한다.
(예를 들어, 4!은 1x2x3x4 = 24이다.)
'''

# userInputIntegerData = int(input('양수 입력: '))
# result = 1
# for num in range(1, userInputIntegerData + 1):
#     result *= num
# print(f'{userInputIntegerData}의 팩토리얼은 {result}이다.')

# quiz) 숫자 맞추기 게임을 만들자
'''
0부터 100 사이의 난수를 발생시키고 사용자가 난수를 맞힐 때까지 계속해서 물어보는 게임을 만드시오.
다음은 프로그램 개발에 필요한 요구사항입니다.
--- 요구사항 ---
- 1부터 100까지의 난수를 발생시킨다.
- 사용자가 입력한 숫자가 난수와 일치하면 ‘정답입니다.’를 출력하고 게임을 종료한다.
- 사용자가 입력한 숫자가 난수와 일치하지 않으면 ‘틀렸습니다. 다시 입력하세요.’를 출력하고, 다시 물어본다.
- 기회는 10회로 제한한다. 만약 열 번을 넘어가면 ‘게임에 졌습니다.’를 출력하고 게임을 종료한다.
- 사용자가 틀릴 때마다 사용자가 입력한 숫자와 난수를 비교해서 크고, 작음을 출력한다. 
- 게임이 종료하기 전 난수를 출력한다.
'''
# import random

# randomNum = random.randint(1, 100)
# chance = 1

# while chance <= 10:
#     userNum = int(input('숫자를 입력하세요: '))

#     if userNum == randomNum:
#         print('정답입니다.')
#         break

#     if userNum < randomNum:
#         print('틀렸습니다. 더 큰 수를 입력하세요.')
#     else:
#         print('틀렸습니다. 더 작은 수를 입력하세요.')

#     chance += 1

# else:
#     print('게임에 졌습니다.')

# print(f'난수: {randomNum}')

# 다음 요구조건을 참고하여 가로와 세로 길이의 변화에 따른 사각형의 넓이를 구하는 프로그램을 만드시오.
'''
- 가로 길이는 1부터 2의 배수로 증가한다.
- 세로 길이는 1부터 3의 배수로 증가한다.
- 사각형의 넓이가 150 보다 크면 프로그램을 종료한다. 
- 가장 작은 사각형과 가장 큰 사각형의 넓이를 출력한다.
'''
# [[ 초기값 ]]
# 가로 & 세로
wid = 1     # 가로 길이
hei = 1     # 세로 길이
# maxArea = 150       # 가장 큰 사각형의 넓이

# smallArea = wid * hei       # 가장 작은 사각형 넓이를 저장하는 변수입니다.
# bigArea = wid * hei         # 가장 큰 사각형 넓이를 저장하는 변수입니다.


# while True:
#     area = wid * hei        # 현재 사각형의 넓이를 계산합니다.

#     if area > maxArea:      # 넓이가 사각형의 최종 넓이보다 크면 프로그램 종료합니다.
#         break

#     bigArea = area          # 현재 넓이를 가장 큰 넓이로 저장합니다.

#     wid += 2                # 가로 길이 2를 늘리고 다시 진행
#     hei += 3                # 세로 길이 3을 늘리고 다시 진행

# print(f'가장 작은 사각형 넓이: {smallArea}')
# print(f'가장 큰 사각형 넓이: {bigArea}')
width = 1
height = 1

# 가장 작은 사각형 넓이
minArea = width * height
# 가장 큰 사각형 넓이
maxArea = width * height

while True:

    area = width * height   # 사각형 넓이
    
    if area > 150:
        break

    print(f'가로: {width}, 세로: {height}, 넓이:{area}')

    if area < minArea:      # 최소 넓이
        minArea = area
    
    if area > maxArea:      # 최대 넓이
        maxArea = area

    if width == 1:       # width가 1인 경우
        width = 2
    else:                # width가 1이 아닌 경우
        width += 2

    if height == 1:      # height가 1인 경우
        height = 3
    else:                # height가 1이 아닌 경우
        height += 3

print(f'가장 작은 넓이: {minArea}')
print(f'가장 큰 넓이: {maxArea}')