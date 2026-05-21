# 0.:  99번 입력 시 프로그램 종료
# 0.0 : 0번 매뉴 출력
flag = True

while flag:

    print('\n메뉴')
    print('1. 회원가입')
    print('2. 로그인')
    print('3. 특정 회원 정보 출력')
    print('4. 모든 회원 정보 출력')
    print('5. id찾기')
    print('6. pw찾기')
    print('0. 종료')

    selectedMenuNum = int(input('번호 선택: '))

    if selectedMenuNum == 0:
        
        print('\n정말로 종료하시겠습니까?')
        print('1. 종료')
        print('2. 취소')

    numChoice = int(input('번호를 선택하세요>> '))

    if numChoice == 1:
        print('프로그램을 종료합니다.')
        flag = False
    
    elif numChoice == 2:
        print('종료를 취소합니다.')
        continue
    else:
        print('잘못된 번호입니다. 다시 입력해주세요.')

   