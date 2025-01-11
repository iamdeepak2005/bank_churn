# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ChurnInformation(models.Model):
    user = models.ForeignKey('UserInformation', models.DO_NOTHING)
    attrition_flag = models.IntegerField(blank=True, null=True)
    months_on_book = models.IntegerField()
    total_relationship_count = models.IntegerField()
    months_inactive_12_mon = models.IntegerField(blank=True, null=True)
    contacts_count_12_mon = models.IntegerField(blank=True, null=True)
    credit_limit = models.FloatField()
    total_revolving_bal = models.FloatField()
    avg_open_to_buy = models.FloatField()
    total_amt_chng_q4_q1 = models.FloatField()
    total_trans_amt = models.FloatField()
    total_trans_ct = models.IntegerField()
    total_ct_chng_q4_q1 = models.FloatField()
    avg_utilization_ratio = models.FloatField()

    class Meta:
        managed = False
        db_table = 'churn_information'


class LoginUser(models.Model):
    login_user_id = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=100)
    email = models.CharField(unique=True, max_length=255)
    password_hash = models.CharField(max_length=255)
    reset_pin = models.CharField(max_length=4, blank=True, null=True)
    pin_expiration = models.DateTimeField(blank=True, null=True)
    token = models.CharField(max_length=256, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    token_expiration = models.DateTimeField(blank=True, null=True)  # New field to store expiration time

    class Meta:
        managed = False
        db_table = 'login_user'


class UserInformation(models.Model):
    user_id = models.AutoField(primary_key=True)
    login_user = models.ForeignKey(LoginUser, models.DO_NOTHING)
    name = models.CharField(max_length=100)
    customer_age = models.IntegerField()
    gender = models.CharField(max_length=10)
    dependent_count = models.IntegerField(blank=True, null=True)
    education_level = models.CharField(max_length=11)
    marital_status = models.CharField(max_length=8)
    income_category = models.CharField(max_length=15)
    card_category = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'user_information'
