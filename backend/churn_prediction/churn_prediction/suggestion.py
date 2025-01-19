import json
import google.generativeai as genai
import os
from django.http import JsonResponse

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'CREDENTAILS_PATH_HERE'

# Define a well-structured and specific prompt for bank churn analysis
PROMPT_TEMPLATE = """
You are an AI analyst for a banking institution. Based on the following customer data, analyze the possible reasons for customer churn. Provide a detailed explanation for each factor and suggest strategies to mitigate churn:

Customer Data:
- Age: {customer_age}
- Number of Dependents: {dependent_count}
- Months as a Customer: {months_on_book}
- Total Relationships (Accounts/Services): {total_relationship_count}
- Months Inactive in the Last Year: {months_inactive_12_mon}
- Number of Contacts in the Last Year: {contacts_count_12_mon}
- Credit Limit: {credit_limit}
- Total Revolving Balance: {total_revolving_bal}
- Average Open-to-Buy Credit: {avg_open_to_buy}
- Change in Transaction Amount (Q4 to Q1): {total_amt_chng_q4_q1}
- Total Transaction Amount: {total_trans_amt}
- Total Transaction Count: {total_trans_ct}
- Change in Transaction Count (Q4 to Q1): {total_ct_chng_q4_q1}
- Average Utilization Ratio: {avg_utilization_ratio}

Based on this data, identify:
1. Key factors contributing to the likelihood of the customer exiting the bank.
2. Possible underlying causes for dissatisfaction or disengagement.
3. Specific actions the bank can take to retain this customer.

JSON Output Expected:
- Reasons for churn: (List)
- Suggested actions: (List)
"""

PROMPT_TEMPLATE1 = """
You are an AI analyst for a banking institution. Based on the following customer data, analyze the current engagement of the customer with the bank and provide strategies to retain them as a loyal customer. Provide a detailed explanation for each factor that requires attention and suggest actionable steps to enhance their experience:

Customer Data:
- Age: {customer_age}
- Number of Dependents: {dependent_count}
- Months as a Customer: {months_on_book}
- Total Relationships (Accounts/Services): {total_relationship_count}
- Months Inactive in the Last Year: {months_inactive_12_mon}
- Number of Contacts in the Last Year: {contacts_count_12_mon}
- Credit Limit: {credit_limit}
- Total Revolving Balance: {total_revolving_bal}
- Average Open-to-Buy Credit: {avg_open_to_buy}
- Change in Transaction Amount (Q4 to Q1): {total_amt_chng_q4_q1}
- Total Transaction Amount: {total_trans_amt}
- Total Transaction Count: {total_trans_ct}
- Change in Transaction Count (Q4 to Q1): {total_ct_chng_q4_q1}
- Average Utilization Ratio: {avg_utilization_ratio}

Based on this data, identify:
1. Key factors that indicate the customer's current level of satisfaction and engagement.
2. Potential risk areas that could lead to customer dissatisfaction in the future.
3. Specific proactive measures the bank can take to strengthen the customer's relationship with the bank.

JSON Output Expected:
- Reasons for potential dissatisfaction: (List)
- Suggested actions to enhance satisfaction: (List)
"""



# def super(request):
#     if 
api_key = 'YOUR_API_KEY_HERE'

def leaving(inp):
    print("Input data:", inp)
    
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash-001", generation_config={"response_mime_type": "application/json"})
    
    # Format the prompt with the input data
    formatted_prompt = PROMPT_TEMPLATE1.format(**inp)
    
    # Generate the response
    try:
        response = model.generate_content(formatted_prompt)
        print("Model response:", response)
        
        response_json = json.loads(response.text)
        return response_json

    except ValueError as e:
        print("Error parsing JSON:", str(e))
        raise JsonResponse(status_code=400, detail=f"Invalid JSON: {str(e)}")
    except AttributeError as e:
        print("Error processing model response:", str(e))
        raise JsonResponse(status_code=500,  detail=f"Error processing customer input: {str(e)}")
    
def inplace(inp):
    print("Input data:", inp)
    
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash-001", generation_config={"response_mime_type": "application/json"})
    
    # Format the prompt with the input data
    formatted_prompt = PROMPT_TEMPLATE.format(**inp)
    
    # Generate the response
    try:
        response = model.generate_content(formatted_prompt)
        print("Model response:", response)
        
        response_json = json.loads(response.text)
        return response_json

    except ValueError as e:
        print("Error parsing JSON:", str(e))
        raise JsonResponse(status_code=400, detail=f"Invalid JSON: {str(e)}")
    except AttributeError as e:
        print("Error processing model response:", str(e))
        raise JsonResponse(status_code=500,  detail=f"Error processing customer input: {str(e)}")


# Example Input Data
# example_input = {
#     "customer_age": 45.0,
#     "dependent_count": 2,
#     "months_on_book": 60,
#     "total_relationship_count": 4,
#     "months_inactive_12_mon": 3,
#     "contacts_count_12_mon": 6,
#     "credit_limit": 15000.0,
#     "total_revolving_bal": 3000.0,
#     "avg_open_to_buy": 12000.0,
#     "total_amt_chng_q4_q1": 0.5,
#     "total_trans_amt": 5000.0,
#     "total_trans_ct": 60,
#     "total_ct_chng_q4_q1": 0.4,
#     "avg_utilization_ratio": 0.2
# }

# # Call the function with example data
# result = speech(example_input)
# print("Final JSON Output:", result)
