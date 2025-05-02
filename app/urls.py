from firstapp import views
from django.urls import path, re_path

urlpatterns = [
    path('', views.index, name='home'),
    re_path('about/*', views.about, name='about', kwargs={'name': 'tom', "age": 100}),
    re_path('support/*', views.support, name='support'),
]

