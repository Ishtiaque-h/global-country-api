from django.shortcuts import redirect


def login_required(function):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('core:login')
        return function(request, *args, **kwargs)
    return wrapper


