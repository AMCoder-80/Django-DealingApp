from django.http import HttpResponseRedirect
from django.shortcuts import reverse


class UnAuthenticatedUserMixin:

    def dispatch(self, request, *args, **kwargs): # noqa
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('account:profile'))
        return super().dispatch(request, *args, **kwargs)