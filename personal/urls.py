from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import login, logout

app_name = "personal"
urlpatterns = [
    url(r'', views.after_login, name='after_login'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.logout, name='log_out'),
    #url(r'^next/$', views.home, name="next"),

]
