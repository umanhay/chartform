import time

from django.shortcuts import render
from django.http import HttpResponse 


def form(request):
  path = 'form.js'
  return render(request, 'form.html', {'component': path})

def chart(request):
  path = 'chart.js'
  return render(request, 'chart.html', {'component': path})
