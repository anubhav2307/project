from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.http import Http404
from django.views import generic
from .models import Genome,Residue,result
from django.db.models import Q


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
    x = result.objects.get(Mutation=a)
    return render(request,'Info/detail.html',{'x':x})
