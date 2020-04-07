'''
@Author: 华豪
@Date: 2019-12-10 21:38:56
@E-Mail: hh@huahaohh.cn
@LastEditors: 华豪
@LastEditTime: 2020-04-07 17:27:08
'''
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from django.views.decorators.csrf import csrf_exempt
import django.utils.timezone as timezone
from user.models import user

from china.models import china
from international.models import international
from entertainment.models import entertainment
from sports.models import sports
from technology.models import technology
from military.models import military

import smtplib
from email.mime.text import MIMEText
from email.header import Header
import random
from itertools import chain


# Create your views here.
def user_news(request):
    if request.method == "GET":
        username = request.session.get("username")
        if username:
            china_count = user.objects.filter(username=username)[0].china_count
            international_count = user.objects.filter(username=username)[0].international_count
            entertainment_count = user.objects.filter(username=username)[0].entertainment_count
            sport_count = user.objects.filter(username=username)[0].sport_count
            technology_count = user.objects.filter(username=username)[0].technology_count
            military_count = user.objects.filter(username=username)[0].military_count

            total_count = china_count + international_count + entertainment_count + sport_count + technology_count + military_count
            if total_count <= 10:
                china_count = 2
                international_count = 2
                entertainment_count = 2
                sport_count = 2
                technology_count = 1
                military_count = 1

                total_count = 10
                flag = False
            else:
                flag = True

            china_count = int(china_count/total_count * 20)
            international_count = int(international_count/total_count * 20)
            entertainment_count = int(entertainment_count/total_count * 20)
            sport_count = int(sport_count/total_count * 20)
            technology_count = int(technology_count/total_count * 20)
            military_count = int(military_count/total_count * 20)

            if flag:
                total_count = china_count + international_count + entertainment_count + sport_count + technology_count + military_count

            china_news = china.objects.filter(abs_titles="latest_news").order_by("?")
            international_news = international.objects.filter(abs_titles="latest_news").order_by('?')
            entertainment_news = entertainment.objects.filter(abs_titles="latest_news").order_by("?")
            sports_news = sports.objects.filter(abs_titles="latest_news").order_by("?")
            technology_news = technology.objects.filter(abs_titles="latest_news").order_by("?")
            military_news = military.objects.filter(abs_titles="latest_news").order_by("?")
            # print(china_news,123)
            china_news = list(china_news[:china_count])
            international_news = list(international_news[:international_count])
            entertainment_news = list(entertainment_news[:entertainment_count])
            sports_news = list(sports_news[:sport_count])
            technology_news = list(technology_news[:technology_count])
            military_news = list(military_news[:military_count])
            # print(china_news,sports_news,666)
            total_news = china_news + international_news + entertainment_news + sports_news + technology_news + military_news
            total_news = random.sample(total_news,total_count)

            # 关键词
            count_list = [china_count, international_count, entertainment_count, sport_count, technology_count, military_count]
            keyword_list = ["国内","国际","娱乐","体育","科技","军事"]

            keyword_index = count_list.index(max(count_list))
            keyword = keyword_list[keyword_index]

            contex={
                'total_news': total_news,
                'username': username,
                'keyword': keyword,
            }
            return render(request,"user.html",contex) 
        else:
            return HttpResponseRedirect("/login")

@csrf_exempt
def register(request):
    if request.method == "GET":
        return render(request,"register.html") 
    elif request.method == "POST":
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        code = request.POST.get("code")

        data = {
        'err':0,
        'err2':0,
        'err3':0
        }

        user_list = user.objects.all().values_list('email','username')

        for tu in user_list:
            if email == tu[0]:
                data["err"] = 1
                return JsonResponse(data)
            elif username == tu[1]:
                data["err2"] = 1
                return JsonResponse(data)
        if code:
            if request.session.get("verify_code") == int(code):
                user.objects.create(email=email,username=username,password=password)
                return JsonResponse(data)
            else:
                data["err3"] = 1
                return JsonResponse(data)
        else:
            return JsonResponse(data)

