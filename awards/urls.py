from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
      url('^$',views.index,name = 'index'),
      url(r'^profile/$',views.profile,name='profile') ,
      url(r'^update-profile/$',views.update,name='update-profile') ,
      url(r'^upload/$',views.upload,name='upload'),
      url(r'^api/merch/$', views.ProjectList.as_view())
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)