from django.http import JsonResponse
# from churn_prediction import serializers
from django.core import serializers
import hashlib
from .models import *
import json
from django.views.decorators.csrf import csrf_exempt
import random
import smtplib
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime, timedelta
import uuid  # For generating a unique token
from django.utils import timezone

def display (request):
    data = LoginUser.objects.all()
    serialized_data = serializers.serialize('json', data)
    data_list = json.loads(serialized_data)
    return JsonResponse(data_list, safe=False)

def send_smtp_email(email: str, pin: str):
    from_email = "dkag709@gmail.com"
    password = "mgjq ljtk frir cvck"  # Use your app password here

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = email
    msg['Subject'] = 'Password Reset PIN'

    html_content = f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {{
            font-family: 'Arial', sans-serif;
            background-color: #f4f6f9;
            margin: 0;
            padding: 0;
        }}
        .email-container {{
            width: 100%;
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
            background-color: #ffffff;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }}
        .header {{
            text-align: center;
            background-color: #1d3557;
            padding: 20px;
            color: #ffffff;
            border-radius: 8px 8px 0 0;
        }}
        .header h1 {{
            margin: 0;
            font-size: 24px;
        }}
        .content {{
            padding: 20px;
        }}
        .content h2 {{
            color: #1d3557;
            font-size: 32px;
            text-align: center;
        }}
        .content p {{
            font-size: 16px;
            line-height: 1.6;
            color: #333;
        }}
        .footer {{
            text-align: center;
            font-size: 14px;
            color: #777;
            padding-top: 20px;
        }}
        .footer a {{
            color: #1d3557;
            text-decoration: none;
        }}
    </style>
</head>
<body>
    <div class="email-container">
        <div class="header">
            <h1>Bank Churn Prediction - Password Reset</h1>
        </div>
        <div class="content">
            <p>Dear Customer,</p>
            <p>We have received a request to reset your password. To proceed with the reset, please use the following 4-digit PIN:</p>
            <h2>{pin}</h2>
            <p>This PIN is valid for a limited time only. If you did not request a password reset, kindly ignore this email and no further action will be required.</p>
            <p>Thank you for trusting us with your banking needs. If you have any questions, feel free to contact our support team.</p>
        </div>
        <div class="footer">
            <p>For security purposes, please do not share your PIN with anyone.</p>
            <p>For assistance, visit our <a href="https://yourbank.com/support">support page</a>.</p>
        </div>
    </div>
</body>
</html>
'''

    msg.attach(MIMEText(html_content, 'html'))

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()  # Secure the connection
        server.login(from_email, password)
        server.sendmail(from_email, email, msg.as_string())





@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)

            # Get data from the parsed JSON
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')        
        if not username or not email or not password:
            return JsonResponse({"error": "All fields are required"}, status=400)
        
        # Hash the password using SHA256 or another hashing method
        password_hash = hashlib.sha256(password.encode()).hexdigest()

        # Create the new user and save to the database
        try:
            new_user = LoginUser(username=username, email=email, password_hash=password_hash)
            new_user.save()
            return JsonResponse({"message": "User created successfully"}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    
def generate_token():
    return str(uuid.uuid4())  # Generate a unique token

@csrf_exempt
def login_user(request):
    """Handle user login, validate credentials, and generate a token."""
    if request.method == 'POST':
        data = json.loads(request.body)

        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return JsonResponse({"error": "Username and password are required"}, status=400)

        try:
            # Fetch the user from the database
            user = LoginUser.objects.get(username=username)
            password_hash = hashlib.sha256(password.encode()).hexdigest()

            # Check if the provided password matches the stored hash
            if user.password_hash == password_hash:
                # Generate and set the token expiration (20 minutes from now)
                token_expiration = timezone.now() + timedelta(minutes=20)

                # Generate a new token
                new_token = generate_token()

                # Update the user's token and expiration in the database
                user.token = new_token
                user.token_expiration = token_expiration
                user.save()  # Save the new token and expiration time

                return JsonResponse({"message": "Login successful", "token": new_token}, status=200)
            else:
                return JsonResponse({"error": "Invalid username or password"}, status=400)
        except LoginUser.DoesNotExist:
            return JsonResponse({"error": "User does not exist"}, status=404)
    else:
        # Handle other methods (e.g., GET or PUT) with a 405 Method Not Allowed
        return JsonResponse({"error": "Method not allowed"}, status=405)# View to handle forgot password functionality
@csrf_exempt
def forgot_password(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        email = data.get('email')

        if not email:
            return JsonResponse({"error": "Email is required"}, status=400)

        try:
            user = LoginUser.objects.get(email=email)

            # Generate a 4-digit PIN for password reset
            pin = str(random.randint(1000, 9999))

            # Set the expiration time (15 minutes from now)
            expiration_time = datetime.now() + timedelta(minutes=15)

            # Store the PIN and expiration time in the user's record
            user.reset_pin = pin
            user.pin_expiration = expiration_time
            user.save()

            # Send the reset PIN to the user's email
            send_smtp_email(email, pin)

            return JsonResponse({"message": f"Password reset PIN sent to {email}"}, status=200)

        except LoginUser.DoesNotExist:
            return JsonResponse({"error": "User with this email does not exist"}, status=404)

# View to handle password reset functionality
@csrf_exempt
def reset_password(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        email = data.get('email')
        pin = data.get('pin')
        new_password = data.get('new_password')

        if not email or not pin or not new_password:
            return JsonResponse({"error": "All fields are required"}, status=400)

        try:
            user = LoginUser.objects.get(email=email)

            # Check if the PIN matches and is within the valid time range
            if user.reset_pin == pin and timezone.now() < user.pin_expiration:
                # Hash the new password
                password_hash = hashlib.sha256(new_password.encode()).hexdigest()

                # Update the user's password
                user.password_hash = password_hash
                user.reset_pin = None  # Clear the PIN after use
                user.pin_expiration = None  # Clear the expiration time
                user.save()

                return JsonResponse({"message": "Password reset successfully"}, status=200)
            else:
                return JsonResponse({"error": "Invalid or expired PIN"}, status=400)

        except LoginUser.DoesNotExist:
            return JsonResponse({"error": "User with this email does not exist"}, status=404)

# View to handle PIN verification (if needed)
@csrf_exempt
def verify_pin(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        email = data.get('email')
        pin = data.get('pin')

        if not email or not pin:
            return JsonResponse({"error": "All fields are required"}, status=400)

        try:
            user = LoginUser.objects.get(email=email)

            # Make datetime.now() timezone-aware (assuming your app uses timezone-aware datetimes)
            now = timezone.now()

            # Check if the PIN matches and is within the valid time range
            if user.reset_pin == pin and now < user.pin_expiration:
                return JsonResponse({"message": "PIN verified successfully"}, status=200)
            else:
                return JsonResponse({"error": "Invalid or expired PIN"}, status=400)

        except LoginUser.DoesNotExist:
            return JsonResponse({"error": "User with this email does not exist"}, status=404)
