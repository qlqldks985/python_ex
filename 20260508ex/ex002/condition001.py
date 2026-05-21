# 조건문(if문) # True 일 경우 실행문 실행, False일 경우 미실행
'''
if 조건식:  if   조건식 클론
    실행문: print('num은 10보다 크다.')
'''

# num = 50
# if num > 10 :
# print('num은 10보다 크다.')

'''
if 키워드: 조건문을 선언하기 위한 키워드로 '만약 ~ 라면'의 뜻을 가지고 있다.
조건식 : 특정 조건을 기술한다. 조건식의 결과에 따라 실행문의 실행 여부가 결정된다.
콜론 : 코드 블록의 시작을 나타내는 것으로 콜론 이후부터가 실행될 문장이다. ( : )
들여쓰기 : 코드 블록의 시작을 의미하며 몇칸을 띄우든 상관은 없지만 여러개일때 칸을 동일시켜야 한다.
끝낼때는 안하면 그만.
실행문: 조건식의 결과가 참(True)인 경우 실행하는 명령문입니다. 조건식이 거짓(False)이면 실행문 실행 x
'''

# 사용자가 입력한 정수가 10보다 크면 실행문을 출력하는 프로그램을 만들어 봅시다.
# num = int(input('please input integer number: '))

# if num > 10:
#     print(f'{num}은 10보다 크다.')

# if num == 10:
#     print(f'{num}은 10과 같다.')

# if num < 10:
#     print(f'{num}은 10보다 작다.')

    # Quiz) 속도위반 경고하기
    # 제한 속도가 50km/h인 도로에서 속도위반을 하는 자동차에 경고를 하는 프로그램을 만들어봅시다.

# carSpeed = int(input('현재 속도를 입력하세요: '))

# if carSpeed > 50 :
#     print(f'속도 위반!!!')

# if carSpeed <= 50 :
#     print(f'정상 운행~~')

# carSpeed = 40       # 간혹 실행문이 한줄일 경우 간략화 가능하다. 단 두줄은 안된다.
# if carSpeed <= 50 :
#      print(f'정상 운행~~')
#      print(f'쪼아요')

# num = 5
# if num > 0 :
#     print('num은 0보다 크다.')

#     print('num은 0보다 크다.') # 들여쓰기 너비가 같을때 실행문 사이에 공백은 아무 상관이 없다.

# pass       # 실행문이 정해지지 않았을 떄 나중에 코딩할거니까 넘기라는 뜻

# if ~ else 구문        #양자택일
# else : 그렇지 않으면
# myScore = 70
# if myScore >= 90 :
#     print('용돈 획득')
# if myScore < 90 :
#     print('빠따')

# if myScore >= 90:
#     print('용돈 획득')
# else:
#     print('빠따')

# if ~ elif 구문        #다중선택
'''
점수가 90점 이상이면 'A' 출력
점수가 80점 이상 ~ 90점 미만이면'B' 출력
점수가 70점 이상 ~ 80점 미만이면'C' 출력
점수가 60점 이상 ~ 70점 미만이면'D' 출력
'''

# myScore = int(input('점수 입력: '))
# if myScore >= 90:
#     print('A')
# elif (myScore >= 70) and (myScore < 80):        #70 이상 80 미만
#     print('C')
# elif (myScore >= 80) and (myScore < 90):
#     print('B')
# elif (myScore >= 60) and (myScore < 70):
#     print('D')
# else:
#     print('F')

# quiz 자동 주문 시스템 만들기
'''
다국어를 지원하는 식당에서 사용할 자동 주문 시스템을 만들고자 합니다.
1번을 누르면 한국어로, 2번을 누르면 영어로, 3번을 누르면 중국어로,
그 외 번호는 영어로 주문을 받는 프로그램을 만들어 봅시다.

1. 대한민국     2. USA      3. 中国 
1.주문하시겠습니까?
2. Would you like to order?
3. 您要点菜吗？
그외. Would you like to order?
'''

# KOREA_NUMBER = 1        # 취업하고싶으면 숫자 1, 2, 3이 아닌 KOREA_NUMBER =1 을 집어놓도록 하자..
# USA_NUMBER = 2
# CHINA_NUMBER = 3
# selectedNumber = int(input('1. 대한민국     2. USA      3. 中国'))
# if   selectedNumber == KOREA_NUMBER:
#     print('주문하시겠습니까?')
# elif selectedNumber == USA_NUMBER:
#     print('Would you like to order?')
# elif selectedNumber == CHINA_NUMBER:
#     print('您要点菜吗？')
# else:
#     print('Would you like to order?')

