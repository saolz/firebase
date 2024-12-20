import React, { useState } from 'react';
import Login from "./components/Login";
import Signup from "./components/Signup";
import RazorpayPayment from "./components/RazorpayPayment";
import './firebase-config';  // Import firebase config

const App: React.FC = () => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [showSignup, setShowSignup] = useState(false);

  const handleLoginSuccess = () => {
    setIsLoggedIn(true);
  };

  const handleSignupSuccess = () => {
    setShowSignup(false);  // Return to login after signup
  };

  return (
    <div style={{
      minHeight: '100vh',
      width: '100vw',
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      backgroundColor: '#f5f5f5',
      position: 'absolute',
      left: 0,
      top: 0
    }}>
      <h1 style={{
        color: '#1a365d',
        marginTop: '40px',
        marginBottom: '20px',
        fontSize: '2.5rem',
        textAlign: 'center',
        fontWeight: '600'
      }}>
        Welcome to the Payment App
      </h1>
      
      <div style={{
        width: '100%',
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        gap: '20px'
      }}>
        {!isLoggedIn ? (
          <>
            {showSignup ? (
              <Signup onSignupSuccess={handleSignupSuccess} />
            ) : (
              <>
                <Login onLoginSuccess={handleLoginSuccess} />
                <button
                  onClick={() => setShowSignup(true)}
                  style={{
                    padding: '10px 20px',
                    backgroundColor: 'transparent',
                    border: '1px solid #3b82f6',
                    color: '#3b82f6',
                    borderRadius: '4px',
                    cursor: 'pointer'
                  }}
                >
                  Need an account? Sign up
                </button>
              </>
            )}
          </>
        ) : (
          <RazorpayPayment />
        )}
      </div>
    </div>
  );
};

export default App;
