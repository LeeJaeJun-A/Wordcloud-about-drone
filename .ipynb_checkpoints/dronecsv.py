from bs4 import BeautifulSoup
import urllib.request
import csv

#각 페이지 url 가져오기
pageurl = {'page1': 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EB%93%9C%EB%A1%A0',
'page2': 'https://search.naver.com/search.naver?&where=news&query=%EB%93%9C%EB%A1%A0&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&cluster_rank=19&start=11&refresh_start=0',
'page3': 'https://search.naver.com/search.naver?&where=news&query=%EB%93%9C%EB%A1%A0&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&cluster_rank=32&start=21&refresh_start=0',
'page4': 'https://search.naver.com/search.naver?&where=news&query=%EB%93%9C%EB%A1%A0&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&cluster_rank=51&start=31&refresh_start=0',
'page5': 'https://search.naver.com/search.naver?&where=news&query=%EB%93%9C%EB%A1%A0&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&cluster_rank=64&start=41&refresh_start=0',
'page6': 'https://search.naver.com/search.naver?&where=news&query=%EB%93%9C%EB%A1%A0&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&cluster_rank=79&start=51&refresh_start=0',
'page7': 'https://search.naver.com/search.naver?&where=news&query=%EB%93%9C%EB%A1%A0&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&cluster_rank=94&start=61&refresh_start=0',
'page8': 'https://search.naver.com/search.naver?&where=news&query=%EB%93%9C%EB%A1%A0&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&cluster_rank=112&start=71&refresh_start=0',
'page9': 'https://search.naver.com/search.naver?&where=news&query=%EB%93%9C%EB%A1%A0&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&cluster_rank=126&start=81&refresh_start=0',
'page10': 'https://search.naver.com/search.naver?&where=news&query=%EB%93%9C%EB%A1%A0&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&cluster_rank=141&start=91&refresh_start=0'}

#각 기사 url을 담을 리스트
url = []
Max_url = 100 
pagename = list(pageurl.values())

#각 기사의 url을 담기(100개)
while len(url) < Max_url:
    for i in pagename:
        html = urllib.request.urlopen(i).read() #
        soup = BeautifulSoup(html, 'html.parser')
        findurl = soup.find_all(class_='_sp_each_title')
        for q in findurl:
            box = [q.attrs['href']] #writerows를 쓰기 위해서 list형태로
            url.append(box)

#기사 url을 담은 리스트를 저장
f = open('NewsUrl.csv', 'w', newline="") #newline =""을 주지않으면, writerow(s)이후 줄바꿈 1줄이 자동으로 실행됨
writer = csv.writer(f)
writer.writerows(url)
f.close