from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^signin/$',views.signup,name="index"),
	url(r'^index/$', views.main, name='profile'),
	url(r'^upcompany/$', views.upcompany, name='profile'),
	url(r'^addCompany/$', views.addCompany, name='addCompany'),
	url(r'^index/$', views.main, name='main'),
	url(r'^login/$', views.signin, name='login'),
	url(r'^$', views.home, name='home'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

