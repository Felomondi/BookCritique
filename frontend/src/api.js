import axios from 'axios';

const api = axios.create({
  baseURL: 'http://127.0.0.1:5001/api', // Make sure this URL matches your Flask backend URL
});

export default api;