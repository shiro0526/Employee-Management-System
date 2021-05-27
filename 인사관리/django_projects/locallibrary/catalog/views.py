from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Person
from django.views import generic
from django.template import loader

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects


    person_list = Person.objects.all()
    # output=', '.join([q.이름 for q in person_list])
    # return HttpResponse(output)

    #template = loader.get_template('catalog/templates/index.html')
    context = {
      'person_list': person_list
    }
    return render(request, 'catalog/index.html',{'person_list':person_list})

# class PersonListView(generic.ListView):
#     model = Person
#     context_object_name = 'persons_list'   # your own name for the list as a template variable
#     queryset = Person.objects.all()  # Person의 오브젝트다 갖고오기
#     template_name = 'persons/my_arbitrary_template_name_list.html'  # Specify your own template name/location
