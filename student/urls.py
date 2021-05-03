from django.contrib import admin
from . import views
from django.urls import path,include
from django.conf import settings
from django.conf import settings
from django.conf.urls.static import static



app_name='student'

urlpatterns = [
    path('home/', views.studenthome,name='home'),
    path('viewcertificate/',views.viewcertificate,name='viewcertificate'),
    path('exam/', include('exam.urls')),
    path('result/',views.resultview,name='result'),
    path('fee/',views.feeview,name='fee')

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)