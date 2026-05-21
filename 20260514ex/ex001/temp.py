# # split(쪼갠다.) (***)
# names = ('박찬호', '이승엽', '박세리', '박지성', '이순철', '선동열', '손흥민', '김연아')
# print(f'names: {names}')
# print(f'names type: {type(names)}')

# str = '박찬호+이승엽+박세리+박지성+이순철+선동열+손흥민+김연아'
# splitedStr = str.split(' ')         #list -> tuple
# print(f'splitedStr: {splitedStr}')
# print(f'splitedStr type: {type(splitedStr)}')


# splitedStr = tuple(splitedStr)
# print(f'splitedStr: {splitedStr}')
# print(f'splitedStr type: {type(splitedStr)}')

# # 튜플 안의 아이템 유/무 확인하기
# # in과 not in 키워드를 사용하면 튜플 안에 특정 아이템의 존재 유/무를 확인할 수 있습니다.
# colors = ('Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple')
# print(f'{'Green'in(colors)}')      # Green > True / Green+ > False
# print(f'{'Green+'in(colors)}')

# if 'Green' in colors:
#     print('colors에는 Green이 있습니다.')
# else:
#     print('colors에는 Green이 없습니다.')       # in > 있습니다 먼저

# if 'Green' not in colors:
#     print('colors에는 Green이 없습니다.')       # not in > 없습니다 먼저
# else:
#     print('colors에는 Green이 있습니다.')

#quiz) 학정 경고 프로그램 만들기
'''
scores는 1학기 성적을 튜플로 나타낸 것입니다. F 학점이 있으면 ‘경고’를 출력하는 프로그램을 만들자!
scores = ('A', 'A+', 'B', 'B-', 'F')
'''
# scores = ('A', 'A+', 'F', 'B', 'B-', 'F')
# if 'F' in scores:
#     print('경고!')
# else:
#     print('경고 없음')

# scores = ('A', 'A+', 'F', 'B', 'B-', 'F')
# fCnt = scores.count('F')
# print(f'F학점 개수: {fCnt}')

# 튜플 결합
# at list
# nums1 = [1,2,3]
# nums2 = [10, 20, 30]

# 첫 번째 방법
# nums1.extend(nums2)
# print(f'nums1: {nums1}')

# 두 번째 방법
# result = nums1 + nums2
# print(f'nums1: {nums1}')
# print(f'nums2: {nums2}')
# print(f'result: {result}')

# at tuple          # 병합은 되는데 수정이 안된다 extend 는 사용 불가
# nums1 = (1,2,3)
# nums2 = (10, 20, 30)
# result = nums1 + nums2
# print(f'nums1: {nums1}')
# print(f'nums2: {nums2}')
# print(f'result: {result}')

# num1 = 10
# num2 = num1
# print(f'nums1: {num1}')      # 10
# print(f'nums2: {num2}')      # 10

# nums1 = [1,2,3]
# nums2 = nums1
# print(f'nums1: {nums1}')        # [1, 2, 3]
# print(f'nums2: {nums2}')        # [1, 2, 3]

# num1 = 100                      # num1: 100
# print(f'num1: {num1}')
# print(f'num2: {num2}')          # # num2: 10

# nums1[0] = 100                  
# print(f'nums1+++: {nums1}')     # [100, 2, 3]
# print(f'nums2+++: {nums2}')     # [100, 2, 3]


# nums1 = [1,2,3]
# nums2 = [0, 0, 0]

# for idx, num in enumerate(nums1):
#     nums2[idx] = num # type: ignore

# print(f'nums1: {nums1}')    # [1,2,3]
# print(f'nums2: {nums2}')    # [1,2,3]

# nums1[0] = 100
# print(f'nums1: {nums1}')    # [100,2,3]
# print(f'nums2: {nums2}')    # [1,2,3]

# print('deep copy --------------------')

# import copy

# a = [1, 2, 3, 4, 5]
# # b = copy.deepcopy(a)      # (o)
# b = a.copy()                # (x)

# b[0] = 100

# print(f'a: {a}')    # [1, 2, 3, 4, 5]
# print(f'b: {b}')    # [100, 2, 3, 4, 5]

# # 슬라이싱
# animals = ('호랑이', '사자', '곰', '여우', '늑대')
# print(f'animals: {animals}')

# print(f'animals[:3]: {animals[:3]}')            # ('호랑이', '사자', '곰')
# print(f'animals[1:4]: {animals[1:4]}')          # ('사자', '곰', '여우')
# print(f'animals[:-2]: {animals[:-2]}')          # ('호랑이', '사자', '곰')
# print(f'animals[-1:-2]: {animals[-1:-2]}')      # (0)
# print(f'animals[-3:-1]: {animals[-3:-1]}')      # ('곰', '여우')

# 슬라이싱 연습하기
'''
fruits 튜플에서 주어진 요구사항에 맞게 슬라이싱해봅시다.
fruits = ('apple', 'banana', 'plum', 'watermelon', 'peach')
 - 인덱스 2부터 4까지의 아이템을 출력하시오.
 - 인덱스 0부터 3까지의 아이템을 출력하시오.
 - 인덱스 3부터 끝까지의 아이템을 출력하시오.
'''
# fruits = ('apple', 'banana', 'plum', 'watermelon', 'peach')
# print(f' fruits[2:5]: {fruits[2:5]}')           # ('plum', 'watermelon', 'peach')
# print(f' fruits[0:4]: {fruits[0:4]}')           # ('apple', 'banana', 'plum', 'watermelon')
# print(f' fruits[3:]: {fruits[3:]}')             # ('watermelon', 'peach')
# print(f' fruits[:-2]: {fruits[:-2]}')           # ('apple', 'banana', 'plum')
# print(f' fruits[3:-2]: {fruits[3:-2]}')           # ()
# print(f' fruits[5:-2]: {fruits[5:-2]}')           # ()

# 리스트와 튜플간 변환(형변환, casting)
'''
불가피하게 튜플의 아이템을 수정하려면 리스트로 변환해야 합니다.
또한 리스트로 선언된 데이 터를 수정이 안 되게 하려면 튜플로 변환해야 합니다.
다음은 데이터 변환을 통해 리스트와 튜플을 변환하고 있습니다.
'''

colors = ('Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple')

# Orange => 오렌지
# colors[1] = '오렌지'
colors = list(colors)
print(f'colors: type: {type(colors)}')

colors[1] = '오렌지'
print(f'colors: {colors}')      # ['Red', '오렌지', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple']

# colors = tuple(colors)
# print(f'colors: {colors}')

# quiz) 튜플 정렬하기
colors = ('Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple')

# colors = list(colors)
# print(f'colors: type: {type(colors)}')
# colors.sort()
# print(f'colors: {colors}')
# colors.sort(reverse=True)
# print(f'colors: {colors}')

# colors = tuple(colors)
# print(f'colors: type: {type(colors)}')

# colors = ('Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple')

# cs = tuple(sorted(colors))
# print(f'cs: {cs}')      # ['Blue', 'Green', 'Indigo', 'Orange', 'Purple', 'Red', 'Yellow']


