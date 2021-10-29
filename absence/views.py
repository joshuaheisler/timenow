from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from absence.models import Absence

# Handler für Views
@login_required
def index(request):
    absence_list = Absence.objects.filter(user=request.user)
    context = {
        'absence_list': absence_list,
    }
    return render(request, 'absence/index.html', context)

@login_required
def history(request):
    return render(request, 'absence/history.html')

@login_required
def create(request):
    return render(request, 'absence/create.html')

@login_required
def approval(request):
    return render(request, 'absence/approval.html')

@login_required
def detail(request, absence_id):
    absence = Absence.objects.get(pk=absence_id)
    if absence.user == request.user:
        context = {
            'absence': absence,
        }
        return render(request, 'absence/detail.html')
    else:
        return redirect('absence:dashboard')

# Handler für Logik-URLs
@login_required
def approve(request, absence_id):
    return redirect('absence approve')

@login_required
def decline(request, absence_id):
    return redirect('absence decline')