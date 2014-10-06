from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api
from italianTurkish.api import ItemResource, TopicResource

v1_api = Api(api_name='v1')
v1_api.register(ItemResource())
v1_api.register(TopicResource())

urlpatterns = patterns('',

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^api/', include(v1_api.urls)),

)
