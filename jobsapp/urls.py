from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.urls import path

urlpatterns=[
    path('',views.login_request,name = 'index'),
    # url(r'^$',views.index, name='index'),
    path('client_register/',views.client_register.as_view(),name = 'client_register'),
    path('garage_register/',views.employer_register.as_view(),name = 'employer_register'),
    path('login/',views.login_request,name = 'login'),
    path('landingpage/',views.landingpage,name = 'landingpage'),
  
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)