// src/App.js
import React from 'react';
import { Routes, Route, Link } from 'react-router-dom';
import Home from './components/Home';
import Homepage from './components/Homepage';
import Login from './components/Login';
import Register from './components/Register';

const App = () => (
  <div>
    <nav>
      <ul>
        <li><Link to="/">Home</Link></li>
        <li><Link to="/login">Login</Link></li>
        <li><Link to="/register">Register</Link></li>
        {/* <li><Link to="/homepage">Homepage</Link></li> */}
      </ul>
    </nav>
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/login" element={<Login />} />
      <Route path="/register" element={<Register />} />
      <Route path="/homepage" element={<Homepage />} />
    </Routes>
  </div>
);

export default App;