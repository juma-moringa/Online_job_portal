from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.urls import path

urlpatterns=[
    path('', views.home, name='home'),
    url(r'^$',views.index, name='index'),
    url('login/',auth_views.LoginView.as_view(), name='login'),
    url('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    url('profile/',views.home, name='profile'), 
    path('apply/',views. applyLinkup, name='apply'),
    path('addjob/',views. addjob, name='addjob'),
    path('about/',views. about, name='about'),
    path('landingpage/',views.landingpage,name = 'landingpage'),
    path('client_register/',views.client_register.as_view(),name = 'client_register'),
    path('employer_register/',views.employer_register.as_view(),name = 'employer_register'),
    path('login/',views.login_request,name = 'login'),
    path('logout/',views.logout_request,name = 'logout'),
    url('searched/', views.search_job, name='search'),
    url(r'^ajax/newsletter/$', views.newsletter, name='newsletter'),
    url('subscribe/',views.news_today,name='newsToday'),
  

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)