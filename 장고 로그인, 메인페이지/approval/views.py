from approval.models import Suggestion

from django.shortcuts import render, get_object_or_404, redirect
from suggestion.models import UploadFileModel
import mimetypes
import os
from django.http import HttpResponse,Http404
from urllib.parse import quote
import urllib
def index(request):
    
    suggestion_list = Suggestion.objects.filter(status=0,reciever=int(request.session['user_num']))

    return render(request,'approval/index.html',{'suggestion_list':suggestion_list,'rank':request.session['user_rank']})
# Create your views here.


def file_download_view(request, pk):
    upload_file = get_object_or_404(UploadFileModel, pk=pk)
    url = upload_file.file.url[1:]
    print(type(url))
    print(url)
    file_url = urllib.parse.unquote(url)
    if os.path.exists(file_url):
        with open(file_url, 'rb') as fh:
            # quote_file_url = urllib.parse.quote(file_url.encode('utf-8'))
            quote_file_url = urllib.parse.quote(upload_file.title.encode('utf-8'))
            response = HttpResponse(fh.read(), content_type=mimetypes.guess_type(file_url)[0])
            # response['Content-Disposition'] = 'attachment;filename*=UTF-8\'\'%s' % quote_file_url[29:]
            response['Content-Disposition'] = 'attachment;filename*=UTF-8\'\'%s' % quote_file_url
            return response
    raise Http404

def allow(request, filenum):
    approve_file = Suggestion.objects.get(num=filenum)
    approve_file.status = 1
    approve_file.save()
    suggestion_list = Suggestion.objects.filter(status=0,reciever=int(request.session['user_num']))
    return redirect('/approval/')

def denined(request,filenum):
    approve_file = Suggestion.objects.get(num=filenum)
    approve_file.status = -1
    approve_file.save()
    suggestion_list = Suggestion.objects.filter(status=0,reciever=int(request.session['user_num']))
    return redirect('/approval/')