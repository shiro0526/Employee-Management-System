
from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
from django.http import HttpResponse
from .models import Suggestion,Userinfo
from django.views import generic
from django.template import loader
from django.views.decorators.csrf import csrf_exempt


def index(request):
    """View function for home page of site."""
    suggest_reciever_list = []
    allow_reciever_list = []
    denined_reciever_list = []


    # Generate counts of some of the main objects
    approved_suggestion_list = Suggestion.objects.filter(status=1,sender=request.session['user_num'])
    suggestion_list = Suggestion.objects.filter(status=0,sender=request.session['user_num'])
    disapproved_suggestion_list = Suggestion.objects.filter(status=-1,sender=request.session['user_num'])



    print()
    # output=', '.join([q.이름 for q in person_list])
    # return HttpResponse(output)

    # template = loader.get_template('catalog/templates/index.html')
    context = {
        #'list': personlist,
        'suggestion_list': suggestion_list,
        'approved_suggestion_list': approved_suggestion_list,
        'disapproved_suggestion_list': disapproved_suggestion_list
    }
    return render(request, 'approvalcheck/index.html',
                  {'suggestion_list': suggestion_list,
                   'approved_suggestion_list': approved_suggestion_list,
                   'disapproved_suggestion_list': disapproved_suggestion_list}
                  )