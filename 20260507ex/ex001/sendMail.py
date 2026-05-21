# print('회원정보를 입력하세요.')

# userName = input('이름: ')
# userMail = input('메일: ')
# userId = input('아이디: ')
# userPw = input('비밀번호: ')

# print('-------------------------------------')
# print('To. ' + userMail)
# print('▶아이디 및 비밀번호 확인')
# print(userName + ' 고객님 안녕하세요.')
# print(userName + ' 고객님의 아이디와 비밀번호는 아래와 같습니다.')
# print('아이디: ' + userId)
# print('비밀번호: ' + userPw)
# print('감사합니다.')
# print('Naver 담당자.')
# print('-------------------------------------')

# userMail = 'gildong@gmail.com'
# print('To. gildong@gmail.com')
# print('To. ' + userMail)        # (*****)

# print("이름:", "홍길동", "나이:", 20)        # 이름: 홍길동 나이: 20 (*****)

# print("2026", "05", "06", sep="-")      #2026-05-06 (**)

# print("Hello", end=" ")     #Hello World (*****)
# print("World")

# f-string (가장 많이 사용) (*****************************************)
name = "철수"
age = 25

# # 이름은 철수, 나이는 25입니다.
# print('이름은 ' + str(name) + ', 나이는 ' + str(age) + '입니다.')
# print(f'이름은 {name}, 나이는 {age}입니다.') # EL 표기법
# # format (두번째로 많이 사용) (***********************************************-1)
# print("이름은 {}, 나이는 {}입니다.". format(name, age))

# print('이름은 {1}, 나이는 {0}입니다.'. format(age, name))

# print(f"이름은 {name}, 나이는 {age}입니다.)

# 사용자가 국어, 영어, 수학 점수를 입력하고, 각각의 점수를 화면에 출력하는 프로그램을 만드세요.

# korean = input("국어 점수를 입력하세요: ")
# english = input("영어 점수를 입력하세요: ")
# math = input("수학 점수를 입력하세요: ")

# print(f"국어 점수:", {koreanScore})
# print(f"영어 점수:", {englishScore})
# print(f"수학 점수:", {mathScore})

# 사용자가 2개의 정수를 입력하면, 입력한 숫자의 합과 평균을 구하는 프로그램을 만드세요.

# firstNum = int(input('첫 번쨰 정수 입력: '))
# secondNum = int(input('두 번째 정수 입력: '))


# print(f'합:{firstNum + secondNum}')
# print(f'평균: {(firstNum + secondNum) / 2}')

# var1 = 10
# var2 = 20

# print(f'var1: {var1}, var2: {var2}')

# temp = var1
# var1 = var2
# var2 = temp
# print(f'var1: {var1}, var2: {var2}')
