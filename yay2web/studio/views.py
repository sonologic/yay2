from time import time
from django.shortcuts import render
from django.http import HttpResponse
import json

from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    context = {}
    return render(request, 'studio/dashboard.html', context)

@login_required
def status(request):
    data = {
        't' : time(),
    }
    return HttpResponse(json.dumps(data), content_type="application/json")
