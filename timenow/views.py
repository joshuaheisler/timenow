from django.shortcuts import render, redirect

# Handle für Aufrufe ohne Parameter
def index(request):
    return redirect('times_dashboard') if request.user.is_authenticated else redirect('login')

# Handle für Fehleranzeige
def error400(request, exception):
    return render(request, 'errors/400.html')

def error403(request, exception):
    return render(request, 'errors/403.html')

def error404(request, exception):
    return render(request, 'errors/404.html')

def error500(request):
    return render(request, 'errors/500.html')