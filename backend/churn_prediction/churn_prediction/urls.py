"""
URL configuration for churn_prediction project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# from .test import *
# from .main_views import *

# from .utils import check_header
from  .prediction import * 
from .test import *

from churn_prediction import main_views

urlpatterns = [
    path('bank/admin/', admin.site.urls),
    path('predict/',predict_churn),
    # path('',test.display),
    path('create/',create_user),
    path('login/',login_user),
    path('forget/',forgot_password),
    path('reset/',reset_password),
    path('verify/',verify_pin),
    path('bank/user/',(main_views.handle_user_information)),
    path('bank/churn/',(main_views.handle_churn_information)),
    # path('suggest/',speech)
]
