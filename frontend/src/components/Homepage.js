// src/components/Homepage.js
import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';
import './Homepage.css';  // Import the CSS file

function Homepage() {
  const [newReleases, setNewReleases] = useState([]);
  const [topRated, setTopRated] = useState([]);
  const [editorsPicks, setEditorsPicks] = useState([]);
  const [searchQuery, setSearchQuery] = useState('');
  const [searchResults, setSearchResults] = useState([]);

  useEffect(() => {
    const fetchBooks = async () => {
      try {
        const [newReleasesResponse, topRatedResponse, editorsPicksResponse] = await Promise.all([
          axios.get('http://127.0.0.1:5001/api/books?query=new_releases'),
          axios.get('http://127.0.0.1:5001/api/books?query=top_rated'),
          axios.get('http://127.0.0.1:5001/api/books?query=editors_picks')
        ]);

        setNewReleases(newReleasesResponse.data);
        setTopRated(topRatedResponse.data);
        setEditorsPicks(editorsPicksResponse.data);
      } catch (error) {
        console.error('Error fetching books:', error);
      }
    };

    fetchBooks();
  }, []);

  const handleSearch = async (event) => {
    event.preventDefault();
    if (searchQuery) {
      try {
        const response = await axios.get(`http://127.0.0.1:5001/api/books?query=${searchQuery}`);
        setSearchResults(response.data);
      } catch (error) {
        console.error('Error searching books:', error);
      }
    }
  };

  return (
    <div className="homepage-container">
      <h1>BookCritique</h1>

      <form className="search-form" onSubmit={handleSearch}>
        <input 
          type="text"
          placeholder="Search by author, genre, or title"
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
          className="search-input"
        />
        <button type="submit" className="search-button">Search</button>
      </form>

      {searchResults.length > 0 && (
        <div>
          <h2>Search Results</h2>
          <div className="books-grid">
            {searchResults.map((book) => (
              <Link to={`/book/${book.id}`} key={book.id} className="book-card">
                <img src={book.volumeInfo.imageLinks?.thumbnail} alt={book.volumeInfo.title} />
                <h3>{book.volumeInfo.title}</h3>
                <p>{book.volumeInfo.authors?.join(', ')}</p>
              </Link>
            ))}
          </div>
        </div>
      )}

      <h2>New Releases</h2>
      <div className="books-grid">
        {newReleases.map((book) => (
          <Link to={`/book/${book.id}`} key={book.id} className="book-card">
            <img src={book.volumeInfo.imageLinks?.thumbnail} alt={book.volumeInfo.title} />
            <h3>{book.volumeInfo.title}</h3>
            <p>{book.volumeInfo.authors?.join(', ')}</p>
          </Link>
        ))}
      </div>

      <h2>Top Rated</h2>
      <div className="books-grid">
        {topRated.map((book) => (
          <Link to={`/book/${book.id}`} key={book.id} className="book-card">
            <img src={book.volumeInfo.imageLinks?.thumbnail} alt={book.volumeInfo.title} />
            <h3>{book.volumeInfo.title}</h3>
            <p>{book.volumeInfo.authors?.join(', ')}</p>
          </Link>
        ))}
      </div>

      <h2>Editor's Picks</h2>
      <div className="books-grid">
        {editorsPicks.map((book) => (
          <Link to={`/book/${book.id}`} key={book.id} className="book-card">
            <img src={book.volumeInfo.imageLinks?.thumbnail} alt={book.volumeInfo.title} />
            <h3>{book.volumeInfo.title}</h3>
            <p>{book.volumeInfo.authors?.join(', ')}</p>
          </Link>
        ))}
      </div>

      <footer className="footer">
        <p>&copy; 2024 Book Review. All rights reserved.</p>
        <p>Terms of Service | Privacy Policy</p>
      </footer>
    </div>
  );
}

export default Homepage;