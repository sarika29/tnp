from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^signin/$',views.signup,name="index"),
	url(r'^profile/$', views.profile, name='profile'),
	url(r'^index/$', views.main, name='profile'),
	url(r'^upcompany/$', views.upcompany, name='profile'),
	url(r'^addCompany/$', views.addCompany, name='addCompany'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

