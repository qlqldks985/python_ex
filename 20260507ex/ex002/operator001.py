# 산술 연산자
# 산술 연산자는 우리가 자주 사용하는 사칙 연산자와
# 컴퓨터 프로그램에서만 사용하는 나머지, 몫, 지수 연산자를 뜻합니다.
# +, -, *, /
# %(나머지), //(몫), (**)지수

# 덧셈 연산자(+)
# print( 10 + 20 )
# print(3.14 + 5)
# num1 = 10; num2 = 100
# print(num1 + num2)

# # DW 전자 회사에서 1분기 매출의 총합을 구하고자 합니다. 프로그램을 작성해봅시다.
# sales1 = int(input('1월 매출: '))
# sales2 = int(input('2월 매출: '))
# sales3 = int(input('3월 매출: '))
# total = sales1 + sales2 + sales3
# print(f'1분기 매출 : {total:,}원')

# 문자열 덧셈
# print('a' + 'b')        # 덧셈(연결) 연산자

# 문자열 + 숫자 > TypeError
# print('Hello' + 3 )

# 뺄셈 연산자
# print(10 - 5)
# print(3.14 - 0.1)

# print('hello' - 10)

# DW 전자에서 1분기 수익을 계산하려고 합니다.
# 사용자가 1분기 매출액과 매입액을 입력하면
# 수익을 계산해주는 프로그램을 만들어봅시다.

# sales = int(input('1분기 매출: '))       # 매출 입력
# purchase = int(input('1분기 매입: '))      #매입 입력
# profit = sales - purchase           #수익 계산
# print(f'수익: {profit:,}원')

# 곱셈(*) 연산자
# print(10 * 20)
# print(3.14 * 3)

# # 문자열 곱셈
# str = 'hello'       # hello hello hello
# print(str * 3)

# # 가로, 세로 길이를 입력하면 방의 넓이를 계산해주는 프로그램을 만들어봅시다.
# width = int(input(' 가로 입력: '))
# length = int(input(' 세로 입력: '))
# area = width * length
# print(f'방의 넓이: {area}')

# # 'Good morning' 문자열을 사용자가 입력한 숫자만큼 출력하는 프로그램입니다.
# intro = 'Good morning'
# cnt = int(input(' 출력을 원하는 횟수를 입력하세요. '))
# print(intro * cnt)

# # 나눗셈 연산자(/)
# print(10 / 2)       #5.0
# print(3.14 / .5)

# num1 = 100
# num2 = 10
# print(f'num1 / num2 = {num1 / num2}')

#quiz 신체 질량지수 (BMI) 구하기
# 몸무게와 신장을 입력하면 신체질량지수(BMI) 를 계산해주는
#프로그램을 만들어봅시다(BMI = 몸무게(kg) / 신장의 제곱(m2))

# weight = float(input('몸무게(kg): '))
# height = float(input('신장(m): '))
# bmi = weight / (height * height)
# print(f'BMI: {bmi}')

# print(f'BMI: {bmi : .2f}')
# 숫자 0을 어떤 수로 나누어도 결과는 항상 0이다.
# print(0 / 123)      #0
# # 어떤 숫자를 0으로 나눌 수 없다. 즉 에러.
# print( 10 / 0 )

# print(f'BMI: {}')
# 컴파일 에러는 눈에 보이기 떄문에 쉽게 고칠 수 있지만
# 런타임(논리적) 에러는 눈에 보이지 않기 때문에 고치기 어렵다.

# 나머지만, 몫, 거듭제곱
# print(10 % 2)
# print(10 % 3)

# 홀짝 게임하기
# 주먹 쥔 손을 상대방에게 내밀며 손 안에 동전 개수가 홀수인지 짝수인지 마주는 게임입니다.
# 손 안에 동전 개수를 입력하면 짝수는 0, 홀수는 1을 출력하는 프로그램을 만들어봅시다.
# inputData = int(input('손 안에 동전 수를 입력하세요.'))
# result = inputData % 2
# print(result)

# 몫(//)
# print(10 // 3)
# print (6 //2)

# # 빵을 나누어 줄 수 있는 학생 수 구하기
# # 길동이는 97개의 빵을 3개씩 같은 반의 친구들에게 나누어 주려고 합니다.
# # 최대 몇 명에게 나누어 줄 수 있는지 구하고, 남는 빵의 개수도 구해봅시다.
# bread = 97
# breadcut = 3
# maxFriendCnt = bread // breadCnt
# print(f'빵을 나누어 줄 수 있는 학생 수: {maxFriendCut}')

# restBreadCnt = bread % breadCnt
# print(f'남는 빵 개수: {restBreadCnt}')

# 거듭제곱(**)
# print( 2**2 )
# print( 2**3 )
# print( 2**10 )

# 전염병 예상 감염자 수 구하기
# 보건 당국은 전염병의 감염 확산 추세를 파악한 결과,
# 하루에 한 사람이 한 명씩 감염시키는 것으로 나타났습니다.
# 확진자 한 사람이 나올 경우 30일 이후에 몇 명의 감염자가 나오는지 계산해봅시다.
# man = 2
# date = 30
# total = man ** date
# print(f'{date}일 이후 예상 감염자 수: {total}')