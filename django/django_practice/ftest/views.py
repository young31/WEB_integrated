from django.shortcuts import render
from datetime import datetime
import random
import requests
from bs4 import BeautifulSoup

def birth(request):
    return render(request, 'birth.html')

def lotto(request):
    real_num = [21, 25,30, 32, 40, 42]
    num_pool = list(range(1, 46))
    lottos = sorted(list(random.sample(num_pool, k=6)))
    context = {
        'nums': lottos,
        'real_nums': real_num,
    }
    return render(request, 'lotto.html', context)


def lotto_pick(request):
    return render(request, 'lotto_pick.html')
 

def lotto_result(request):
    nums = sorted(list(map(int, request.GET.get('nums').split( ))))
    real_lotto = [21, 25, 30, 32, 40, 42]
    res = requests.get('https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=870').json()
    really_real = sorted([res['drwtNo1'], res['drwtNo2'],res['drwtNo3'], res['drwtNo4'], res['drwtNo5'], res['drwtNo6']])

    context = {
        'nums': nums,
        'real': real_lotto,
        'really_real': really_real,
    }
    return render(request, 'lotto_result.html', context)



