from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('generator/', views.generateKey, name='generateKey'),
    #path('alisa/', views.replyToAlisa, name='replyToAlisa'),
    path('test/', views.testAlice, name='testAlice'),
]
