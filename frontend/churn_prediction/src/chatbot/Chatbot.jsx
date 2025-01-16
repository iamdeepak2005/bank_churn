import React from 'react';
import { Box, Typography, List, ListItem, Divider } from '@mui/material';

function Chatbot({ response = {} }) {
  const { prediction, suggestion } = response;

  // Add a fallback value for prediction and suggestion if they are undefined
  const predictionText = prediction === 1 ? 'Churn Likely' : 'Churn Unlikely';
  const reasons = suggestion?.['Reasons for churn'] || [];
  const actions = suggestion?.['Suggested actions'] || [];

  return (
    <Box 
      sx={{ 
        padding: 3, 
        width: '200%', 
        margin: 'auto', 
        backgroundColor: '#ffffff', 
        borderRadius: 2, 
        boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)', 
        border: '1px solid #ddd' 
      }}
    >
      <Typography 
        variant="h5" 
        sx={{ 
          marginBottom: 2, 
          fontWeight: '600', 
          color: '#1976d2', 
          fontSize: '1.5rem' 
        }}
      >
        Chatbot Response
      </Typography>
      
      <Typography 
        variant="h6" 
        sx={{ 
          marginBottom: 1, 
          color: '#333', 
          fontSize: '1.125rem', 
          fontWeight: '500' 
        }}
      >
        Prediction: {predictionText}
      </Typography>

      <Box sx={{ marginBottom: 3 }}>
        <Typography 
          variant="h6" 
          sx={{ 
            fontWeight: '600', 
            color: '#1976d2', 
            fontSize: '1.125rem' 
          }}
        >
          Reasons for Churn:
        </Typography>
        <List sx={{ paddingLeft: 2, paddingTop: 1 }}>
          {reasons.map((reason, index) => (
            <ListItem key={index} sx={{ paddingLeft: 0 }}>
              <Typography variant="body2" sx={{ color: '#555', fontSize: '1rem' }}>
                {reason}
              </Typography>
            </ListItem>
          ))}
        </List>
      </Box>

      <Divider sx={{ marginY: 3 }} />

      <Box>
        <Typography 
          variant="h6" 
          sx={{ 
            fontWeight: '600', 
            color: '#1976d2', 
            fontSize: '1.125rem' 
          }}
        >
          Suggested Actions:
        </Typography>
        <List sx={{ paddingLeft: 2, paddingTop: 1 }}>
          {actions.map((action, index) => (
            <ListItem key={index} sx={{ paddingLeft: 0 }}>
              <Typography variant="body2" sx={{ color: '#555', fontSize: '1rem' }}>
                {action}
              </Typography>
            </ListItem>
          ))}
        </List>
      </Box>
    </Box>
  );
}

export default Chatbot;
