from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^signin/$',views.signin,name="index"),
	url(r'^profile/$', views.profile, name='profile'),
]