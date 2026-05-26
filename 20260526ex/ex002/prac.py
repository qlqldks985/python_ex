# 다음 실행 결과를 참고하여 컴퓨터와 함께하는 가위,바위,보 게임을 만드세요.
# 난수를 이용해서 진행하고 결과를 출력한다.
'''
가위 바위 보를 선택하세요.
0. 가위, 1.바위, 2.보 0
Com: 바위
User : 가위
컴퓨터 승리!
'''

import random


# items = ['0. 가위','1. 바위','2. 보']
# print('가위바위보 게임을 시작합니다.')
# user = int(input('가위 바위 보 중에서 선택하세요.: '))

# computer = random.randint(0, 2)

# print('나 :', items[user])
# print('컴퓨터 :', items[computer])

# if items[user] == items[computer]:
#     print('무승부입니다.')
# elif items[user] > items[computer]:
#     print('나 님의 승리입니다.')
# elif items[user] < items[computer]:
#     print('컴퓨터의 승리입니다.')

# 다음 실행 결과를 참고하여 단어장에서 무작위로 출력되는 영어단어를 맞추는 게임을 만드시오.
# 영어 : Football       Pencil      Eraser      Car     Doll    Clock
# 한글 :    축구          연필        지우개       차      인형     시계
'''
영어 : Clock
한글을 입력하세요. 자동차
틀렸습니다!!
한글 : 시계
'''

class WordGame:

    def __init__(self):

        self.eng = ['Football', 'Pencil', 'Eraser', 'Car', 'Doll', 'Clock']
        self.kor = ['축구', '연필', '지우개', '차', '인형', '시계']

    def play(self):
        num = random.randint(0, 5)

        print('영어 단어: ', (self.eng[num]))
        userAnswer = input('뜻을 입력하세요.: ')

        if userAnswer == self.kor[num]:
            print('정답입니다!')
        else:
            print('틀렸습니다!!')
            print('정답: ', self.kor[num])
