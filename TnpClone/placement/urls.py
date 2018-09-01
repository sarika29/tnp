from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^signin/$',views.signup,name="index"),
	url(r'^profile/$', views.profile, name='profile'),
	url(r'^index/$', views.main, name='main'),
	url(r'^upcompany/$', views.upcompany, name='upcompany'),
	url(r'^login/$', views.signin, name='login')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

