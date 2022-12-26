from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin
admin.autodiscover()

import webapp.views
import api.views


# Examples:
# url(r'^$', 'HseAlice.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webapp.urls')),
    path('api/', include('api.urls')),
]
