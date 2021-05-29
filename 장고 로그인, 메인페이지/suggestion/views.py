from django.shortcuts import render
def index(request):
    return render(request,'suggestion/index.html',{'hi':'django test'})
# Create your views here.
