import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom'; // Use useNavigate instead of useHistory
import { Button, FormControl, FormLabel, Input, Typography, Sheet, CssBaseline } from '@mui/joy';

function Login() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [loginError, setLoginError] = useState('');
  const navigate = useNavigate(); // Use navigate

  const handleLogin = async () => {
    // Prepare login data
    const loginData = {
      username,
      password,
    };
  
    try {
      const response = await fetch('http://localhost:8000/login/', {
        method: 'POST', // Indicates it's a POST request
        headers: {
          'Content-Type': 'application/json', // Ensures that the body is sent as JSON
        },
        body: JSON.stringify(loginData), // Stringify the login data before sending it
      });
  
      const data = await response.json();
  
      // If token is returned, navigate to the main page
      if (data.token) {
        // Store the token or handle it as per your requirements (e.g., in localStorage)
        localStorage.setItem('token', data.token);
        navigate('/main'); // Navigate to the main page using navigate
      } else {
        // Show login failed message
        setLoginError('Login failed. Please check your credentials.');
      }
    } catch (error) {
      // Handle network or other errors
      setLoginError('An error occurred. Please try again later.');
    }
  };

  // Navigate as guest without login
  const handleContinueAsGuest = () => {
    navigate('/main'); // Navigate to the main page for the guest user
  };

  // Navigate to Forgot Password page
  const handleForgotPassword = () => {
    navigate('/forgot-password'); // Navigate to the forgot password page
  };

  return (
    <main>
      <CssBaseline />
      <Sheet
        sx={{
          width: 300,
          mx: 'auto',
          my: 4,
          py: 3,
          px: 2,
          display: 'flex',
          flexDirection: 'column',
          gap: 2,
          borderRadius: 'sm',
          boxShadow: 'md',
        }}
        variant="outlined"
      >
        <div>
          <Typography level="h4" component="h1">
            <b>Welcome!</b>
          </Typography>
          <Typography level="body-sm">Sign in to continue.</Typography>
        </div>

        <FormControl>
          <FormLabel>User Name</FormLabel>
          <Input
            name="username"
            type="text"
            placeholder="johndoe@email.com"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
        </FormControl>

        <FormControl>
          <FormLabel>Password</FormLabel>
          <Input
            name="password"
            type="password"
            placeholder="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </FormControl>

        <Button sx={{ mt: 1 }} onClick={handleLogin}>
          Log in
        </Button>

        {loginError && (
          <Typography sx={{ fontSize: 'sm', color: 'red', alignSelf: 'center' }}>
            {loginError}
          </Typography>
        )}

        {/* "Continue as Guest" Button */}
        <Button sx={{ mt: 2 }} variant="outlined" onClick={handleContinueAsGuest}>
          Continue as Guest
        </Button>

        {/* "Forgot Password" Button */}
        <Button sx={{ mt: 2 }} variant="text" onClick={handleForgotPassword}>
          Forgot Password?
        </Button>
      </Sheet>
    </main>
  );
}

export default Login;
