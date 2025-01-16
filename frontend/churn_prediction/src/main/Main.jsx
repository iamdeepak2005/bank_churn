import * as React from 'react';
import { extendTheme, styled } from '@mui/material/styles';
import BarChartIcon from '@mui/icons-material/BarChart';
import { AppProvider } from '@toolpad/core/AppProvider';
import { DashboardLayout } from '@toolpad/core/DashboardLayout';
import { PageContainer } from '@toolpad/core/PageContainer';
import PersonAddIcon from '@mui/icons-material/PersonAdd';
import AddCircleIcon from '@mui/icons-material/AddCircle';
import AnalyticsIcon from '@mui/icons-material/Analytics';
import { TextField, Button, Box, Typography, CircularProgress,Paper, Grid } from '@mui/material';
import './Main.css';
import { MenuItem, Select, FormControl, InputLabel, } from '@mui/material';
import Loader from './Loader';
const NAVIGATION = [
  {
    kind: 'header',
    title: 'Main items',
  },
  {
    segment: 'dashboard',
    title: 'Predict Churning',
    icon: <AnalyticsIcon />,
  },
  {
    segment: 'customer',
    title: 'Add Customer Details',
    icon: <PersonAddIcon />,
  },
  {
    segment: 'churn',
    title: 'Add Additional Info',
    icon: <AddCircleIcon />,
  },
  {
    kind: 'divider',
  },
  {
    kind: 'header',
    title: 'Analytics',
  },
  {
    segment: 'reports',
    title: 'Reports',
    icon: <BarChartIcon />,
  },
];

const demoTheme = extendTheme({
  colorSchemes: { light: true, dark: true },
  colorSchemeSelector: 'class',
  breakpoints: {
    values: {
      xs: 0,
      sm: 600,
      md: 600,
      lg: 1200,
      xl: 1536,
    },
  },
});

function useDemoRouter(initialPath) {
  const [pathname, setPathname] = React.useState(initialPath);

  const router = React.useMemo(() => {
    return {
      pathname,
      searchParams: new URLSearchParams(),
      navigate: (path) => setPathname(String(path)),
    };
  }, [pathname]);

  return router;
}

