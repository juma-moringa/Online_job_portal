from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.urls import path

urlpatterns=[
    url(r'^$',views.index, name='index'),
    path('landingpage/',views.landingpage,name = 'landingpage'),
    path('client_register/',views.client_register.as_view(),name = 'client_register'),
    path('employer_register/',views.employer_register.as_view(),name = 'employer_register'),
    path('login/',views.login_request,name = 'login'),
    path('logout/',views.logout_request,name = 'logout'),
    path('apply/',views. applyLinkup, name='apply'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)