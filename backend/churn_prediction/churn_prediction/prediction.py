import joblib
from django.shortcuts import render
from django.http import JsonResponse
import numpy as np
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def predict_churn(request):
    if request.method == 'POST':
        # Load the trained model and scaler from joblib files
        model = joblib.load(r"C:\Users\deepa\asan_innovations\backend\random_forest_model.joblib")  # Update path accordingly
        scaler = joblib.load(r"C:\Users\deepa\asan_innovations\backend\scaler.joblib")  # Update with the correct scaler path

        try:
            # Extract the JSON data from the request body
            data = json.loads(request.body)

            # List of all required fields
            required_fields = [
                'customer_age', 'gender', 'dependent_count', 'education_level', 'marital_status', 'income_category',
                'card_category', 'months_on_book', 'total_relationship_count', 'months_inactive_12_mon',
                'contacts_count_12_mon', 'credit_limit', 'total_revolving_bal', 'avg_open_to_buy', 
                'total_amt_chng_q4_q1', 'total_trans_amt', 'total_trans_ct', 'total_ct_chng_q4_q1', 
                'avg_utilization_ratio'
            ]
            
            # Check if any required field is missing and return an error message
            for field in required_fields:
                value = data.get(field)
                if value is None:
                    return JsonResponse({'error': f'Missing value for {field}'}, status=400)

            # Convert fields to appropriate data types
            try:
                data['customer_age'] = float(data['customer_age'])
                data['dependent_count'] = int(data['dependent_count'])
                data['months_on_book'] = int(data['months_on_book'])
                data['total_relationship_count'] = int(data['total_relationship_count'])
                data['months_inactive_12_mon'] = int(data['months_inactive_12_mon'])
                data['contacts_count_12_mon'] = int(data['contacts_count_12_mon'])
                data['credit_limit'] = float(data['credit_limit'])
                data['total_revolving_bal'] = float(data['total_revolving_bal'])
                data['avg_open_to_buy'] = float(data['avg_open_to_buy'])
                data['total_amt_chng_q4_q1'] = float(data['total_amt_chng_q4_q1'])
                data['total_trans_amt'] = float(data['total_trans_amt'])
                data['total_trans_ct'] = int(data['total_trans_ct'])
                data['total_ct_chng_q4_q1'] = float(data['total_ct_chng_q4_q1'])
                data['avg_utilization_ratio'] = float(data['avg_utilization_ratio'])
            except ValueError as e:
                return JsonResponse({'error': f'Invalid value format: {str(e)}'}, status=400)

            # Map categorical features to their corresponding numerical values
            data['gender'] = 0 if data['gender'] == 'Female' else 1  # Male -> 1, Female -> 0
            data['education_level'] = {
                'Graduate': 6,
                'College': 5,
                'High School': 4,
                'Post-Graduate': 3,
                'Doctorate': 2,
                'Unknown': 1,
                'Uneducated': 0
            }.get(data['education_level'], -1)  # Default to -1 for unknown
            data['marital_status'] = {
                'Married': 3,
                'Single': 2,
                'Unknown': 1,
                'Divorced': 0
            }.get(data['marital_status'], -1)  # Default to -1 for unknown
            data['income_category'] = {
                'Less than $40K': 1,
                '$40K - $60K': 2,
                '$80K - $120K': 3,
                '$60K - $80K': 4,
                '$120K +': 5,
                'Unknown': 0
            }.get(data['income_category'], -1)  # Default to -1 for unknown
            data['card_category'] = {
                'Blue': 0,
                'Silver': 1,
                'Gold': 2,
                'Platinum': 3
            }.get(data['card_category'], -1)  # Default to -1 for unknown

            # Prepare the features in the same order as the model expects
            encoded_data = [
                data['gender'],
                data['education_level'],
                data['marital_status'],
                data['income_category'],
                data['card_category'],
                data['customer_age'],
                data['dependent_count'],
                data['months_on_book'],
                data['total_relationship_count'],
                data['months_inactive_12_mon'],
                data['contacts_count_12_mon'],
                data['credit_limit'],
                data['total_revolving_bal'],
                data['avg_open_to_buy'],
                data['total_amt_chng_q4_q1'],
                data['total_trans_amt'],
                data['total_trans_ct'],
                data['total_ct_chng_q4_q1'],
                data['avg_utilization_ratio']
            ]

            # Convert the input data to a 2D array for prediction (required format)
            input_data = [encoded_data]

            # Scale the data using the pre-loaded scaler
            scaled_data = scaler.transform(input_data)

            # Predict using the trained model
            prediction = model.predict(scaled_data)

            # Return the prediction as a JSON response

            # Ensure the prediction is a regular Python data type (int or float)
            prediction_value = int(prediction[0]) if isinstance(prediction[0], (np.int64, np.float64)) else prediction[0]

            # Return the prediction as a JSON response
            return JsonResponse({'prediction': prediction_value})

        except Exception as e:
            return JsonResponse({'error': f'Error occurred: {str(e)}'}, status=400)

    else:
        return JsonResponse({'error': 'Only POST method is allowed.'}, status=405)
