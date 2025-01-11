# from django.http import HttpResponseForbidden
# import json

# def check_header(expected_token):
#     def decorator(view_func):
#         def _wrapped_view(request, *args, **kwargs):
#             # Retrieve the Authorization header
#             auth_header = request.headers.get('Authorization')
            
#             # Check if the header exists and the token is correct
#             if not auth_header or not auth_header.startswith('Bearer '):
#                 return HttpResponseForbidden("Access Denied: Missing Authorization Header")
            
#             token = auth_header.split(' ')[1]  # Extract the token part
            
#             if token != expected_token:
#                 return HttpResponseForbidden("Access Denied: Invalid Token")
            
#             return view_func(request, *args, **kwargs)
        
#         return _wrapped_view
#     return decorator
