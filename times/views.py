from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def index(request):
    return render(request, 'times/index.html')

@login_required
def history(request):
    return render(request, 'times/history.html')