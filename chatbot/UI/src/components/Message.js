import React from 'react';
import { ListItem, ListItemText, Paper } from '@mui/material';

const Message = ({ text, isUser }) => {
  const style = {
    backgroundColor: isUser ? '#e0f7fa' : '#eceff1',
    padding: '10px 20px',
    borderRadius: '20px',
    maxWidth: '75%',
    marginLeft: isUser ? 'auto' : '10px',
    marginRight: isUser ? '10px' : 'auto',
    marginBottom: '10px',
  };

  return (
    <ListItem>
      <Paper style={style}>
        <ListItemText primary={text} />
      </Paper>
    </ListItem>
  );
};

export default Message;
