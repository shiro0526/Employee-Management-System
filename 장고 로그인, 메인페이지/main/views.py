from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'main/index.html',{'name':request.session['user_name'],'department':request.session['user_department'],'rank':request.session['user_rank'],'position':request.session['user_position']})