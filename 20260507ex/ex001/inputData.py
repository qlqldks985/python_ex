# 데이터 입력(input data)
# input()

'''
print('데이터를 입력하세요.')
inputData = input()        * input() = 외부에서 데이터를 받는 함수
print(inputData)
'''

'''
print('정수를 입력하세요.')
inputInteger = input()    # 6
print(inputInteger)       # 6
print(type(inputInteger)) # Int
'''

'''
print('실수 입력하세요.')
inputFloat = input()       # 3.14
print(inputFloat)          # 3.14
print(type(inputFloat))    # str
'''

# 외부에서 들어온 자료는 전부 문자열로 취급된다.

'''
print('논리형 데이터 입력하세요.')         # 논리형 데이터 입력하세요. (자동개행)
intputBoolean = input()                # True
print(intputBoolean)                   # True
print(type(intputBoolean))             # str
'''

# inputBoolean = input('논리형 데이터 입력하세요.\n') # (\n) 개행을 하는 기능이 있다. \n\n\n\n\n 많을수록 열이 늘어난다.
# print(inputBoolean)       # True
# print(type(inputBoolean)) # str

# 자료(data)형을 변환해야 합니다. data type casting
# userInputData = input('사용자야~~~~ 정수 입력해라~') # 10
# print(userInputData)                              # 10
# print(type(userInputData))                        # str
# userInputData = int(userInputData)                # str --> int
# print(type(userInputData))                        #int

# str -> boolean
# userinputData = input('True or False 입력하세요.')
# print(userInputData)                              # True
# print(type(userInputData))                        # str
# userInputData = bool(userInputData)               #boolean
# print(userInputData)

#str --> float
# userInputData = input('실수 입력하세요.')
# print(userInputData)
# print(type(userInputData))            #str
# userInputData = float(userInputData)  
# print(type(userInputData))            #float

# userInputData = 'true'
# userInputData = bool(userInputData)            #?
# print(type(userInputData))                     #?

x = 3                          # int 3
y = float(x)                   # int -> float
print(y)                       # 3.0
x = 3.141592
y = int(x)
print(y)                      # 3
print(float(y))               # 3.0
