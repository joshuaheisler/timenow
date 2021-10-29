from django.urls import path

from . import views

app_name = 'times'
urlpatterns = [
    path('', views.index, name='dashboard'),
    path('history', views.history, name="history")
    # path('api/', views.api, name='api')
]