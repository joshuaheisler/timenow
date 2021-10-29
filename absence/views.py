import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from absence.models import Absence as AbsenceModel
from absence.forms import AbsenceCreateForm, AbsenceDetailForm

# Handler für Views
@login_required
def index(request):
    absence_set = AbsenceModel.objects.filter(user=request.user, absence_from__gt=datetime.datetime.now())
    context = {
        'absence_set': absence_set,
    }
    return render(request, 'absence/index.html', context)

@login_required
def history(request):
    absence_set = AbsenceModel.objects.filter(user=request.user).order_by('-absence_from')
    context = {
        'absence_set': absence_set
    }
    return render(request, 'absence/history.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = AbsenceCreateForm(request.POST)

        if form.is_valid():
            absence = form.save(commit=False)
            absence.user = request.user
            absence.save()
            return redirect('absence:detail', absence.id)
    else:
        form = AbsenceCreateForm()
        context = {
            'form': form
        }
        return render(request, 'absence/create.html', context)

@login_required
def approval(request):
    return render(request, 'absence/approval.html')

@login_required
def detail(request, absence_id):
    absence = get_object_or_404(AbsenceModel, pk=absence_id)

    if absence.user == request.user:
        form = AbsenceDetailForm(instance=absence)

        context = {
            'absence': absence,
            'form': form
        }
        return render(request, 'absence/detail.html', context)
    else:
        return redirect('absence:dashboard')

# Handler für Logik-URLs
@login_required
def approve(request, absence_id):
    return redirect('absence approve')

@login_required
def decline(request, absence_id):
    return redirect('absence decline')