import React, { useState } from "react";
import "./App.css";

function App() {
  const [selectedOption, setSelectedOption] = useState(null);
  const [placeholderText, setPlaceholderText] = useState("");

  const handleButtonClick = (option) => {
    setSelectedOption(option);
    setPlaceholderText(
      option === "spam"
        ? "Email text goes here"
        : "Textbox to enter URL to Phishing Website"
    );
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Spam and Phishing Detector</h1>
        <div>
          <button
            className="App-button"
            style={{ backgroundColor: selectedOption === "spam" ? "blue" : "" }}
            onClick={() => handleButtonClick("spam")}
          >
            Spam Email
          </button>
          <button
            className="App-button"
            style={{
              backgroundColor: selectedOption === "phishing" ? "blue" : "",
            }}
            onClick={() => handleButtonClick("phishing")}
          >
            Phishing Website
          </button>
        </div>
        <textarea
          className="App-textarea"
          placeholder={placeholderText}
          rows={10}
          cols={50}
        />
      </header>
      <footer className="App-footer">
        <p>credits footer</p>
      </footer>
    </div>
  );
}

export default App;
