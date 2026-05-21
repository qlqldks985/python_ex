# flag = True

# members = {}

# while flag:
#    selectedMenuNum =  int(input('1.회원가입       2.프로그램 종료'))
   
#    if selectedMenuNum == 1:
#       id = input('아이디: ')
#       pw = input('비밀번호: ')
#       members[id] = pw
#    elif selectedMenuNum == 2:
#       flag = False

#       for key in members.keys():
#          print(f'ID: {key}, PW: {members[key]}')

# classes =  {'python':'5학점', 'C/C++':'5학점', 'HTML5':'3학점', 'Java':'5학점', 'Javascript':'3학점'}

# for key in classes:
#     if classes[key] == '3학점':
#         classes[key] = '5학점'
# print(classes)

# members = {
#     '2019-052001':['박찬호', 25, 'M', "010-1234-5678", '헬스,수영',0],
#     '2019-052004':['박용택', 65, 'M', "010-9012-3456", '수영',50],
#     '2019-052003':['박세리', 70, 'W', "010-7890-1234", '아쿠아로빅',50],
# }
'''
# 전체 회원 정보 출력
for key in members:
    print(f'회원번호: {key},회원정보: {members[key]}')

# 전체 회원 정보 출력을 하는데, 이때 회원의 이름과 성별만 출력을 하자!
for key, value in members.items():
    print(f'회원번호: {key},회원정보(이름, 성별): {value[0]},{value[2]}')
'''

# members = {
#     '2019-052001':{
#     '이름': '박찬호',
#     '나이': 25,
#     '성별': 'M',
#     '연락처':'010-1234-5678',
#     '이용서비스': ['헬스', '수영'],
#     '할인율': 0
#     },
#     '2019-052004':{
#     '이름': '박용택',
#     '나이': 65,
#     '성별': 'M',
#     '연락처':'010-9012-3456',
#     '이용서비스': ['수영'],
#     '할인율': 50
#     },
#     '2019-052003':{
#     '이름': '박세리',
#     '나이': 70,
#     '성별': 'W',
#     '연락처':'010-7890-1234',
#     '이용서비스': ['아쿠아로빅'],
#     '할인율': 50
#     }
# }

# 전체 회원 정보 출력
# for key in members:
#     print(f'회원번호: {key}, 회원정보: {members[key]}')

# print('-' * 30)
# # 전체 회원 정보 출력을 하는데, 이때 회원의 이름과 성별만 출력을 하자!
# for key, value in members.items():
#     print(f'회원번호: {key},회원정보(이름, 성별): {value['이름']},{value['성별']}')
# print('-' * 30)
# # 전체 회원 정보 출력을 하는데, 이때 회원의 이름과 성별, 이용서비스만 출력을 하자!
# for key,value in members.items():
#     print(f'회원번호: {key},회원정보(이름, 성별): {value['이름']},{value['성별']},{value['이용서비스']}')
#     # 전체 회원 정보 출력을 하는데, 이때 회원의 이름과 성별, 이용서비스 그리고 이용서비스 갯수 만 출력을 하자!
# for key,value in members.items():
#     print(f'회원번호: {key},회원정보(이름, 성별): {value['이름']},{value['성별']},{value['이용서비스']},{len(value['이용서비스'])}')

# vegetables = {}

# vegetables['당근']= 10
# vegetables['건대추']= 100
# vegetables['대파']= 20
# vegetables['애호박']= 3
# vegetables['부추']= 1

# for key in vegetables:
#     print(f'야채 이름: {key}, 재고: {vegetables[key]}')

# vegetables['당근']-= 1
# vegetables['건대추']-= 10
# vegetables['대파']-= 1
# vegetables['애호박']-= 1
# vegetables['부추']-= 1
# print('-' * 30)
# for key in vegetables:
#     print(f'야채 이름: {key}, 재고: {vegetables[key]}')

# drinks = {}

# drinks['콜라']= 50
# drinks['사이다']= 40
# drinks['오렌지주스']= 30
# drinks['물']= 100
# drinks['커피']= 20

# for key in drinks:
#     print(f'음료 이름:{key}, 음료 재고: {drinks[key]}')

# drinks['콜라']-= 10
# drinks['사이다']-= 5
# drinks['오렌지주스']-= 7
# drinks['물']-= 25
# drinks['커피']-= 3
# for key in drinks:
#     print(f'음료 이름:{key}, 음료 재고: {drinks[key]}')

# 다음 회원 데이터를 사용하시오.
members = {
    '2024-1001': {'이름': '김민준', '나이': 22, '성별': 'M', '이용서비스': ['헬스']},
    '2024-1002': {'이름': '이서연', '나이': 29, '성별': 'W', '이용서비스': ['수영', '필라테스']},
    '2024-1003': {'이름': '박지훈', '나이': 35, '성별': 'M', '이용서비스': ['헬스', '수영', '스피닝']}
}
for key in members:
    print(f'회원 번호: {key}, 전체 정보: {members[key]}')

for key, value in members.items():
    print(f'회원 번호: {key}, 회원정보(이름, 나이): {value['이름']}, {value['나이']}')

for key,value in members.items():
    if value['나이'] >= 30 :
        print(f'회원번호: {key}, 이름: {value["이름"]}, 나이: {value["나이"]}')

for key,value in members.items():
    print(f'이름: {value["이름"]}, 이용서비스 목록: {value['이용서비스']}, 이용서비스 개수: {len(value['이용서비스'])},')

for key, value in members.items():
    if len(value['이용서비스']) >= 2:
        grade = 'VIP 회원'
    else:
        grade = '일반 회원'

    print(f'회원 번호: {key}, 전체 정보: {members[key]}, 등급: {grade}')

for key, value in members.items():
    if '헬스' in value['이용서비스']:
        print(f'이름: {value["이름"]}, 성별: {value['성별']}, 이용서비스: {value["이용서비스"]}')