from django.shortcuts import render
from django.http import HttpResponse
from testAapp.models import *
from django.contrib.sessions.models import Session
# from user_agents import parse
# Create your views here.
def index(request):
    check_login = request.session.get("Name")
    if check_login:
        return render(request,'good.html',{"name":request.session.get("Name")})
    else:
    # s = Session.objects.all()[0]
    # print(s.get_decoded())
        return render(request,"index.html")
    # if("name" in request.COOKIES):
    #     user_name = request.COOKIES['name']
    #     response = render(request,'good.html',{"name":user_name})
    #     return response


def login(request):
    account = request.POST["account"]
    password = request.POST["pwd"]
    user_data = User.objects.get(UserID=account)
    # check_account = User.objects.filter(UserID=account)
    # check_pwd = User.objects.filter("Password")
    if(account == user_data.UserID and password == user_data.Password):
        request.session["Name"] ="apple"
        response = render(request,'good.html',{"name":request.session['Name']})
        # response.set_cookie("name",user_data.Name)
        return response
    else:
        return render(request,"index.html")