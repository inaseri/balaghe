from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from tastypie.api import Api
from BalaghePWA.resource import LanguageResouce,TranslatorResouce,ContentResouce,SectionResouce
from BalaghePWA import views

v1_api = Api(api_name='v1')
v1_api.register(LanguageResouce())
v1_api.register(TranslatorResouce())
v1_api.register(ContentResouce())
v1_api.register(SectionResouce())
# v1_api.register(slider_androidResource())
# v1_api.register(LocationResource())

urlpatterns = [
    path('', views.index, name='index'),
    url(r'list/(?P<type>[0-9]){1}/',views.list, name='list'),
    url(r'content/(?P<contentID>[0-9]){1,3}/',views.contentView, name='content'),
    path('admin/', admin.site.urls),
    url(r'^api/', include(v1_api.urls)),
    url('', include('pwa.urls')),
]
