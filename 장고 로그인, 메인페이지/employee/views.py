import json

from django.shortcuts import render, redirect, get_object_or_404
from .forms import PersonForm
# Create your views here.
from django.http import HttpResponse
from .models import Userinfo
from django.views import generic
from django.template import loader
from django.views.decorators.csrf import csrf_exempt


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    if request.method == "POST" and 'edit' in request.POST:

        person = Userinfo.objects.get(user_num=request.POST['id'])
        person.user_name =request.POST['name']
        person.user_age = request.POST['age']
        person.user_position = request.POST['position']
        person.user_department = request.POST['department']
        person.save()
        return redirect('index')
    if request.method == "POST" and 'fire' in request.POST:

        person = Userinfo.objects.get(user_num=request.POST['id'])
        person.status=0
        person.save()
        return redirect('index')
    if request.method == "POST" and 'add' in request.POST:

        person = Userinfo()
        #person.id = Person.objects.last().id+1
        person.user_name = request.POST['name']
        person.user_age = request.POST['age']
        person.user_position = request.POST['position']
        person.user_department = request.POST['department']
        person.user_rank = request.POST['rank']
        person.status=1
        person.save()
        return redirect('index')
    person_list = Userinfo.objects.filter(status=1)
    # output=', '.join([q.이름 for q in person_list])
    # return HttpResponse(output)

    # template = loader.get_template('catalog/templates/index.html')
    context = {
        'person_list': person_list
    }
    return render(request, 'employee/index.html', {'person_list': person_list,'rank':request.session['user_rank']})

#
# def update(request):
#     # 수정하는 코드
#     person = Person.objects.get(id=id)
#     print("dd")
#     if request.method == 'POST':
#         form = PersonForm(request.POST)
#         person.이름 = form.cleaned_data['name']
#         person.나이 = form.cleaned_data['age']
#         person.직급 = form.cleaned_data['position']
#         person.부서 = form.cleaned_data['department']
#         person.save()
#     return redirect('catalog:index')

# def notice_edit_view(request, id):
#     notice = Notice.objects.get(id=id)
#
#     if request.method == "POST":
#         if (notice.writer == request.user or request.user.level == '0'):
#             form = NoticeWriteForm(request.POST, instance=notice)
#             if form.is_valid():
#                 notice = form.save(commit=False)
#                 notice.save()
#                 messages.success(request, "수정되었습니다.")
#                 return redirect('/notice/' + str(pk))
#     else:
#         notice = Notice.objects.get(id=pk)
#         if notice.writer == request.user or request.user.level == '0':
#             form = NoticeWriteForm(instance=notice)
#             context = {
#                 'form': form,
#                 'edit': '수정하기',
#             }
#             return render(request, "notice/notice_write.html", context)
#         else:
#             messages.error(request, "본인 게시글이 아닙니다.")
#             return redirect('/notice/' + str(pk))
#


# def edit(request, person_id):
#     person = Person.objects.get(id=person_id)
#     # 글을 수정사항을 입력하고 제출을 눌렀을 때
#     if request.method == "Confirm":
#          form= PersonEdit(request., request.FILES)
#         if form.is_valid():
#             print(form.cleaned_data)
#             # {'name': '수정된 이름', 'image': <InMemoryUploadedFile: Birman_43.jpg 	(image/jpeg)>, 'gender': 'female', 'body': '수정된 내용'}
#             person.이름 = form.cleaned_data['name']
#             person.나이 = form.cleaned_data['image']
#             person.부서 = form.cleaned_data['gender']
#             person.직급 = form.cleaned_data['body']
#             person.save()
#             return redirect('/detail/' + str(person.id))
#
#     # 수정사항을 입력하기 위해 페이지에 처음 접속했을 때
#     else:
#         form = PersonEdit()
#         return render(request, 'catalog/edit_person.html', {'form': form})
