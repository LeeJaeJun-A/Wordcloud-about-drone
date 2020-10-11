from bs4 import BeautifulSoup
import urllib.request
import csv

p = 1
#각 페이지 url 가져오기
pageurl = 'https://www.donga.com/news/search?p={0}&query=%EB%93%9C%EB%A1%A0&check_news=1&more=1&sorting=1&search_date=1&v1=&v2=&range=1'.format(p)
#p가 1에서 시작해서 15씩 늘어난다는 것으 알 수 있었음.

#각 기사 url을 담을 리스트
url = []
pageurlbox = []
Max_url = 150 
for n1 in range(10):  #10페이지니까
    pageurlbox.append(pageurl)
    p += 15

#각 기사의 url을 담기(100개)
while len(url) < Max_url:
    for i in pageurlbox:
        html = urllib.request.urlopen(i).read()
        soup = BeautifulSoup(html, 'html.parser')
        findurl = soup.find_all("p", class_ ="txt")
        for q in findurl:
            box = [q.find("a")["href"]] #writerows를 쓰기 위해서 list형태로
            url.append(box)

#기사 url을 담은 리스트를 저장
f = open('DongaNewsUrls.csv', 'w', newline="") #newline =""을 주지않으면, writerow(s)이후 줄바꿈 1줄이 자동으로 실행됨
writer = csv.writer(f)
writer.writerows(url)
f.close()
