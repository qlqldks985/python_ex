# 지금까지는 파이썬 셸 창에서 데이터를 출력하거나 입력했습니다. 이 방법은 데이터를 일시적으로 메모리에 보관할 뿐 영구적이지 않습니다.
# 문자열을 영구적인 보관 방법으로 텍스트 파일을 다루는 방법에 대해서 살펴보겠습니다.
# 파일 열기, 파일 읽기/쓰기, 파일 닫기
'''
1. 파일 열기: 파일을 여는 단계, 파일을 열기 위해서는 open() 함수를 이용한다. 파일 열기에 성공하면 파일은 객체로 만들어져 메모리에 생성된다.
2. 파일 읽기/쓰기: 문자열을 쓰거나 읽는 단계이다. 문자열을 쓸 때는 write() 함수를, 읽을 때는 read() 함수를 이용한다.
3. 파일 닫기: 파일을 닫는 단계이다. 쓰기 또는 읽기가 끝난 파일은 close() 함수를 이용한다.

즉, 텍스트 파일을 다루기 위해서는 위 3가지를 기억하면 된다.
'''

# file = open('C:/JJH/python/test.txt', 'w')  # 파일을 '쓰기' 모드로 open 한다.
# result = file.write('Hello python!')        # 쓰기(Write)
# print(f'result: {result}')                  # 13
# file.close()                                # 파일 닫기(close, 외부자원 해제)

# file = open('C:/JJH/python/test.txt', 'r')
# readResult = file.read()
# print(f'readResult: {readResult}')
# print(f'readResult type: {type(readResult)}')

# readResult = int(readResult)
# readResult += 1
# print(f'readResult: {readResult}')

# file.close()

# file = open('C:/JJH/python/test.txt', 'a')
# file.write('\nhello~')
# file.close()

# with open('C:/JJH/python/test.txt', 'a') as file:
#     for n in range(10):
#         file.write('\nhello~')

# file = open('C:/JJH/python/test.txt', 'a') as file:
# file.write('\nhi~')                           # 'w' 가 기존에 있던 내용을 덮어버린다.
# file.close()

# 예외 처리(보험)
# 세상에 모든 프로그램은 100% 완벽할 수가 없다.

try:
    print(10 + 20)      # 30
    print(10 / 1)       # 에러 발생
except Exception as e:
    print(f'e: {e}')

else:
    print('에러가 발생하지 않으면 실행되는 코드')

finally:
    print('에러가 발생하든 안하든 무조건 실행되는 코드')

    print(10 - 20)      # 출력 불가
    print(10 * 20)      # 출력 불가

    # 에러 발생하면 그 즉시 밑에 있던 뺼셈, 곱셈은 출력을 하지 않고 중단해버린다. 


# 예외 처리 기본 문법
'''
try ~ Exception
'''