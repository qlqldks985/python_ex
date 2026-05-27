import urllib.request           # 인터넷 주소(URL)를 열고 데이터를 가져오는 도구
import datetime                 # 날짜와 시간을 다루는 도구
import json                     # 데이터를 JSON 형식으로 변환하거나 읽는 도구

client_id = 'xy85smhQ2zfLEm3AEe_x'      # 네이버 API를 사용하기 위한 아이디
client_Secret = 'jledF33tnN'            # 네이버 API를 사용하기 위한 비밀번호

# NAVER에서 데이터 가져오는 녀석
def getRequestUrl(url):
    req = urllib.request.Request(url)                       # 입력받은 주소(URL)로 갈 준비를 함
    req.add_header('X-Naver-Client-Id', client_id)          # 네이버 통행증(아이디)을 챙김
    req.add_header('X-Naver-Client-Secret', client_Secret)  # 네이버 통행증(비밀번호)을 챙김

    try:
        response = urllib.request.urlopen(req)              # 실제로 네이버 서버에 접속해서 응답을 받음
        # 응답 코드란 : 웹 브라우저나 프로그램이 서버에 요청했을 때, 서버가 결과 상태를 숫자로 알려주는 코드
        # 요청 성공했는지, 페이지가 없는지, 접근이 금지되었는지, 서버 오류가 걸렸는지
        if response.getcode() == 200:                       # 응답 코드가 200(성공)이라면
            print(f'[{datetime.datetime.now()}]URL REQUEST SUCCESS!!')  # 화면에 '성공했다'고 시간을 찍어줌
            # print(f'response data: {response.read().decode('utf-8')}')
            # decode란 바이트(byte) 코드를 문자열(string)로 변환하는 것
            return response.read().decode('utf-8')          # 컴퓨터용 데이터를 우리가 읽을 수 있는 문자열로 바꿔서 반환함

    except Exception as e:
        print(f'[{datetime.datetime.now()}] Error: {e}')    # 만약 접속에 실패하거나 에러가 나면 에러 내용을 화면에 출력함
        return None                                         # 아무것도 반환하지 않음(빈손으로 돌아감)

# Naver 에서 데이터 검색 하는 녀석
def getNaverSearch(node, secText, start, display):          
    base = 'https://openapi.naver.com/v1/search'            # 네이버 검색 기본 주소
    node = f'/{node}.json'       # news.json     뉴스를 주거니 받거니 해야하니 json 파일로
    parameters = f'?query={urllib.parse.quote(secText)}&start={start}&display={display}'    # 검색어(인코딩 포함), 시작 위치, 가져올 개수 설정

    url = base + node + parameters                          # 위의 주소들을 다 합쳐서 하나의 완성된 인터넷 주소로 만듦
    responseDecode = getRequestUrl(url)                     # 완성된 주소를 들고 위에서 만든 '접속 함수'를 호출함
    
    if responseDecode == None:                              # 만약 가져온 데이터가 없다면
        return None                                         # 빈 값을 돌려줌
    else:                                                   # 데이터를 잘 가져왔다면
        return json.loads(responseDecode)                   # 글자 덩어리(JSON 문자열)를 파이썬이 다루기 쉬운 딕셔너리/리스트 형태로 변환해서 반환함
    
def getpostData(post, jsonResult, cnt):
    title = post['title']                                   # 뉴스 제목을 추출
    description = post['description']                       # 뉴스 요약 내용을 추출
    org_link = post['originallink']                         # 언론사 원본 뉴스 링크를 추출
    link = post['link']                                     # 네이버 뉴스 링크를 추출
    pDate = datetime.datetime.strptime(post['pubDate'],  '%a, %d %b %Y %H:%M:%S +0900') # 네이버가 준 이상한 날짜 형식을 컴퓨터가 이해하게 바꿈
    pDate = pDate.strftime('%Y-%m-%d %H:%M:%S')             # 우리가 보기 편한 '년-월-일 시:분:초' 형식으로 날짜를 예쁘게 바꿈

    jsonResult.append({                                     # 예쁘게 정리한 데이터들을 결과 바구니(jsonResult)에 하나씩 추가함
        'cnt': cnt,
        'title': title,
        'description': description,
        'org_link': org_link,
        'link': link,
        'pDate': pDate
    })

def main():
    node = 'news'   # 크롤링할 대상은 '뉴스'로 지정
    srcText = input('검색어 입력: ')    # 사용자에게 어떤 단어를 검색할지 입력받음
    cnt = 0     # 가져온 뉴스 개수를 세기 위한 계수기(카운터)
    jsonResult = []                   # 최종 결과를 모두 담아둘 빈 바구니(리스트)
     # json 은 javaScript 객체 표기법 을 기반으로 만든 데이터 교환 형식입니다.
    # 쉽게 말하면, 프로그램끼리 데이터를 주고받기 쉽게 만든 텍스트 형식입니다.
    jsonResponse = getNaverSearch(node, srcText, 1, 100 )   # 1번째 뉴스부터 100개를 가져오라고 네이버에 첫 요청을 보냄
    # print(f'jsonResponse: {jsonResponse}')
    # print(f'jsonResponse total: {jsonResponse['total']}')
    # print(f'jsonResponse items 0: {jsonResponse['items'][0]}')
    # print(f'jsonResponse items 0 title: {jsonResponse['items'][0]['title']}')
    # print(f'jsonResponse items 0 description: {jsonResponse['items'][0]['description']}')

    while jsonResponse != None and jsonResponse['display'] != 0:    # 데이터가 있고, 네이버가 준 뉴스 개수가 0개가 아닐 때까지 계속 반복함
        for post in jsonResponse['items']:  # 네이버가 던져준 뉴스 뭉치(100개)에서 뉴스 한 개씩 꺼냄
            cnt += 1    # 뉴스 개수를 1 더함
            getpostData(post, jsonResult, cnt)  # 꺼낸 뉴스 한 개를 예쁘게 다듬어서 바구니에 넣음
        # 다음 뉴스 100개를 또 가져오기 위해 시작 위치를 뒤로 밀어서 다시 요청함 (예: 1번째 다음은 101번째)
        jsonResponse = getNaverSearch(node, srcText, jsonResponse['start'] + jsonResponse['display'], 100)

    # 모든 뉴스를 다 가져왔다면 파일로 저장할 준비를 함 (파일명 예: 아이폰_naver_news.json)
    with open(f'{srcText}_naver_{node}.json', 'w', encoding='utf8') as f:
        # 바구니에 담긴 파이썬 데이터를 예쁜 JSON 글자 덩어리로 변환함 (들여쓰기 4칸, 알파벳순 정렬, 한글 깨짐 방지)
        jsonFile = json.dumps(jsonResult, indent=4, sort_keys=True,  ensure_ascii=False)
        f.write(jsonFile)   # 완성된 JSON 내용을 실제 파일에 받아 적음

if __name__ == '__main__':
    main()                  # 이 파일이 직접 실행되면 main() 함수를 작동시킴