// src/components/Home.js
import React from 'react';
import { Link } from 'react-router-dom';

function Home() {
  return (
    <div>
      <h1>Welcome to Book Review</h1>
      <p>
        <Link to="/login">Login</Link> if you already have an account.
      </p>
      <p>
        <Link to="/register">Register</Link> if you don't have an account.
      </p>
    </div>
  );
}

export default Home;