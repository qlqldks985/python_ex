import urllib.request
import datetime
import json

client_id = 'xy85smhQ2zfLEm3AEe_x'
client_Secret = 'jledF33tnN'

# NAVER에서 데이터 가져오는 녀석
def getRequestUrl(url):
    req = urllib.request.Request(url)                       # url 주소로 접속하기 위한 요청 정보를 만들고 그 요청 객체를 req 변수에 저장한 것
    req.add_header('X-Naver-Client-Id', client_id)          # 네이버에 요청 보낼때 인증을 위한 ID값을 더함
    req.add_header('X-Naver-Client-Secret', client_Secret)

    try:
        response = urllib.request.urlopen(req)
        # 응답 코드란 : 웹 브라우저나 프로그램이 서버에 요청했을 때, 서버가 결과 상태를 숫자로 알려주는 코드
        # 요청 성공했는지, 페이지가 없는지, 접근이 금지되었는지, 서버 오류가 걸렸는지
        if response.getcode() == 200:
            print(f'[{datetime.datetime.now()}]URL REQUEST SUCCESS!!')
            # print(f'response data: {response.read().decode('utf-8')}')
            # decode란 바이트(byte) 코드를 문자열(string)로 변환하는 것
            return response.read().decode('utf-8')

    except Exception as e:
        print(f'[{datetime.datetime.now()}] Error: {e}')
        return None

# Naver 에서 데이터 검색 하는 녀석
def getNaverSearch(node, secText, start, display):
    base = 'https://openapi.naver.com/v1/search'
    node = f'/{node}.json'       # news.json     뉴스를 주거니 받거니 해야하니 json 파일로
    parameters = f'?query={urllib.parse.quote(secText)}&start={start}&display={display}'

    url = base + node + parameters
    responseDecode = getRequestUrl(url)
    
    if responseDecode == None:
        return None
    else:
        return json.loads(responseDecode)
    
def getpostData(post, jsonResult, cnt):
    title = post['title']
    description = post['description']
    org_link = post['originallink']
    link = post['link']
    pDate = datetime.datetime.strptime(post['pubDate'],  '%a, %d %b %Y %H:%M:%S +0900')
    pDate = pDate.strftime('%Y-%m-%d %H:%M:%S')

    jsonResult.append({
        'cnt': cnt,
        'title': title,
        'description': description,
        'org_link': org_link,
        'link': link,
        'pDate': pDate
    })

def main():
    node = 'news'   # 크롤링 하는 대상을 지정
    srcText = input('검색어 입력: ')
    cnt = 0     # 제한 갯수
    jsonResult = []
     # json 은 javaScript 객체 표기법 을 기반으로 만든 데이터 교환 형식입니다.
    # 쉽게 말하면, 프로그램끼리 데이터를 주고받기 쉽게 만든 텍스트 형식입니다.
    jsonResponse = getNaverSearch(node, srcText, 1, 100 )
    # print(f'jsonResponse: {jsonResponse}')
    # print(f'jsonResponse total: {jsonResponse['total']}')
    # print(f'jsonResponse items 0: {jsonResponse['items'][0]}')
    # print(f'jsonResponse items 0 title: {jsonResponse['items'][0]['title']}')
    # print(f'jsonResponse items 0 description: {jsonResponse['items'][0]['description']}')

    while jsonResponse != None and jsonResponse['display'] != 0:
        for post in jsonResponse['items']:
            cnt += 1
            getpostData(post, jsonResult, cnt)

        jsonResponse = getNaverSearch(node, srcText, jsonResponse['start'] + jsonResponse['display'], 100)

    # 파일로 저장(날씨_naver_news.json)
    with open(f'{srcText}_naver_{node}.json', 'w', encoding='utf8') as f:
        jsonFile = json.dumps(jsonResult, indent=4, sort_keys=True,  ensure_ascii=False)
        f.write(jsonFile)

if __name__ == '__main__':
    main()