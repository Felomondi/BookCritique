// src/components/BookDetails.js
import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import './BookDetails.css';

function BookDetails() {
  const { id } = useParams();
  const [book, setBook] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchBookDetails = async () => {
      try {
        // Fetch book details directly from Google Books API
        const response = await axios.get(`https://www.googleapis.com/books/v1/volumes/${id}`);
        if (response.status === 200) {
          setBook(response.data);
        } else {
          setError({ message: 'Book not found' });
        }
      } catch (error) {
        console.error('Error fetching book details:', error);
        setError(error);
      }
    };

    fetchBookDetails();
  }, [id]);

  if (error) {
    return <div>Error fetching book details: {error.message}</div>;
  }

  if (!book) {
    return <div>Loading...</div>;
  }

  return (
    <div className="book-details-container">
  <h1>{book.volumeInfo.title}</h1>
  {book.volumeInfo.subtitle && <h3>{book.volumeInfo.subtitle}</h3>}
  <img src={book.volumeInfo.imageLinks?.thumbnail} alt={book.volumeInfo.title} />
  <h2>By {book.volumeInfo.authors?.join(', ')}</h2>
  {book.volumeInfo.categories && <p><strong>Categories:</strong> {book.volumeInfo.categories.join(', ')}</p>}
  {book.volumeInfo.averageRating && <p><strong>Average Rating:</strong> {book.volumeInfo.averageRating} / 5</p>}
  {book.volumeInfo.ratingsCount && <p><strong>Ratings Count:</strong> {book.volumeInfo.ratingsCount}</p>}
  {book.volumeInfo.pageCount && <p><strong>Page Count:</strong> {book.volumeInfo.pageCount}</p>}
  {book.volumeInfo.language && <p><strong>Language:</strong> {book.volumeInfo.language.toUpperCase()}</p>}
  <p>{book.volumeInfo.description}</p>
  <p><strong>Publisher:</strong> {book.volumeInfo.publisher}</p>
  <p><strong>Published Date:</strong> {book.volumeInfo.publishedDate}</p>
  {book.volumeInfo.industryIdentifiers && (
    <p><strong>ISBNs:</strong> {book.volumeInfo.industryIdentifiers.map(identifier => `${identifier.type}: ${identifier.identifier}`).join(', ')}</p>
  )}
  <a href={book.volumeInfo.previewLink} target="_blank" rel="noopener noreferrer">Preview this book</a>
  <a href={book.volumeInfo.infoLink} target="_blank" rel="noopener noreferrer">More information</a>
</div>
  );
}

export default BookDetails;