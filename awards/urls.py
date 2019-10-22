from django.conf.urls import url
from . import views

urlpatterns=[
      url('^$',views.index,name = 'index'),
      url(r'^profile/$',views.profile,name='profile') ,
      url(r'^update-profile/$',views.update,name='update-profile') ,
]