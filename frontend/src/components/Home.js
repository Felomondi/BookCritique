// src/components/Home.js
import React from 'react';
import { Link } from 'react-router-dom';
import './Home.css';

function Home() {
  return (
    <div className="home-container">
      <h1>Welcome to Book Review</h1>
      <h2>A Community For All Book Lovers</h2>
      <p className="description">Your one-stop platform for all book reviews and ratings. Join our community now!</p>
      <div className="links-container">
        <Link to="/login" className="home-link">Login</Link>
        <Link to="/register" className="home-link">Register</Link>
      </div>
    </div>
  );
}

export default Home;