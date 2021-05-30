from suggestion.models import Suggestion, UploadFileModel
from login.models import Userinfo

from django.shortcuts import render, get_object_or_404, redirect

import mimetypes
import os
from django.http import HttpResponse,Http404
from urllib.parse import quote
import urllib

import base64
def index(request):
    employee_list = Userinfo.objects.all()
    if request.method=="POST":
        print(request.POST['title'])
        print(request.POST['people_array'])
      #  print(request.POST['file'])
        file = request.FILES['file']

        print(file)
        filename = file._name
        print(filename)
        file.chunks()

        people_list = str(request.POST['people_array'])
        people_list = people_list.split(',')
        upload_file = UploadFileModel()
        upload_file.file = file
        upload_file.title = filename
        upload_file.save()
        obj = Suggestion.objects.last()
        file_locate = int(obj.file_locate)+1
        for people in people_list:
            suggest = Suggestion()
            suggest.title = request.POST['title']
            suggest.sender = request.session['user_num']
            suggest.reciever = int(people.strip())
            suggest.sender_name = request.session['user_name']
            suggest.status = 0
            suggest.file = file
            suggest.file_locate = file_locate
            user = Userinfo.objects.get(user_num=suggest.reciever)
            suggest.reciever_name = user.user_name
            suggest.save()


        return render(request,'suggestion/index.html',{'employee_list':employee_list,'rank':request.session['user_rank']})
    else:
    #    employee_list = Userinfo.objects.all()

        return render(request,'suggestion/index.html',{'employee_list':employee_list,'rank':request.session['user_rank']})
# Create your views here.

def file_download_view(request, pk):
    upload_file = get_object_or_404(UploadFileModel, pk=pk)
    url = upload_file.upload_files.url[1:]
    print(type(url))
    print(url)
    file_url = urllib.parse.unquote(url)
    if os.path.exists(file_url):
        with open(file_url, 'rb') as fh:
            # quote_file_url = urllib.parse.quote(file_url.encode('utf-8'))
            quote_file_url = urllib.parse.quote(upload_file.filename.encode('utf-8'))
            response = HttpResponse(fh.read(), content_type=mimetypes.guess_type(file_url)[0])
            # response['Content-Disposition'] = 'attachment;filename*=UTF-8\'\'%s' % quote_file_url[29:]
            response['Content-Disposition'] = 'attachment;filename*=UTF-8\'\'%s' % quote_file_url
            return response
    raise Http404