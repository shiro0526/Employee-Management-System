from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Userinfo
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.
def index(request):
    if request.method == "POST":
        id = request.POST['id']
        pw = request.POST['password']

        if Userinfo.objects.filter(user_id=id, user_password=pw).exists():
        #    auth.login(request,user)
            user = Userinfo.objects.get(user_id=id)
            #print(user.user_name)
            request.session['user_id'] = id
            request.session['user_name'] = user.user_name
            request.session['user_num'] = user.user_num
            request.session['user_department'] = user.user_department # 부서
            request.session['user_rank'] = user.user_rank #  권한
            request.session['user_position'] = user.user_position # 직급
            return redirect('/main/')
        else:
            return render(request,'login/index.html',{'error':'아이디나 패스워드가 틀렸습니다'})
    else:
        return render(request,'login/index.html')
