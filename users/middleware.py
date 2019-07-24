from django.shortcuts import redirect
from django.http import HttpResponse
from django.urls import reverse
from urllib.parse import urlencode


class LoginRequiredMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    @staticmethod
    def process_view(request, view_func, view_args, view_kwargs):
        assert hasattr(request, 'user')
        if "admin" in request.path:
            if request.user.is_authenticated:
                if not request.user.is_staff:
                    return HttpResponse("<h1>403 Forbidden</h1>")
            else:
                base_url = reverse('login')
                query_string = urlencode({'next': request.path})
                url = '{}?{}'.format(base_url, query_string)
                return redirect(url)
        elif "login" in request.path:
            pass
        elif "profile" in request.path:
            if not request.user.is_authenticated:
                if "restaurant" in request.path:
                    base_url = reverse('rest-login')
                    query_string = urlencode({'next': request.path})
                    url = '{}?{}'.format(base_url, query_string)
                    return redirect(url)
                else:
                    base_url = reverse('login')
                    query_string = urlencode({'next': request.path})
                    url = '{}?{}'.format(base_url, query_string)
                    return redirect(url)
            else:
                if request.user.usertype.user_type == "user":
                    redirect('profile')
                else:
                    redirect('rest-profile')
        elif "restaurant" in request.path:
            if request.user.is_authenticated:
                if "user" == request.user.usertype.user_type:
                    return redirect('/')
                elif "register" in request.path:
                    return redirect('rest-home')
            elif "register" in request.path:
                pass
            else:
                base_url = reverse('rest-login')
                query_string = urlencode({'next': request.path})
                url = '{}?{}'.format(base_url, query_string)
                return redirect(url)
        elif request.path == "/":
            if request.user.is_authenticated:
                if request.user.usertype.user_type == "restaurant":
                    return redirect('restaurant/')
