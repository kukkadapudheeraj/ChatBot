  import React, { useState } from 'react';
  import ChatWindow from './components/ChatWindow';
  import InputBox from './components/InputBox';
  import { Button } from '@mui/material';
  import Legend from "./components/Legend";
  import { Container, Paper, Typography, Grid } from '@mui/material';
  import './App.css';

  const App = () => {
    const [messages, setMessages] = useState([]);
    const [currentOption, setCurrentOption] = useState('Chitchat');
    const [inputValue, setInputValue] = useState('');
    const [isLoading, setIsLoading] = useState(false);
    const options = ["Chitchat", "All","A Tale of Two Cities","Alice's Adventures in Wonderland",
              "Dracula","Frankenstein; Or, The Modern Prometheus","Moby Dick; Or, The Whale",
              "Pride and Prejudice","The Adventures of Sherlock Holmes",
              "The Adventures of Tom Sawyer, Complete", "The Picture of Dorian Gray",
                "Wuthering Heights"]; // Your topics

    const handleSendMessage = async (messageText) => {
    if (messageText.trim()) {
       let queryType = currentOption.toLowerCase();
      if (queryType !== 'chitchat' && queryType !== 'all') {
        queryType = 'novel';
      }

      const messagePayload = {
        question: messageText,
        query_type: queryType,
        novel_name: queryType === 'novel' ? currentOption : "",
      };

      if (options.includes(currentOption) && currentOption !== 'All' && currentOption !== 'Chit Chat') {
        messagePayload.novel_name = currentOption;
      }

      setMessages(prevMessages => [...prevMessages, { text: messageText, sender: 'user' }]);
      setIsLoading(true);

      try {
        const response = await fetch("http://34.125.9.200:9999/execute_query", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(messagePayload),
        });
          console.log(messagePayload);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        setMessages(prevMessages => [...prevMessages, {
          text: data.answer,
          sender: 'bot',
          topic_name: data.topic,
          rating: 0
        }]);
        console.log('Response', data);
      } catch (error) {
        console.error('Error:', error);
        setMessages(prevMessages => [...prevMessages, { text: 'Error fetching response', sender: 'bot' }]);
      } finally {
        setIsLoading(false);
        setInputValue('');
      }
    }
  };


    const handleOptionSelect = (option) => {
      setCurrentOption(option);
    };

    return (
      <Container maxWidth="xl" style={{ padding: 0 }}>
        <div className="header">
          <Legend/>
          <Typography variant="h4" align="center" style={{ color: 'white' }} fontFamily={"Georgia"}>
            Chatbot
          </Typography>
          <Button
              variant="contained"
              style={{
                position: 'absolute',
                top: '25px',
                right: '100px',
                fontFamily: 'Georgia, serif',
                backgroundColor: '#ececec',
                color: '#4A4A4A',
                fontWeight: 'bold',
                textTransform: 'none',
              }}
              onClick={() => window.open('http://34.125.9.200:9999/analysis', '_blank')}
            >
              Statistics
            </Button>
        </div>
        <Paper style={{ height: '100vh', display: 'flex', flexDirection: 'row' }}>
          <Grid container style={{ height: '100%' }}>
            <Grid item xs={9}>
              <ChatWindow messages={messages} setMessages={setMessages} isLoading={isLoading}/>
              <InputBox onSendMessage={handleSendMessage} inputValue={inputValue} setInputValue={setInputValue} />
            </Grid>
            <Grid item xs={3} style={{ overflowY: 'auto' }}>
              <div className="options-panel">
                {options.map((option, index) => (
                  <div
                    key={index}
                    className={`option ${currentOption === option ? 'selected' : ''}`}
                    onClick={() => handleOptionSelect(option)}
                  >
                    {option}
                  </div>
                ))}
              </div>
            </Grid>
          </Grid>
        </Paper>
      </Container>
    );
  };

  export default App;