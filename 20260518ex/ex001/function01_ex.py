# 다음은 슈퍼마켓의 상품가격표이다. 가격표와 실행 결과를 참조해서 영수증을 출력하는 함수를 만들어보자.
# 단 상품 구매 개수는 사용자가 입력한다.

goods = {
    '새우깡': 1200,
    '비비빅': 400,
    '초코파이': 500,
    '맛동산': 1500,
}

totalPrice = 0

def shrimpCrackerPrice():
    global totalPrice
    totalPrice += goods['새우깡'] * shrimpCrackers
    print(f'새우깡 구매 금액: {goods["새우깡"]*shrimpCrackers}원')

def bibibigPrice():
    global totalPrice
    totalPrice += goods['비비빅'] * bibibigs
    print(f'비비빅 구매 금액: {goods["비비빅"]*bibibigs}원')

def chocoPiePrice():
    global totalPrice
    totalPrice += goods['초코파이'] * chocoPies
    print(f'초코파이 구매 금액: {goods["초코파이"]*chocoPies}원')

def MatdongsanPrice():
    global totalPrice
    totalPrice += goods['맛동산'] * Matdongsans
    print(f'맛동산 구매 금액: {goods["맛동산"]*Matdongsans}원')

shrimpCrackers = int(input('새우깡 구매 개수: '))
bibibigs = int(input('비비빅 구매 개수: '))
chocoPies = int(input('초코파이 구매 개수: '))
Matdongsans = int(input('맛동산 구매 개수: ')) 

print(f'새우깡 구매 개수: {shrimpCrackers}')
print(f'비비빅 구매 개수: {bibibigs}')
print(f'초코파이 구매 개수: {chocoPies}')
print(f'맛동산 구매 개수: {Matdongsans}')
print('=' * 40)
shrimpCrackerPrice()
bibibigPrice()
chocoPiePrice()
MatdongsanPrice()
print('=' * 40)
print(f'총 구매 금액: {totalPrice}')
print('=' * 40)

# global 역할
# 함수 내부에서 전역변수를 수정하고 싶을 때 사용합니다.

student = {     # student 변수 {} 데이터의 주소 값을 가지고 있다.
    '이름':'홍길동',
    '나이':25
}

print(f'나이: {student["나이"]}')

def modifyStudentAge():
    student['나이'] += 1

modifyStudentAge()
print(f'나이: {student["나이"]}')