import { useEffect, useRef, useState } from "react"
import logo from './logo.svg';
import './App.css';
import { io } from 'socket.io-client'

function App() {
  const [socket, setSocket] = useState()
  const counter = useRef(0)
  const [message, setMessage] = useState()

  useEffect(() => {
    const s = io()

    s.on("message", json => {
      setMessage(json)
    })

    setSocket(s)

    return () => {
      console.log("Disconnected!")
      s.disconnect()
    }

  }, [])

  return (
    <div className="App">
      <header className="App-header">
        <p>{message}</p>
      </header>
    </div>
  );
}

export default App;
