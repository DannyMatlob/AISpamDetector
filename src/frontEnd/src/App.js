import React, { useState } from "react";
import "./App.css";

function App() {
  const [selectedOption, setSelectedOption] = useState(null);
  const [placeholderText, setPlaceholderText] = useState("");
  const [textEntry, setTextEntry] = useState("");

  const handleButtonClick = (option) => {
    setSelectedOption(option);
    if (option==="spam") {
      setTextEntry("")
      setPlaceholderText("Email text goes here")
    } else {
      setTextEntry("")
      setPlaceholderText("Textbox to enter URL to Phishing Website")
    }
  };

  const handleSubmit = () => {
    if (selectedOption === "spam") {
        console.log("Submitting Spam request with text:")
        console.log(textEntry)
        setTextEntry("PlaceHolder Email Result")
    } else if (selectedOption === "phishing") {
        console.log("Submitting Phishing request")
        console.log(textEntry)
        setTextEntry("PlaceHolder Phishing Result")
    } else {
        console.log("No selection")
    }
  };

  function handleChange(event) {
    setTextEntry(event.target.value)
  }
  return (
    <div className="App">
      <header className="App-header">
        <h1>Spam and Phishing Detector</h1>
        <div>
          <button
            className="App-button"
            style={{ backgroundColor: selectedOption === "spam" ? "#419760" : "" }}
            onClick={() => handleButtonClick("spam")}
          >
            Spam Email
          </button>
          <button
            className="App-button"
            style={{
              backgroundColor: selectedOption === "phishing" ? "#419760" : "",
            }}
            onClick={() => handleButtonClick("phishing")}
          >
            Phishing Website
          </button>
        </div>
        <textarea
          className="App-textarea"
          placeholder={placeholderText}
          value={textEntry}
          onChange={handleChange}
          rows={10}
          cols={50}
        />
        <button
            className="App-button"
            onClick={() => handleSubmit()}
          >
            Submit Request
        </button>
      </header>
      <footer className="App-footer">
        <p> Danny Matlob  | 
            Minh  | 
            Nathan Duong  | 
            Phil  | 
            Nguyen  | 
        </p>
        <a href="https://github.com/DannyMatlob/AISpamDetector">Github Page</a>
      </footer>
    </div>
  );
}

export default App;
