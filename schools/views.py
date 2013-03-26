
from django.shortcuts import render
from django.http import HttpResponse

def list_schools(request):
    return render(request, 'schools/list.html')
