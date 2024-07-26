// src/components/Homepage.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';

function Homepage() {
  const [books, setBooks] = useState([]);

  useEffect(() => {
    const fetchBooks = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:5001/api/books?query=bestsellers');
        setBooks(response.data);
      } catch (error) {
        console.error('Error fetching books:', error);
      }
    };

    fetchBooks();
  }, []);

  return (
    <div>
      <h1>Book Previews</h1>
      <div>
        {books.map((book) => (
          <div key={book.id}>
            <h2>{book.volumeInfo.title}</h2>
            <p>{book.volumeInfo.authors?.join(', ')}</p>
            <img src={book.volumeInfo.imageLinks?.thumbnail} alt={book.volumeInfo.title} />
          </div>
        ))}
      </div>
    </div>
  );
}

export default Homepage;