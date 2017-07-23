import time

from django.shortcuts import render
from django.http import HttpResponse 


def form(request):
  path = 'app.js'
  now = time.time()
  return render(request, 'form.html', {'component': path, 'time': now})
