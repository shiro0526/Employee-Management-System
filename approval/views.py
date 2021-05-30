from django.shortcuts import render
def index(request):
    return render(request,'approval/index.html')
# Create your views here.