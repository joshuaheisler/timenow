from django.urls import path

from . import views

app_name = 'absence'
urlpatterns = [
    path('', views.index, name='dashboard'),
    path('history', views.history, name="history"),
    path('create', views.create, name="create"),
    path('approval', views.approval, name="approval"),
    path('<int:absence_id>', views.detail, name="detail"),
    path('<int:absence_id>/approve', views.approve, name="approve"),
    path('<int:absence_id>/decline', views.decline, name="decline")
]