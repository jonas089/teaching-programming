import logo from './logo.svg';
import './App.css';
import React, {useEffect, useState} from 'react';

function App() {
  const [text, setText] = useState(null);

  useEffect(() => {
    fetch('http://127.0.0.1:7000/react')
      .then(response => response.json())
      .then(text => setText(text))
      .catch(error => console.log("Error: ", error));
  }, []);

  if (!text){
    return <div>Loading...</div>
  }
  else{
    return (
      <div className="App">
        <p>Text from server {text}</p>
      </div>
    );
  }
}

export default App;
