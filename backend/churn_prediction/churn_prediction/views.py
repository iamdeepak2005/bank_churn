from rest_framework import viewsets
from models import LoginUser, UserInformation, ChurnInformation
from .serializers import LoginUserSerializer, UserInformationSerializer, ChurnInformationSerializer
import json



# ViewSet for LoginUser
class LoginUserViewSet(viewsets.ModelViewSet):
    queryset = LoginUser.objects.all()
    serializer_class = LoginUserSerializer

# ViewSet for UserInformation
class UserInformationViewSet(viewsets.ModelViewSet):
    queryset = UserInformation.objects.all()
    serializer_class = UserInformationSerializer

# ViewSet for ChurnInformation
class ChurnInformationViewSet(viewsets.ModelViewSet):
    queryset = ChurnInformation.objects.all()
    serializer_class = ChurnInformationSerializer


# def display_login_users(request){
#     data = LoginUser.objects.all()
#     serialized_data = serializers.serialize('json', data)
#     data_list = json.loads(serialized_data)
#     return JsonResponse(data_list, safe=False)
# }