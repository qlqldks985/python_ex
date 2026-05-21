members = []
flag = True

# 회원가입
def signUp():
    userId = input('회원ID: ')
    userPw = input('회원PW: ')
    userEmail = input('회원Email: ')
    userPhone = input('회원Phone: ')

    userInfo = {
        'id': userId,
        'pw': userPw,
        'email': userEmail,
        'phone': userPhone
    }

    members.append(userInfo)
    print('회원가입 완료!')


# 로그인
def logIn():
    userId = input('회원ID: ')
    userPw = input('회원PW: ')

    for member in members:
        if member['id'] == userId and member['pw'] == userPw:
            print('로그인 성공!')
            return

    print('로그인 실패!')


# 특정 회원 정보 출력
def printMember():
    userId = input('회원ID: ')
    userPw = input('회원PW: ')

    for member in members:
        if member['id'] == userId and member['pw'] == userPw:
            print('\n===== 회원 정보 =====')
            print(f"ID: {member['id']}")
            print(f"PW: {member['pw']}")
            print(f"EMAIL: {member['email']}")
            print(f"PHONE: {member['phone']}")
            return

    print('일치하는 회원 정보가 없습니다.')


# 모든 회원 정보 출력
def printAllMembers():

    if len(members) == 0:
        print('등록된 회원이 없습니다.')
        return

    print('\n===== 전체 회원 정보 =====')

    for idx, member in enumerate(members, start=1):
        print(f'\n[{idx}번 회원]')
        print(f"ID: {member['id']}")
        print(f"PW: {member['pw']}")
        print(f"EMAIL: {member['email']}")
        print(f"PHONE: {member['phone']}")


# 회원 정보 수정
def updateMember():
    userId = input('회원ID: ')
    userPw = input('회원PW: ')

    for member in members:
        if member['id'] == userId and member['pw'] == userPw:

            print('\n수정할 정보를 입력하세요.')

            member['pw'] = input('새 비밀번호: ')
            member['email'] = input('새 이메일: ')
            member['phone'] = input('새 전화번호: ')

            print('회원 정보 수정 완료!')
            return

    print('회원 인증 실패!')


# 프로그램 실행
while flag:

    print('\n메뉴')
    print('1. 회원가입')
    print('2. 로그인')
    print('3. 특정 회원 정보 출력')
    print('4. 모든 회원 정보 출력')
    print('5. 회원 정보 수정')
    print('99. 종료')

    selectedMenuNum = int(input('선택 >>> '))

    if selectedMenuNum == 1:
        signUp()

    elif selectedMenuNum == 2:
        logIn()

    elif selectedMenuNum == 3:
        printMember()

    elif selectedMenuNum == 4:
        printAllMembers()

    elif selectedMenuNum == 5:
        updateMember()

    elif selectedMenuNum == 99:
        print('프로그램 종료')
        flag = False

    else:
        print('잘못 입력했습니다.')