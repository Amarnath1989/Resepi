from django.http import HttpResponseRedirect,Http404
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Resepi

# Create your views here.
#@login_required()
def index(request):
    resipies_list = Resepi.objects.all()
    context = {'resipies_list':resipies_list}
    return render (request,'myresipies/index.html',context)

def detail_new(request,id):
    try:
        resipies_list = Resepi.objects.get(id=id)
        context = {'resipies_list': resipies_list}
    except Resepi.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'myresipies/details_new.html', context)

def detail(request):
    resipies_list = Resepi.objects.all()
    context = {'resipies_list': resipies_list}
    return render(request, 'myresipies/detail.html',context)



def create_resepi(request):
    if request.method == 'POST':
        Resepi.objects.create(name= request.POST['name'],
                              ingredients=request.POST['ingredients'],
                              process = request.POST['process'],
                              image = request.POST['img']
                              )
        return HttpResponseRedirect(reverse('index', args=()))
    return render(request,'myresipies/create.html',{})