def check_uname(request):
    email = request.GET["email"]
    username = request.GET["username"]

    data = {
        'err':0,
        'err2':0
        }

    email_list = user.objects.all().values_list('email')
    user_list = user.objects.all().values_list('username')

    for l in email_list:
        if email in l[0]:
            data['err'] = 1
    for l in user_list:
        if username in l[0]:
            data['err2'] = 1
    return JsonResponse(data)

@csrf_exempt
def send_code(request):
    email = request.POST["email"]
    print(email)
    data = {
        'err':1,
        'desc': "请重新发送!"
        }
    verify_code = send_email(email)
    if(verify_code):
        request.session["verify_code"] = verify_code
        print(request.session.get("verify_code"))
        data["err"] = 0

    return JsonResponse(data)

def send_email(email):
    sender = 'hh@huahaohh.cn'
    receiver = email
    subject = '验证码'
    smtpserver = 'smtp.qq.com'
    email = 'hh@huahaohh.cn'
    password = 'pyopnsannicfbeca'

    s = str(random.randint(100000,999999))
    s2 = "您的验证码为：" + s

    try:
        msg = MIMEText(s2,'plain','utf-8')#中文需参数‘utf-8'，单字节字符不需要
        msg['Subject'] = Header(subject, 'utf-8')
        msg['From'] = 'hh<hh@huahaohh.cn>'  
        msg['To'] = "<%s>"%email

        smtp = smtplib.SMTP_SSL(smtpserver,port=465)
        smtp.connect('smtp.qq.com')
        smtp.login(email, password)
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()
        print("发送验证码成功")
    except:
        return False
    return int(s)

def login(request):
    if request.method == "GET":
        return render(request,"login.html") 
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        data = {
            "err":1
            }
        user_list1 = user.objects.all().values_list('username','password')

        for tu in user_list1:
            if username == tu[0] and password == tu[1]:
                request.session["username"] = username
                data["err"] = 0

                user.objects.filter(username=username).update(last_login_time=timezone.now())
                return JsonResponse(data)

        return JsonResponse(data)

def log_out(request):
    del request.session['username']
    return HttpResponseRedirect("/")

def china_count(request):
    count = request.POST.get("china_count")
    data = {"err":0}

    username = request.session.get("username")
    china_count = user.objects.filter(username=username)[0].china_count
    user.objects.filter(username=username).update(china_count=china_count+1)

    return JsonResponse(data)

def international_count(request):
    count = request.POST.get("international_count")
    data = {"err":0}

    username = request.session.get("username")
    international_count = user.objects.filter(username=username)[0].international_count
    user.objects.filter(username=username).update(international_count=international_count+1)

    return JsonResponse(data)

def entertainment_count(request):
    count = request.POST.get("entertainment_count")
    data = {"err":0}

    username = request.session.get("username")
    entertainment_count = user.objects.filter(username=username)[0].entertainment_count
    user.objects.filter(username=username).update(entertainment_count=entertainment_count+1)

    return JsonResponse(data)

def sport_count(request):
    count = request.POST.get("sport_count")
    data = {"err":0}

    username = request.session.get("username")
    sport_count = user.objects.filter(username=username)[0].sport_count
    user.objects.filter(username=username).update(sport_count=sport_count+1)

    return JsonResponse(data)

def technology_count(request):
    count = request.POST.get("technology_count")
    data = {"err":0}

    username = request.session.get("username")
    technology_count = user.objects.filter(username=username)[0].technology_count
    user.objects.filter(username=username).update(technology_count=technology_count+1)

    return JsonResponse(data)

def military_count(request):
    count = request.POST.get("military_count")
    data = {"err":0}

    username = request.session.get("username")
    military_count = user.objects.filter(username=username)[0].military_count
    user.objects.filter(username=username).update(military_count=military_count+1)

    return JsonResponse(data)
