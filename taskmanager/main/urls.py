from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('create', views.create, name='create'),
    path('all_tasks', views.all_tasks, name='all_tasks'),
    path('delete/<int:id>/', views.delete),
    path('error_404', views.error_404, name='error_404')
]
