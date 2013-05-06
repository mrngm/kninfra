from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse
from django.template import RequestContext

import kn.redirection.entities as Es_red

def redirection_to(request, redirecturl):
    return render_to_response('redirection/redirect.html',
            {'redirect_to': Es_red.redirect_by_short(redirecturl),
             'redirect_from': redirecturl},
            context_instance=RequestContext(request))

# vim: et:sta:bs=2:sw=4:
