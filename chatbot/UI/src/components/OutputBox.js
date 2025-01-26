import React from 'react';
import { Box } from '@mui/material';
import Message from './Message';

const OutputBox = ({ messages }) => {
  return (
    <Box sx={{ height: '150px', overflowY: 'auto', padding: '10px', border: '1px solid #ccc', marginTop: '10px' }}>
      {messages.map((message, index) => (
        <Message key={index} text={message.text} isUser={message.isUser} />
      ))}
    </Box>
  );
};

export default OutputBox;