const InputFields = ({ onSubmit }) => {
  const [responseData, setResponseData] = React.useState(null);

  const [customerData, setCustomerData] = React.useState({
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

  // Handle input changes for form fields

  // Handle input changes for form fields
  const handleChange = (e) => {
    const { name, value } = e.target;
    setCustomerData({
      ...customerData,
      [name]: value,
    });
  };
  const [isLoad, setIsLoad] = React.useState(false);

  const handleSubmit = async () => {
    try {
      setIsLoad(true);  // Start the loading spinner
      const response = await fetch('http://localhost:8000/predict/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(customerData),
      });
  
      if (response.ok) {
        const result = await response.json();
        setResponseData(result); // Handle the response from backend
      } else {
        console.error('Error with response:', response.status);
      }
    } catch (error) {
      console.error('Error predicting churn:', error);
    } finally {
      setIsLoad(false);  // Stop the loading spinner after the request is complete or if there's an error
    }
  };

  return (
<div className="dashboard">
{isLoad ? <Loader  /> : <div></div>}
<Box sx={{ display: 'flex', flexDirection: 'row', justifyContent: 'space-between', marginTop: 2 }}>
        <Box sx={{ flex: 1, padding: 2 }}>
          <label htmlFor="">Customer Details</label>
          <div className="span">
          <TextField
            name="customer_age"
            label="Customer Age"
            value={customerData.customer_age}
            onChange={handleChange}
            fullWidth
            type="number"
            margin="normal"
          />

          <FormControl fullWidth>
            <InputLabel>Gender</InputLabel>
            <Select
              name="gender"
              value={customerData.gender}
              onChange={handleChange}
              label="Gender"
            >
              <MenuItem value="Male">Male</MenuItem>
              <MenuItem value="Female">Female</MenuItem>
              <MenuItem value="Unknown">Unknown</MenuItem>
            </Select>
          </FormControl>
          </div>

          <div className="span">
          <FormControl fullWidth>
            <InputLabel>Education Level</InputLabel>
            <Select
              name="education_level"
              value={customerData.education_level}
              onChange={handleChange}
              label="Education Level"
            >
              <MenuItem value="Graduate">Graduate</MenuItem>
              <MenuItem value="College">College</MenuItem>
              <MenuItem value="High School">High School</MenuItem>
              <MenuItem value="Post-Graduate">Post-Graduate</MenuItem>
              <MenuItem value="Doctorate">Doctorate</MenuItem>
              <MenuItem value="Unknown">Unknown</MenuItem>
              <MenuItem value="Uneducated">Uneducated</MenuItem>
            </Select>
          </FormControl>

          <FormControl fullWidth>
            <InputLabel>Marital Status</InputLabel>
            <Select
              name="marital_status"
              value={customerData.marital_status}
              onChange={handleChange}
              label="Marital Status"
            >
              <MenuItem value="Single">Single</MenuItem>
              <MenuItem value="Married">Married</MenuItem>
              <MenuItem value="Divorced">Divorced</MenuItem>
              <MenuItem value="Unknown">Unknown</MenuItem>

            </Select>
          </FormControl>

          <TextField
          name="total_relationship_count"
          label="Total Relationship Count"
          value={customerData.total_relationship_count}
          onChange={handleChange}
          fullWidth
          type="number"
          margin="normal"
        />

          </div>
          <FormControl fullWidth>
            <InputLabel>Income Category</InputLabel>
            <Select
              name="income_category"
              value={customerData.income_category}
              onChange={handleChange}
              label="Income Category"
            >
              <MenuItem value="Less than $40K">Less than $40K</MenuItem>
              <MenuItem value="$40K - $60K">$40K - $60K</MenuItem>
              <MenuItem value="$60K - $80K">$60K - $80K</MenuItem>
              <MenuItem value="$80K - $120K">$80K - $120K</MenuItem>
              <MenuItem value="$120K +">$120K +</MenuItem>
              <MenuItem value="Unknown">Unknown</MenuItem>

            </Select>
          </FormControl>


          <label htmlFor="">Card Details</label>
          <div className="span">
          <FormControl fullWidth>
            <InputLabel>Card Category</InputLabel>
            <Select
              name="card_category"
              value={customerData.card_category}
              onChange={handleChange}
              label="Card Category"
            >
              <MenuItem value="Blue">Blue</MenuItem>
              <MenuItem value="Silver">Silver</MenuItem>
              <MenuItem value="Gold">Gold</MenuItem>
              <MenuItem value="Gold">Platinum</MenuItem>

            </Select>
          </FormControl>

          <TextField
          name="credit_limit"
          label="Credit Limit"
          value={customerData.credit_limit}
          onChange={handleChange}
          fullWidth
          type="number"
          margin="normal"
        />
          </div>
          <div className="span">
          <TextField
          name="total_revolving_bal"
          label="Total Revolving Balance"
          value={customerData.total_revolving_bal}
          onChange={handleChange}
          fullWidth
          type="number"
          margin="normal"
        />

        {/* Avg Open to Buy (Text input) */}
        <TextField
          name="avg_open_to_buy"
          label="Avg Open to Buy"
          value={customerData.avg_open_to_buy}
          onChange={handleChange}
          fullWidth
          type="number"
          margin="normal"
        />
          </div>


        <label htmlFor="">Transaction Details</label>
        <div className="span">
        <TextField
          name="months_inactive_12_mon"
          label="Months Inactive in Last 12 Months"
          value={customerData.months_inactive_12_mon}
          onChange={handleChange}
          fullWidth
          type="number"
          margin="normal"
        />

        {/* Contacts Count in Last 12 Months (Text input) */}
        <TextField
          name="contacts_count_12_mon"
          label="Contacts Count in Last 12 Months"
          value={customerData.contacts_count_12_mon}
          onChange={handleChange}
          fullWidth
          type="number"
          margin="normal"
        />

        <TextField
          name="total_amt_chng_q4_q1"
          label="Total Amt Change Q4 to Q1"
          value={customerData.total_amt_chng_q4_q1}
          onChange={handleChange}
          fullWidth
          type="number"
          margin="normal"
        />


        </div>
        {/* Total Transaction Amount (Text input) */}
<div className="span">
<TextField
          name="total_trans_amt"
          label="Total Transaction Amount"
          value={customerData.total_trans_amt}
          onChange={handleChange}
          fullWidth
          type="number"
          margin="normal"
        />

        {/* Total Transaction Count (Text input) */}
        <TextField
          name="total_trans_ct"
          label="Total Transaction Count"
          value={customerData.total_trans_ct}
          onChange={handleChange}
          fullWidth
          type="number"
          margin="normal"
        />

        {/* Total Count Change Q4 to Q1 (Text input) */}
        <TextField
          name="total_ct_chng_q4_q1"
          label="Total Count Change Q4 to Q1"
          value={customerData.total_ct_chng_q4_q1}
          onChange={handleChange}
          fullWidth
          type="number"
          margin="normal"
        />

</div>
        {/* Avg Utilization Ratio (Text input) */}
<div className="span">
<TextField
          name="avg_utilization_ratio"
          label="Avg Utilization Ratio"
          value={customerData.avg_utilization_ratio}
          onChange={handleChange}
          fullWidth
          type="number"
          margin="normal"
        />





          {/* Age (Text input) */}

           {/* Age (Text input) */}

        {/* Dependent Count (Text input) */}
        <TextField
          name="dependent_count"
          label="Dependent Count"
          value={customerData.dependent_count}
          onChange={handleChange}
          fullWidth
          type="number"
          margin="normal"
        />

        {/* Months on Book (Text input) */}
        <TextField
          name="months_on_book"
          label="Months on Book"
          value={customerData.months_on_book}
          onChange={handleChange}
          fullWidth
          type="number"
          margin="normal"
        />

</div>        {/* Total Relationship Count (Text input) */}


        {/* Months Inactive in Last 12 Months (Text input) */}
          {/* Other input fields... */}

          <Button variant="contained" color="primary" onClick={handleSubmit} sx={{ marginTop: 2 }}>
            Predict Churn
          </Button>
        </Box>

        {/* Response Section */}
        {responseData && responseData.suggestion && (
          <Box sx={{ flex: 1, padding: 2 }}>
            <Paper sx={{ padding: 2, backgroundColor: '#f9f9f9', borderRadius: 2 }}>
              <Typography variant="h6" sx={{ fontWeight: 'bold' }}>
                Prediction: {responseData.prediction === 0 ? 'No Churn' : 'Churn'}
              </Typography>

              <Typography variant="subtitle1" sx={{ fontWeight: 'bold', marginTop: 2 }}>
                Reasons for Potential Dissatisfaction:
              </Typography>
              <Box sx={{ marginTop: 1 }}>
                {responseData.suggestion['Reasons for potential dissatisfaction'].map((reason, index) => (
                  <Typography key={index} sx={{ marginBottom: 1 }}>
                    - {reason}
                  </Typography>
                ))}
              </Box>

              <Typography variant="subtitle1" sx={{ fontWeight: 'bold', marginTop: 2 }}>
                Suggested Actions to Enhance Satisfaction:
              </Typography>
              <Box sx={{ marginTop: 1 }}>
                {responseData.suggestion['Suggested actions to enhance satisfaction'].map((action, index) => (
                  <Typography key={index} sx={{ marginBottom: 1 }}>
                    - {action}
                  </Typography>
                ))}
              </Box>
            </Paper>
          </Box>
        )}
      </Box>
    </div>
  );};


function Main(props) {
  const { window } = props;
  const router = useDemoRouter('/dashboard');
  const [session, setSession] = React.useState({
    user: {
      name: 'Bharat Kashyap',
      email: 'bharatkashyap@outlook.com',
      image: 'https://avatars.githubusercontent.com/u/19550456',
    },
  });

  const authentication = React.useMemo(() => {
    return {
      signIn: () => {
        setSession({
          user: {
            name: 'Bharat Kashyap',
            email: 'bharatkashyap@outlook.com',
            image: 'https://avatars.githubusercontent.com/u/19550456',
          },
        });
      },
      signOut: () => {
        setSession(null);
      },
    };
  }, []);

  const [predictionResult, setPredictionResult] = React.useState(null);
  const [chatMessages, setChatMessages] = React.useState([
    'Hello, how can I assist you today?',
  ]);
  const [userInput, setUserInput] = React.useState('');
  const [loading, setLoading] = React.useState(false);

  const handlePredictionResult = (result) => {
    setLoading(false);
    setPredictionResult(result);
    setChatMessages((prevMessages) => [
      ...prevMessages,
      'Prediction result: ' + (result.prediction === 1 ? 'Churn likely' : 'No churn'),
      ...result.suggestion['Reasons for churn'].map((reason) => 'Reason: ' + reason),
      ...result.suggestion['Suggested actions'].map((action) => 'Action: ' + action),
    ]);
  };

  const handleSendMessage = (message) => {
    setUserInput('');
    setChatMessages((prevMessages) => [...prevMessages, message]);
  };

  return (
    <AppProvider
      navigation={NAVIGATION}
      router={router}
      theme={demoTheme}
      window={window}
      branding={{
        logo: <img src="" />,
        title: 'Bank Churn Prediction',
        homeUrl: '/toolpad/core/introduction',
      }}
      session={session}
      authentication={authentication}
    >
      <DashboardLayout className="dashboard">
        <PageContainer sx={{ display: 'flex', flexDirection: 'row', padding: '16px' }}>
          <Box sx={{ width: '25%', paddingRight: '16px', borderRight: '1px solid #ddd' }} />

          <Box sx={{ flex: 1 }}>
            <InputFields onSubmit={handlePredictionResult} />

            {loading && (
              <Box sx={{ display: 'flex', justifyContent: 'center', padding: '20px' }}>
                <CircularProgress />
              </Box>
            )}


            {predictionResult && (
              <Box sx={{ marginTop: '16px' }}>
                <Typography variant="h6">Prediction Result</Typography>
                <Typography>
                  Churn Prediction: {predictionResult.prediction === 1 ? 'Yes' : 'No'}
                </Typography>
                <Typography>Reasons for churn:</Typography>
                <ul>
                  {predictionResult.suggestion['Reasons for churn'].map((reason, index) => (
                    <li key={index}>{reason}</li>
                  ))}
                </ul>
                <Typography>Suggested actions:</Typography>
                <ul>
                  {predictionResult.suggestion['Suggested actions'].map((action, index) => (
                    <li key={index}>{action}</li>
                  ))}
                </ul>
              </Box>
            )}
          </Box>
        </PageContainer>

      </DashboardLayout>
    </AppProvider>
  );
}

export default Main;
