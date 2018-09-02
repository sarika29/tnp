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
	url(r'^listcomp/$', views.listcomp, name='main'),
	url(r'^upcompany/$', views.upcompany, name='upcompany'),

	url(r'^login/$', views.signin, name='login'),
	url(r'^$', views.home, name='home'),
	url(r'^acceptcomp/(?P<compname>[A-Za-z0-9.,]+)/$', views.acceptcomp,name="acceptcomp/(?P<req>[A-Za-z0-9.,]+)"),
	url(r'^logout/$',views.logout_view,name="logout"),
	url(r'^applycomp/(?P<req>[A-Za-z0-9.,]+)/$', views.applycomp,name="applycomp"),
	url(r'^liststd/(?P<compname>[A-Za-z0-9.,]+)/$', views.liststd,name="stdlist"),
	url(r'^export/xls/(?P<compname>[A-Za-z0-9.,]+)/$', views.export_users_xls, name='export_users_xls'),
]	
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

