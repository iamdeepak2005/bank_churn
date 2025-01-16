import React, { useState } from 'react';
import Box from '@mui/material/Box';
import Stepper from '@mui/material/Stepper';
import Step from '@mui/material/Step';
import StepLabel from '@mui/material/StepLabel';
import StepContent from '@mui/material/StepContent';
import Button from '@mui/material/Button';
import Paper from '@mui/material/Paper';
import Typography from '@mui/material/Typography';
import TextField from '@mui/material/TextField';
import Grid from '@mui/material/Grid';

const steps = [
  {
    label: 'Enter Customer Details',
    fields: [
      { name: 'customer_age', label: 'Customer Age', description: 'Enter the customer\'s age.' },
      { name: 'gender', label: 'Gender', description: 'Select the customer\'s gender.' },
      { name: 'dependent_count', label: 'Dependent Count', description: 'Enter the number of dependents.' },
      { name: 'education_level', label: 'Education Level', description: 'Select the customer\'s highest education level.' },
      { name: 'marital_status', label: 'Marital Status', description: 'Select the marital status.' },
      { name: 'income_category', label: 'Income Category', description: 'Select the income category.' },
      { name: 'card_category', label: 'Card Category', description: 'Select the card category.' }
    ],
  },
  {
    label: 'Enter Relationship Details',
    fields: [
      { name: 'months_on_book', label: 'Months on Book', description: 'Enter the number of months on the account.' },
      { name: 'total_relationship_count', label: 'Total Relationship Count', description: 'Enter the total number of relationships.' },
      { name: 'months_inactive_12_mon', label: 'Months Inactive (12 Mon)', description: 'Enter the months of inactivity within the past 12 months.' },
      { name: 'contacts_count_12_mon', label: 'Contacts Count (12 Mon)', description: 'Enter the number of contacts made in the past 12 months.' },
      { name: 'credit_limit', label: 'Credit Limit', description: 'Enter the credit limit.' },
      { name: 'total_revolving_bal', label: 'Total Revolving Balance', description: 'Enter the total revolving balance.' },
      { name: 'avg_open_to_buy', label: 'Average Open to Buy', description: 'Enter the average amount available to buy.' },
    ],
  },
  {
    label: 'Enter Transaction Details',
    fields: [
      { name: 'total_amt_chng_q4_q1', label: 'Total Amount Change (Q4/Q1)', description: 'Enter the change in total amount from Q4 to Q1.' },
      { name: 'total_trans_amt', label: 'Total Transaction Amount', description: 'Enter the total transaction amount.' },
      { name: 'total_trans_ct', label: 'Total Transaction Count', description: 'Enter the total number of transactions.' },
      { name: 'total_ct_chng_q4_q1', label: 'Total Count Change (Q4/Q1)', description: 'Enter the change in total transaction count from Q4 to Q1.' },
      { name: 'avg_utilization_ratio', label: 'Average Utilization Ratio', description: 'Enter the average utilization ratio.' }
    ],
  },
];

function StepperForm() {
  const [activeStep, setActiveStep] = useState(0);
  const [formData, setFormData] = useState({
    customer_age: '',
    gender: '',
    dependent_count: '',
    education_level: '',
    marital_status: '',
    income_category: '',
    card_category: '',
    months_on_book: '',
    total_relationship_count: '',
    months_inactive_12_mon: '',
    contacts_count_12_mon: '',
    credit_limit: '',
    total_revolving_bal: '',
    avg_open_to_buy: '',
    total_amt_chng_q4_q1: '',
    total_trans_amt: '',
    total_trans_ct: '',
    total_ct_chng_q4_q1: '',
    avg_utilization_ratio: '',
  });

  const [fieldDescription, setFieldDescription] = useState('');

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({ ...prevData, [name]: value }));
  };

  const handleNext = () => {
    setActiveStep((prevActiveStep) => prevActiveStep + 1);
  };

  const handleBack = () => {
    setActiveStep((prevActiveStep) => prevActiveStep - 1);
  };

  const handleReset = () => {
    setActiveStep(0);
    setFormData({
      customer_age: '',
      gender: '',
      dependent_count: '',
      education_level: '',
      marital_status: '',
      income_category: '',
      card_category: '',
      months_on_book: '',
      total_relationship_count: '',
      months_inactive_12_mon: '',
      contacts_count_12_mon: '',
      credit_limit: '',
      total_revolving_bal: '',
      avg_open_to_buy: '',
      total_amt_chng_q4_q1: '',
      total_trans_amt: '',
      total_trans_ct: '',
      total_ct_chng_q4_q1: '',
      avg_utilization_ratio: '',
    });
  };

  const handleFocus = (description) => {
    setFieldDescription(description);
  };

  return (
    <Box sx={{ maxWidth: 600 }}>
      <Stepper activeStep={activeStep} orientation="vertical">
        {steps.map((step, index) => (
          <Step key={step.label}>
            <StepLabel
              optional={
                index === steps.length - 1 ? (
                  <Typography variant="caption">Last step</Typography>
                ) : null
              }
            >
              {step.label}
            </StepLabel>
            <StepContent>
              <Grid container spacing={2}>
                {step.fields.map((field) => (
                  <Grid item xs={6} key={field.name}>
                    <TextField
                      name={field.name}
                      label={field.label}
                      value={formData[field.name]}
                      onChange={handleChange}
                      onFocus={() => handleFocus(field.description)}
                      fullWidth
                      margin="normal"
                    />
                  </Grid>
                ))}
              </Grid>
              <Box sx={{ mb: 2 }}>
                {fieldDescription && (
                  <Typography variant="body2" sx={{ color: 'gray' }}>
                    {fieldDescription}
                  </Typography>
                )}
                <Button
                  variant="contained"
                  onClick={handleNext}
                  sx={{ mt: 1, mr: 1 }}
                >
                  {index === steps.length - 1 ? 'Finish' : 'Continue'}
                </Button>
                <Button
                  disabled={index === 0}
                  onClick={handleBack}
                  sx={{ mt: 1, mr: 1 }}
                >
                  Back
                </Button>
              </Box>
            </StepContent>
          </Step>
        ))}
      </Stepper>
      {activeStep === steps.length && (
        <Paper square elevation={0} sx={{ p: 3 }}>
          <Typography>All steps completed - you&apos;re finished</Typography>
          <Button onClick={handleReset} sx={{ mt: 1, mr: 1 }}>
            Reset
          </Button>
        </Paper>
      )}
    </Box>
  );
}

export default StepperForm;
  