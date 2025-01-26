import React, { useEffect, useRef } from 'react';
import StarRating from './StarRating';
import './ChatWindow.css';

const ChatWindow = ({ messages = [], setMessages, isLoading }) => {
  const endOfMessagesRef = useRef(null);

  useEffect(() => {
    endOfMessagesRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);


const handleRatingChange = (newRating, messageIndex) => {
  const newMessages = messages.map((msg, index) => {
    if (index === messageIndex) {
      // If the message has a topic property, it will be retained
      return { ...msg, rating: newRating };
    }
    return msg;
  });

  setMessages(newMessages);

    const ratedMessage = newMessages[messageIndex];
    sendFeedbackToAPI(newRating >= 3 ? 1 : 0, ratedMessage);
};



  const sendFeedbackToAPI = (relevant, message) => {
  console.log("Message object before sending feedback:", message);

  const payload = {
    relevant: relevant,
    topic_name: message.topic_name,
  };

  console.log("Sending to backend:", payload);

  fetch('http://34.125.9.200:9999/relevance', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(payload),
  })
  .then(response => response.json())
  .then(data => console.log(data))
  .catch((error) => console.error('Error:', error));
  console.log(payload);
};


  return (
    <div className="chat-window">
      {messages.map((msg, index) => (
  <div key={index} className={`message-bubble ${msg.sender}`}>
    {msg.sender === 'user' && (
      <img src={`${process.env.PUBLIC_URL}/assets/user-avatar.png`} alt="User" className="user-avatar" />
    )}
    {msg.sender === 'bot' && (
      <img src={`${process.env.PUBLIC_URL}/assets/bot-avatar.png`} alt="Bot" className="bot-avatar" />
    )}
    <div className="message-text">{msg.text}</div>
    {msg.sender === 'bot' && (
    <div className="star-rating">
      <StarRating currentRating={msg.rating} onRating={(rating) => handleRatingChange(rating, index)} />
    </div>
  )}
  </div>
))}

      <div ref={endOfMessagesRef} />
      {isLoading && (
        <div className="message-bubble bot loading">
          <div className="loading-indicator">Loading...</div>
        </div>
      )}
    </div>
  );
};

export default ChatWindow;