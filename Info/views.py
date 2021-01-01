from __future__ import unicode_literals
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from django.http import Http404
from django.views import generic
from .models import Genome,Residue,result,files,user_uploads
from .forms import user_form
from django.db.models import Q
from django.http import FileResponse



def front(request):
    return render(request,'Info/homepg.html')


def hlp(request):
    return render(request, 'Info/help.html')


def contk(request):
    return render(request, 'Info/contacts.html')


class IndexView(generic.ListView):
    template_name = 'Info/index.html'

    def get_queryset(self):
        return Genome.objects.all()


def delta(request,name):
    album = get_object_or_404(Genome, pk=name)
    return render(request, 'Info/extra.html', {'album':album})


def detail(request,Mutation):
    a=Mutation
    x = get_object_or_404(result, Mutation=a)
    return render(request,'Info/detail.html',{'x':x})

def sheet(request,id):

    m = get_object_or_404(files,pk =id) 

    filenam = settings.MEDIA_ROOT + '/'+ str(m.fil)
    print (filenam)

    try:
        return FileResponse(open(filenam, 'rb'), content_type='application/vnd.ms-excel')
    except FileNotFoundError:
        raise Http404()


def downl(request):

    f = files.objects.all()

    print (f)

    return render(request,'Info/downloadpg.html',{'f':f})

IMAGE_FILE_TYPES = ['xlsx']
def upload(request):
    x = user_uploads.objects.all()
    form = user_form()
    if request.method == 'POST':
        form = user_form(request.POST, request.FILES)
        if form.is_valid():
            user_pr = form.save(commit=False)
            user_pr.file = request.FILES['file']
            file_type = user_pr.file.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                return redirect('Info:upload')
            user_pr.save()
            x = user_uploads.objects.all()
            print (x)
            return render(request,'Info/success.html',{'x':x})
    context = {"form":form,"x":x}
    return render(request, 'Info/uploadpg.html', context)    
 