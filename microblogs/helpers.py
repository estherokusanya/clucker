from django.conf import settings
from django.shortcuts import redirect

def login_prohibited(view_function):
    def modified_view_funtion(request):
        if request.user.is_authenticated:
            return redirect(settings.REDIREDCT__URL_WHEN_LOGGED_IN)
        else:
            return view_function(request)
    return modified_view_funtion