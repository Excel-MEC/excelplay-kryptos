from django.middleware.csrf import get_token
from django.http import JsonResponse

def set_cookies(view_func):
    def new_view_func(request):
        decorated_func = view_func(request)
        if 'csrftoken' not in request.COOKIES:
            decorated_func.set_cookie('csrftoken', get_token(request), 2592000)
        
        return decorated_func
    return new_view_func


def is_logged_in(view_func):
    """
    This decorator checks whether the request comes from an authenticated user,
    If yes, returns to the view function, else returns an error response.
    """

    def new_view_func(request):
        if request.session.get('logged_in', False):
            return view_func(request)
        else:
            return JsonResponse({'error' : 'User not logged in'})
    return new_view_func
