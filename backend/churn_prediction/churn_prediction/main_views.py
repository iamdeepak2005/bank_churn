from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from .utils import *
from .middleware import *
@csrf_exempt
@check_token
@method_decorator(csrf_exempt, name='dispatch')
def handle_user_information(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # Parse JSON input

            # Validate gender field
            gender = data.get('gender')
            if gender and len(gender) > 5:
                return JsonResponse({"error": "Gender field cannot exceed 5 characters"}, status=400)

            # Check if `user_id` exists in the input
            user_id = data.get('user_id')
            if user_id:
                # Update logic: Fetch the existing user and update fields
                user_info = UserInformation.objects.get(user_id=user_id)

                for field, value in data.items():
                    if hasattr(user_info, field) and field != "user_id":
                        setattr(user_info, field, value)
                user_info.save()
                return JsonResponse({"message": "User information updated successfully"}, status=200)
            else:
                # Create logic: Ensure the required fields are provided
                login_user_id = data.get("login_user_id")
                login_user = LoginUser.objects.get(login_user_id=login_user_id)  # Fetch LoginUser object

                user_info = UserInformation.objects.create(
                    login_user=login_user,
                    name=data.get('name'),
                    customer_age=data.get('customer_age'),
                    gender=gender,  # Already validated
                    dependent_count=data.get('dependent_count'),
                    education_level=data.get('education_level'),
                    marital_status=data.get('marital_status'),
                    income_category=data.get('income_category'),
                    card_category=data.get('card_category'),
                )
                return JsonResponse({"message": "User information created successfully", "user_id": user_info.user_id}, status=201)

        except UserInformation.DoesNotExist:
            return JsonResponse({"error": "User information with the given ID does not exist"}, status=404)
        except LoginUser.DoesNotExist:
            return JsonResponse({"error": "Login user not found"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    else:
        return JsonResponse({"error": "Invalid HTTP method"}, status=405)

@csrf_exempt
@check_token
@method_decorator(csrf_exempt, name='dispatch')
def handle_churn_information(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            # Validate that required fields are present
            required_fields = [
                'user_id', 'months_on_book', 'total_relationship_count',
                'credit_limit', 'total_revolving_bal', 'avg_open_to_buy',
                'total_amt_chng_q4_q1', 'total_trans_amt',
                'total_trans_ct', 'total_ct_chng_q4_q1',
                'avg_utilization_ratio'
            ]
            missing_fields = [field for field in required_fields if field not in data]
            if missing_fields:
                return JsonResponse({"error": f"Missing fields: {', '.join(missing_fields)}"}, status=400)

            # Get related UserInformation instance
            user = UserInformation.objects.get(user_id=data['user_id'])

            # Create new ChurnInformation instance
            churn_info = ChurnInformation.objects.create(
                user=user,
                attrition_flag=data.get('attrition_flag'),
                months_on_book=data['months_on_book'],
                total_relationship_count=data['total_relationship_count'],
                months_inactive_12_mon=data.get('months_inactive_12_mon'),
                contacts_count_12_mon=data.get('contacts_count_12_mon'),
                credit_limit=data['credit_limit'],
                total_revolving_bal=data['total_revolving_bal'],
                avg_open_to_buy=data['avg_open_to_buy'],
                total_amt_chng_q4_q1=data['total_amt_chng_q4_q1'],
                total_trans_amt=data['total_trans_amt'],
                total_trans_ct=data['total_trans_ct'],
                total_ct_chng_q4_q1=data['total_ct_chng_q4_q1'],
                avg_utilization_ratio=data['avg_utilization_ratio']
            )

            return JsonResponse({"message": "Churn information created successfully", "id": churn_info.id}, status=201)

        except UserInformation.DoesNotExist:
            return JsonResponse({"error": "User not found"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    elif request.method == 'PUT':
        try:
            data = json.loads(request.body)

            # Validate that ID is provided
            churn_id = data.get('id')
            if not churn_id:
                return JsonResponse({"error": "Churn information ID is required for update"}, status=400)

            # Fetch existing ChurnInformation instance
            churn_info = ChurnInformation.objects.get(id=churn_id)

            # Update fields if provided
            for field in [
                'attrition_flag', 'months_on_book', 'total_relationship_count',
                'months_inactive_12_mon', 'contacts_count_12_mon',
                'credit_limit', 'total_revolving_bal', 'avg_open_to_buy',
                'total_amt_chng_q4_q1', 'total_trans_amt',
                'total_trans_ct', 'total_ct_chng_q4_q1',
                'avg_utilization_ratio'
            ]:
                if field in data:
                    setattr(churn_info, field, data[field])

            # Save the updated instance
            churn_info.save()
            return JsonResponse({"message": "Churn information updated successfully"}, status=200)

        except ChurnInformation.DoesNotExist:
            return JsonResponse({"error": "Churn information not found"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)