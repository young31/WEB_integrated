import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=870').json()

really_real = sorted([res['drwtNo1'], res['drwtNo2'],res['drwtNo3'], res['drwtNo4'], res['drwtNo5'], res['drwtNo6']])

print(really_real)