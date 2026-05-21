# 컨테이너 자료형 container data type 같은 유형의 자료를 통으로 묶어 관리
# list, tuple, dictionary
# 프로그램을 개발하다보면 변수를 이용해서 데이터를 하나씩 저장하여 사용하기보다
# 여러 데이터를 묶어서 저장하고 관리하는 것이 훨씬 효율적일 때가 있다. # 과일 데이터가 3개나 있는데? 이걸 묶어서 관리해도 되겠는데?
# fruit1 = [ '사과', '포도', '복숭아']
# tools = [ '연필', '칼' ]
# 컨테이너 자료형에는 리스트, 튜플, 딕셔너리가 있다.
# list : 대괄호 []로 묶어서 표현하는 컨테이너 자료형, 요소의 추가, 삭제, 변경이 가능하다.
# tuple : 소괄호 ()로 묶어서 표현하는 컨테이너 자료형, 요소의 추가, 삭제, 변경이 불가능하다. immutable
# dictionary : 중괄호 {}로 묶어서 표현하는 컨테이너 자료형, 키와 값의 쌍으로 데이터를 저장하는 자료형, 요소의 추가, 삭제, 변경이 가능하다.
# 리스트는 어떤 데이터 집합을 순차적으로 나열하고자 할 때 사용한다.
# 리스트를 선언할 때는 대괄호 []를 이용한다. 리스트의 요소는 [,]쉼표로 구분한다.

# 기초 데이터 타입은 메모리를 직접 관리
# 레퍼런스 데이터 타입은 메모리를 직접 관리하지 않고 데이터의 주소를 기억함
# fruit 이라는 변수안에 사과, 포도, 메론이 직접 담기는게 아니라 사과, 포도, 메론이 저장된 메모리 주소가 fruit 변수에 담긴다. 그래서 레퍼런스 데이터 타입이라고 불리는 것이다.
# 기초 데이터 타입: 위치
# 레퍼런스 데이터 타입 : 네비게이션

# 기존 레퍼런스 데이터 타입에 새로운 데이터가 추가되면 기존 데이터가 저장된 메모리 주소는 변경되지 않고 새로운 데이터가 저장된 메모리 주소가 새로 만들어진다.
# # 기초 데이터는 garbage collecter가 알아서 메모리를 관리 

# 리스트
fruits = ['사과', '포도', '수박', '참외', '배', '자두', '복숭아', '바나나']
# print(f'fruits: {fruits}')
# print(f'type of fruits: {type(fruits)}')

# 리스트와 데이터
'''
리스트에 포함되는 데이터는 어떤 자료형이든 상관없습니다.
예를 들어 정수, 실수, 문자(열)이 하나의 리스트로 묶일 수도 있습니다.
'''
complexList = [10, 3.14, 'a', 'hello']
# 이렇게 하나의 리스트에 다양한 데이터 타입의 데이터를 넣을 수 있는 언어는 
# 파이썬과 javaScript뿐이다. java는 안된다.
# print(f'complexList: {complexList}')
# print(f'type of complexList: {type(complexList)}')

# member = []
# print(f'member: {member}')
# print(f'type of member: {type(member)}')

# #ex) 다음 회의 참석자 명단을 리스트로 선언하고 attendList 변수에 담아보자.
# attendList = ['이순철', '김병헌', '김민우', '박찬호', '김민태']
# print(f'attendList: {attendList}')
# print(f'type of attendList: {type(attendList)}')

# # how to 리스트의 아이템 조회
# # 특정 아이템 조회
# #           0       1      2      3      4      5       6        7
# fruits = ['사과', '포도', '수박', '참외', '배', '자두', '복숭아', '바나나']
# print(fruits[2])
# print(f'fruits[3]: {fruits[3]}')
# print(f'fruits[7]: {fruits[7]}')

# 만약 리스트에서 존재하지 않는 인덱스를 참조하면 어떻게 될까요?
# print(f'fruits[8]: {fruits[8]}')
# 당연히 에러가 발생합니다. 다음 코드로 확인해봅시다. (IndexError: list index out of range)

# 리스트 길이(아이템 개수) 조회
'''
리스트 길이란 리스트의 아이템 개수를 뜻하는 것으로 len() 함수를 사용하면 알 수 있습니다.
다음은 len() 함수를 이용해서 리스트의 길이를 확인하는 코드입니다.
'''
# numbers = [1, 2, 3, 4, 5]
# print(f'numbers: {numbers}')
# print(f'numbers length: {len(numbers)}')

# numbers = [ 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 99,]
# # 첫 번째 데이터 조회:
# print(f'첫 번째 데이터 : {numbers[0]}')

# # 마지막 데이터 조회:
# print(f'마지막 데이터 : {numbers[len(numbers) - 1]}') # 인덱스에서 마지막 데이터는 길이 -1이다.

# len() 함수는 문자열의 길이를 조회하는데에도 사용된다.
# str = 'helllllllllllllllllo' # 띄어쓰기도 길이에 포함된다.
# print(len(str))

# #quiz) 입력한 글자 수 확인하기
# '''
# 사용자로부터 메시지를 입력 받고, 입력 받은 문자열의 길이를 출력하는 프로그램을 만들어봅시다.
# '''
# message = input('메시지를 입력하세요: ')
# msgLen = len(message)
# print(f'msgLen: {msgLen}')

# 리스트 전체 데이터 조회
balls = ['축구공', '농구공', '배구공', '탁구공', '야구공']
# print(f'{balls[0]}')
# print(f'{balls[1]}')
# print(f'{balls[2]}')
# print(f'{balls[3]}')
# print(f'{balls[4]}')

# for 변수 in 이터러블 데이터:
#     pass

