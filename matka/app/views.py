from django.shortcuts import render
from .models import Markets,table
##16c9f6
#16c9f6
# Create your views here.
def index(request):
    services = table.objects.all()

    return render(request,'index.html',{'market': services})

def jdforum(request):

    return render(request,'forum.html')
def login(request):
    return render(request,'login.html')