# quiz 국가재난지원금 수령액 조회하기
# '''
# 다음은 가구 인원수에 따른 국가재난지원금 수령액을 안내하는 프로그램입니다.
# 표를 참고하여 프로그램을 만들어봅시다.
# 1인가구: 400.000원
# 2인가구: 600,000원
# 3인가구: 800,000원
# 4인이상 가구: 1,000,000원
# '''

# ONE_PERSON = 1
# TWO_PERSON = 2
# THREE_PERSON = 3
# family = int(input('가구 인원수를 작성하시오: '))
# if family == ONE_PERSON:
#     print('400,000원')
# elif family == TWO_PERSON:
#     print('600,000원')
# elif family == THREE_PERSON:
#     print('800,000원')
# else :
#     print('1,000,000원')

'''
다음 요구사항을 충족하는 프로그램을 if~elif문을 이용해서 만드시오.
 - BMI 지수를 입력한다.
 - BMI 지수가 90 이하면 '저체중'을 출력한다.
 - BMI 지수가 90 초과~110 이하면 '정상 체중'을 출력한다.
 - BMI 지수가 110 초과~120 이하면 '과체중'을 출력한다.
 - BMI 지수가 120초과~140 이하면 '비만'을 출력한다.
 - BMI 지수가 140 초과면 '고도 비만'을 출력한다.
'''

# bmi = int(input('BMI 지수를 입력하시오: '))

# if bmi <= 90:
#     print('저체중')
# elif bmi > 90 and bmi <= 110:
#     print('정상 체중')
# elif bmi > 110 and bmi <= 120:
#     print('과체중')
# elif bmi > 120 and bmi <= 140:
#     print('비만')
# else:
#     print('고도 비만')

# 중첩 조건문
# 조건문 내에 또 다른 조건문을 쓸 수 있는데 이를 중첩 조건문이라고 합니다.
# 사용자가 입력한 정수에서 양수(0도 포함)인지를 판단하고 양수라면 홀/짝인지 구분하자.

# myInteger = int(input('정수 입력: '))
# if myInteger >= 0:
#     print('양수!')
#     if myInteger % 2 ==0:
#         print('짝수!')
#     else:
#         print('홀수!')
# else:
#     print('음수!')

# Quiz) 짝수/홀수를 판별하는 프로그램을 만들자.
# num = int(input('사용자야~~ 양의 정수 입력해주라~'))
# if num > 0:
#     if num % 2 == 0:
#         print('짝수!!!!!')
#     else:
#         print('홀수!!!!!')
# else:
#     print('입력할 정수는 0 또는 음수 입니다.')

# Quiz)
'''
출생연도 끝자리(endBirthYear)와 나이(age)를 입력하면 다음 요구사항에 맞춰 마스크 구매 가능한
요일을 출력하는 프로그램을 만드시오.

- 공적마스크 판매 관련해서 출생연도 끝자리를 이용한 5부제를 다음과 같이 실시한다.
- 1, 6 => 월
- 2, 7 => 화
- 3, 8 => 수
- 4, 9 => 목
- 5, 0 => 금
- 만 65세 이상 어르신은 언제든지 구매 가능하다.
'''

# endBirthYear = int(input('출생연도 끝자리 입력: '))
# age = int(input('나이 입력: '))

# if age < 65:
#     if endBirthYear == 1 or endBirthYear == 6:
#         print('월요일에 구매 가능합니다.')
#     elif endBirthYear == 2 or endBirthYear == 7:
#         print('화요일에 구매 가능합니다.')
#     elif endBirthYear == 3 or endBirthYear == 8:
#         print('수요일에 구매 가능합니다.')
#     elif endBirthYear == 4 or endBirthYear == 9:
#         print('목요일에 구매 가능합니다.')
#     elif endBirthYear == 5 or endBirthYear == 0:
#         print('금요일에 구매 가능합니다.')
# else:
#     print('언제나 구매 가능합니다.')

# 날짜 관련 모듈: datetime
# from datetime import datetime
# 
# 현재 일 구하기
# print(datetime.today().weekday())       #4 (0:월, 1:화, 2:수, 3:목, 4:금)
# print(datetime.today().day)             #8

# from datetime import datetime
# # print(datetime.today().day)
# dayNum = datetime.today().day

# carNumber = int(input('차량 번호 4자리 입력하시오: '))

# print(f'오늘 날짜: {dayNum}일')

# if carNumber % 2 == 0:
#     print('오늘 입차: 번호가 짝수인 차량')
# else:
#     print('오늘 입차: 번호가 홀수인 차량')

# if dayNum % 2 == carNumber % 2:
#     print('귀하의 차량은 입차 가능합니다.')
# else:
#     print('귀하의 차량은 입차 불가합니다.')

