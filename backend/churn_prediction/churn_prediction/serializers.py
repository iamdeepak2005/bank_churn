from rest_framework import serializers
from .models import LoginUser, UserInformation, ChurnInformation

class LoginUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginUser
        fields = ['login_user_id', 'username', 'email', 'password_hash']

class UserInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInformation
        fields = ['user_id', 'login_user_id', 'name', 'customer_age', 'gender', 'dependent_count', 'education_level', 'marital_status', 'income_category', 'card_category']

class ChurnInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChurnInformation
        fields = ['id', 'user_id', 'attrition_flag', 'months_on_book', 'total_relationship_count', 'months_inactive_12_mon', 'contacts_count_12_mon', 'credit_limit', 'total_revolving_bal', 'avg_open_to_buy', 'total_amt_chng_q4_q1', 'total_trans_amt', 'total_trans_ct', 'total_ct_chng_q4_q1', 'avg_utilization_ratio']