# idx = 0     #(******************)
# for item in balls:      # item = '축구공', item = '농구공', item = '배구공' ...
#     print(f'item: {item}, index: {idx}')
#     idx += 1

# idx = 0     #(******************)
# for idx, item in enumerate(balls): # item = '축구공' idx = 0, item = '농구공' idx = 1, item = '배구공' idx = 2 ...
#     print(f'item: {item}, index: {idx}')

# balls = ['축구공', '농구공', '배구공', '탁구공', '야구공']

# i = 0
# while i < len(balls):
#     print(f'items: {balls[i]}, index: {i}')
#     i += 1

#문자 #정수 #실수 #불 #문자열
#quiz) 다음 리스트에서 마지막 인덱스 값을 출력하는 프로그램을 만드시오.
#            0             1           2        3        4
# sports = ['basball', 'basketball', 'tennis', 'golf', 'soccer']
# lenVar = len(sports) - 1
# print(sports[4])    # 5 - 1 = 4

# # quiz) 다음 리스트에서 'python' 문자열의 인덱스 값을 출력하는 프로그램을 만드시오
# languages = ['c/c++', 'c#', 'python', 'java']
# for idx, str in enumerate(languages):
#     if str == 'python':
#         print(f'python idx: {idx}')

# # 위 방식은 리스트의 길이만큼 반복문이 돌아야하기 때문에 비효율적이다. 리스트에서 특정 데이터의 인덱스를 조회하는 방법이 따로 있다.
# targetIdx = languages.index('python')
# print(f'targetIdx: {targetIdx}')

# # 아이템 기존 리스트에 삽입
# # 리스트 마지막에 삽입
# sports = ['football', 'baseball', 'volleyball']
# add = 'basketball'
# sports.append(add)  # append() 메서드는 리스트의 마지막에 새로운 아이템을 추가하는 메서드입니다.
# print(f'sports: {sports}')
# print(f'sports length: {len(sports)}')

# # quiz) 취미 추가하기
# '''
# 취미들을 저장할 리스트를 정의하고 사용자가 입력한 취미가 추가 되는 프로그램을 만들어보자!
# 그리고 취미의 개수를 출력하자!
# '''

# hobbies = []
# flag = True

# while flag:
#     hobby = input('취미를 입력하세요: ')
#     hobbies.append(hobby)
#     print(f'hobbies: {hobbies}')       # 축구 입력하면 ['축구'] 출력
#     selectedMenuNumber = int(input('1. 취미 추가  2. 종료 '))
#     if selectedMenuNumber == 2:
#         print(f'총 개수: {len(hobbies)}')
#         flag = False # 혹은 break로도 가능하다.

# 특정 위치에 아이템 삽입
# 리스트의 원하는 위치에 아이템을 삽입할 때는 insert() 함수를 이용합니다.
# countries = ['korea', 'china', 'japan'] # ['korea', 'usa', 'china', 'japan']
# countries.insert(1, 'usa') # insert() 메서드는 리스트의 특정 위치에 새로운 아이템을 추가하는 메서드입니다. 첫 번째 인자는 삽입할 위치의 인덱스, 두 번째 인자는 삽입할 아이템입니다.
# print(f'countries: {countries}')        # ['korea', 'usa', 'china', 'japan']

# quiz) 누락된 숫자 추가하기
# numbers = [1, 2, 3, 4, 5, 7, 8, 9]
# numbers 리스트를 보고 1~10까지 숫자 중 누락된 숫자를 추가해보자.
# numbers = [1, 2, 3, 4, 5, 7, 8, 9]
# numbers.insert(5, 6)
# print(f'numbers: {numbers}')
# numbers.append(10)
# print(f'numbers: {numbers}') # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 리스트 연결하기
# 리스트에 또 다른 리스트를 연결할 때는 extend() 함수를 사용합니다.
# list1 = [1, 2, 3]
# print(f'list1: {list1}')    # [1, 2, 3]

# list2 = [10, 20, 30]
# print(f'list2: {list2}')    # [10, 20, 30]

# list1.extend(list2)
# print(f'list1: {list1}')    # [1, 2, 3, 10, 20, 30]
# print(f'list2: {list2}')
# # ---------------------------------------
# list3 = list1 + list2
# print(f'list1: {list1}')
# print(f'list2: {list2}')
# print(f'list3: {list3}')
# # print(f'list3: {list3}')

# # 리스트 아이템 삭제하기
# # 리스트 마지막 아이템 삭제하기
# sports = ['football', 'baseball', 'volleyball', 'basketball']
# print(f'sports: {sports}')
# sports.pop()  # pop() 메서드는 리스트의 마지막 아이템을 제거하고 반환하는 메서드입니다.
# print(f'sports: {sports}')
# sports.pop(1)
# print(f'sports: {sports}')
# removedItem = sports.pop()  # ['football']
# print(f'removedItem: {removedItem}') # volleyball

# # pop() 대신 del 키워드를 이용해서 아이템을 삭제할 수 있다.
# sports = ['football', 'baseball', 'volleyball', 'basketball']
# del sports[2] # del 키워드는 리스트에서 특정 인덱스에 있는 아이템을 삭제하는 키워드입니다. del sports[2]는 sports 리스트에서 인덱스 2에 있는 아이템을 삭제합니다.
# print(f'sports: {sports}') # ['football', 'baseball', 'basketball']

# # quiz) sports 리스트에서 'volleyball' 아이템을 삭제하는 프로그램을 만들어보자!
# sports = ['football', 'baseball', 'volleyball', 'basketball']
# volleyballIdx = sports.index('volleyball')# volleyball이 있는 인덱스 번호를 반환한다. 2
# sports.pop(volleyballIdx)
# print(f'sports: {sports}') # ['football', 'baseball', 'basketball']