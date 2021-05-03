from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf import settings
from django.conf.urls.static import static


app_name='Prince_Institute'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('login/',views.login_call,name='login'),
    path('logout/',views.logout_call,name='logout'),
    path('register/',views.register,name='register'),
    path('student/', include('student.urls')),
    path('submitfee/',views.submitfee,name='submitfee'),
    path('finalfee/',views.finalfee,name='finalfee'),
    path('gallery/',views.gallery),
    path('faculty/',views.faculty),
    path('courses/',views.courses),
    path('about/',views.about),
    path('contact/',views.contact)

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)