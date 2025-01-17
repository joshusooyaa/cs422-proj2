from django.shortcuts import redirect

def anonymous_required(view_func):
    """Customer decorator to redirect a logged in user to dashboard page so
    they can't access the login page (or any other page that uses this decorator)
    """
    def wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('forecast:dashboard')
        else:
            return view_func(request, *args, **kwargs)
    return wrapped_view

