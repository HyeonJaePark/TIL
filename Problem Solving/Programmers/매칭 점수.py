import re

def solution(word, pages):
    # 기본점수, 외부 링크 수, 링크점수, 매칭점수
    # 기본점수 = 해당 웹페이지 텍스트 중 검색어가 등장하는 횟수 (대소문자 무시)
    # 외부 링크 수 = 해당 웹페이지에서 다른 외부 페이지로 연결된 링크의 개수
    # 링크점수 = 해당 웹페이지로 링크가 걸린 다른 웹페이지의 (기본 점수 / 외부 링크 수) 의 총합
    # 매칭점수 = 기본점수 + 링크점수
    page_score = {}
    answer = {}
    word = word.lower()
    
    for idx, page in enumerate(pages):
        page = page.lower()
        
        url = re.search(r'(<meta property.+content=")(https://.*)"/>', page).group(2)
        answer[url] = {'index': idx, 'match_score': 0}
        page_score[url] = {'basic_score': 0, 'external_link_score': 0, 'links': []}
        
        external_url = re.findall(r'<a href="https://\S*">', page)
        page_score[url]['external_link_score'] = len(external_url)
        for link in external_url:
            page_score[url]['links'].append(re.search('"(.+?)"', link).group(1))
        
        basic_score = 0
        for vocab in re.findall('[a-z]+', page):
            if vocab == word:
                basic_score += 1
        page_score[url]['basic_score'] = basic_score

    for url in page_score:
        for link in page_score[url]['links']:
            try:
                answer[link]['match_score'] += page_score[url]['basic_score'] / page_score[url]['external_link_score']
            except ZeroDivisionError and KeyError:
                pass
    
    for url in page_score:
        answer[url]['match_score'] += page_score[url]['basic_score']
    
    print(answer)
    return answer[sorted(answer, key=lambda x:(-answer[x]['match_score'], answer[x]['index']))[0]]['index']

pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]
word = 'muzi'
print(solution(word, pages))