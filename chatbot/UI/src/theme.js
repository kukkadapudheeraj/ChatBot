// theme.js

import { createTheme } from '@mui/material/styles';

const theme = createTheme({
  palette: {
    primary: {
      main: '#007acc', // Change to your primary color
    },
    secondary: {
      main: '#ff6f61', // Change to your secondary color
    },
  },
  typography: {
    fontFamily: 'Arial, sans-serif', // Change to your preferred font
  },
});

export default theme;