# 다음 표는 심장 정지 환자에게 자동 심장 충격기를 사용했을 때 최초로 시행한 시간에
# 따른 환자의 생존율을 나타냅니다. 표를 보고 장비를 사용하기까지 걸린 시간을
# 입력하면 생존율이 출력되는 프로그램을 만들어봅시다.

# lifeTime = int(input('최초 장비를 사용하기까지 걸린 시간(초)를 입력하세요: '))

# if lifeTime < 60:
#     print('시행한 시간: 1분 이내 사용')
#     print('생존율: 85% 이상')
# elif lifeTime > 60 and lifeTime <= 120:
#     print('시행한 시간: 2분 이내 사용')
#     print('생존율: 76% 이상')
# elif lifeTime > 120 and lifeTime <= 180:
#     print('시행한 시간: 3분 이내 사용')
#     print('생존율: 66% 이상')
# elif lifeTime > 180 and lifeTime <= 240:
#     print('시행한 시간: 4분 이내 사용')
#     print('생존율: 57% 이상')
# elif lifeTime > 240 and lifeTime <= 300:
#     print('시행한 시간: 5분 이내 사용')
#     print('생존율: 47% 이상')
# else:
#     print('시행한 시간: 6분 초과')
#     print('생존율: 25% 미만')

# 전기를 많이 사용하면 누진세가 붙어 단가와 기본요금이 올라갑니다. 다음
# 누진세가 적용된 단기표를 참고하여 전기 사용량을 입력하면 전기료가 출력되는
# 프로그램을 만들어봅시다.

# 사용량  200이하 / 201~400 이하 / 400 초과
# 단가(원) 99.3 / 187.9 / 280.6
# 기본요금(원) 910 / 1600 / 7300

#전기 사용량을 입력하세요. 190
#사용량: 190.0 kwh
#기본요금 : 910원
#단가 : 99.3원
#전기 요금: 19777.0원       # 910 + (190 * 99.3) = 19777.0원

# kwh = int(input("전기 사용량을 입력하세요: "))

# if kwh < 200:
#     price = 99.3
#     basic = 910
# elif kwh > 201 and kwh <= 400:
#     price = 187.9
#     basic = 1600
# else:
#     price = 280.6
#     basic = 7300

# total = (kwh * price + basic)

# print(f"사용량에 따른 요금 :", kwh, "kwh")
# print("단가 :", price, "원")
# print("기본요금 :", basic, "원")
# print("전기 요금 :", total, "원")

# 어린이의 신장을 입력하면 놀이기구 탑승 여부가 출력되는 프로그램을 만드시오(단, 놀이기구 탑승은 신장이 최소 120cm부터 최대 160cm까지 가능하다.)
# height = int(input('신장을 입력하세요: '))

# if height < 120:
#     print('탑승이 불가합니다.')
# elif height > 120 and height <= 160:
#     print('탑승이 가능합니다.')

# testScore = int(input('시험 점수 입력: '))
# if testScore >= 85:
#      print('success')
# else:
#      print('fail')

# 다음은 컴퓨터와 사용자가 '난수를 이용한 가위 바위 보 게임'을 하는 모습이다. 실행 결과를 보고 프로그램을 완성하시오.

# import random       #난수 발생 모듈

# ranNum = random.randint(1, 3)        #1부터 3까지의 점수중에서 하나는 발생한다.

# myNum = int(input('1.가위 2.바위 3.보 를 선택하세요.'))
# if (ranNum == 1 and myNum == 1) and (ranNum == 2 and myNum == 2) and (ranNum == 3 and myNum == 3):
#     print('무승부')
# elif (ranNum == 1 and myNum == 2) and (ranNum == 2 and myNum == 3) and (ranNum == 3 and myNum == 1):
#     print('사용자 승')
# elif (ranNum == 1 and myNum == 3) and (ranNum == 2 and myNum == 1)and (ranNum == 3 and myNum == 2):
#     print('컴퓨터 승')

# '''
# 사용자가 입력한 문자 메세지 길이에 따라서 SMS 또는 MMS의 발송을 결정하는 프로그램을 완성하시오(단, 메시지 길이가 50 이하면 SMS 발송, 그렇지 않으면 MMS를 발송한다.)
# '''

# # str = 'hello'
# # print(f'str: {str}')        #hello
# # print(f'str\'length: {len(str)}')        #5

# useMessage = input('메시지를 입력하세요.')
# msgLen = len(useMessage)

# if msgLen <= 50:
#     print('SMS 발송!')
# else:
#     print('MMS 발송!')