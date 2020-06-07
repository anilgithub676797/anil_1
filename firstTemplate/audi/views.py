from django.shortcuts import render
import datetime
import random
# Create your views here.

def audiView(request):
    d=datetime.datetime.now()

    mydict={"time":d,"name":rand(),"one":"ajay","two":"vijay"}


    return render(request,"audi/audi.html",context=mydict)

def rand():
    name=['anil','akash']
    l=random.choice(name)
    return l
