from django.urls import path, include
from . import views



app_name='exam'

urlpatterns = [
    path('',views.home,name='home'),
    path('examination/',views.exam,name='exam'),
    path('quesres/',views.quesres)
]
