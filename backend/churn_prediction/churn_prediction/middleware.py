from django.http import JsonResponse, HttpResponseForbidden
from django.utils import timezone
from .models import LoginUser

def check_token(func):
    def wrapper(request, *args, **kwargs):
        # Retrieve the token and user_id from the headers
        token = request.headers.get('Authorization')
        user_id = request.headers.get('User-ID')

        if not token or not user_id:
            return JsonResponse({"error": "Token or User-ID is missing"}, status=401)

        # Remove 'Bearer ' from the token if it exists
        if token.startswith('Bearer '):
            token = token[7:]

        try:
            # Get the user associated with the user_id
            user = LoginUser.objects.get(login_user_id=user_id)

            # Check if the token matches the one in the database for that user
            if user.token != token:
                return HttpResponseForbidden("Access Denied: Invalid token for this user")

            # Check if token has expired (for example, if it's older than 20 minutes)
            if user.token_expiration and user.token_expiration < timezone.now():
                return HttpResponseForbidden("Access Denied: Token has expired")

            # Attach the user to the request object
            request.user = user

            # Proceed with the wrapped view function
            return func(request, *args, **kwargs)

        except LoginUser.DoesNotExist:
            return HttpResponseForbidden("Access Denied: Invalid user ID or token")

    return wrapper
