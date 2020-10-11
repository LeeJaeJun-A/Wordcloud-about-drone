import csv
import urllib.request
from bs4 import BeautifulSoup

#csv파일로부터 뉴스 url 읽어와서 리스트꼴로([[0],[1]..])
f = open("DongaNewsUrl.csv",'r')
reader = csv.reader(f)
urlbox = [row for row in reader]
f.close()

#본문 긁어오기
for i in range(len(urlbox)):
    url = urlbox[i][0]
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.find_all("h1", class_="title")
    print(title)