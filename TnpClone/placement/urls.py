from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

<<<<<<< HEAD
url(r'^signin/$',views.signup,name="index"),
]
=======
urlpatterns = [
	url(r'^signin/$',views.signin,name="index"),
	url(r'^profile/$', views.profile, name='profile'),
]
>>>>>>> 31c4604744205ac0caf2eeb5d7ed15073d5c135c
