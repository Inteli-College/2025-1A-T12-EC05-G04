// ErrorMessage.js
import React from 'react';

const ErrorMessage = ({ message }) => {
  if (!message) return null;
  return (
    <div style={{
      backgroundColor: "#ffcccc",
      padding: "1rem",
      borderRadius: "8px",
      marginBottom: "1rem"
    }}>
      <p style={{ color: "#cc0000" }}>{message}</p>
    </div>
  );
};

export default ErrorMessage;
