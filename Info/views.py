from __future__ import unicode_literals
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.http import Http404
from django.views import generic
from .models import Genome,Residue,result,files
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

    filenam = settings.MEDIA_ROOT + str(m.fil)

    try:
        return FileResponse(open(filenam, 'rb'), content_type='application/vnd.ms-excel')
    except FileNotFoundError:
        raise Http404()


def downl(request):

    f = files.objects.all()

    print (f)

    return render(request,'Info/downloadpg.html',{'f':f})



 