from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/(.*)', admin.site.root),
    (r'^$', 'bookmark.views.index'),
    (r'^jqdjangogrid/', include('jqdjangogrid.urls')),
)

from django.conf import settings
urlpatterns += patterns('',
    (r'^media/(.*)', 'django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
)
