const InputBox = ({ onSendMessage, inputValue, setInputValue }) => {
  const handleInputChange = (e) => {
    setInputValue(e.target.value);
  };

  const handleSubmit = () => {
    onSendMessage(inputValue);
  };

  return (
    <div className="input-box">
      <input type="text" value={inputValue} onChange={handleInputChange} />
      <button onClick={handleSubmit}>Send</button>
    </div>
  );
};

export default InputBox;
