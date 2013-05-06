from django.conf.urls.defaults import *
import django.views.generic.list_detail
from django.contrib.auth.decorators import login_required

from kn.redirection import views

urlpatterns = patterns('',
    url(r'(?P<redirecturl>[a-zA-Z0-9._~-]+)?$',
        views.redirection_to, name='redirect'),
)

# vim: et:sta:bs=2:sw=4:
