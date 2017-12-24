from django.conf.urls import include, url
from django.contrib import admin
from trips.views import hello_world
from trips.views import hello_world_name

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^hello/$', hello_world),
    url(r'^hello/(?P<text>.*)$', hello_world_name),

]


