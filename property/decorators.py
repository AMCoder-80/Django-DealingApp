from django.shortcuts import redirect


def anonymous_only(to_url):
    def outer(func):
        def wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return func(request, *args, **kwargs)
            else:
                return redirect(to_url)
        return wrapper
    return outer
