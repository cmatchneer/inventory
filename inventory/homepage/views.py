from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homepage_view(request,*args, **kwargs):
    test={
        "count":[1,2,3,4,5,6],
        "word":"testing"
    }
    return render(request,"home.html",test)
