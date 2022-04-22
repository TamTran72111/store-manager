import axios from 'axios';

const hostname = window.location.hostname || 'localhost';
const instance = axios.create({
  baseURL: `http://${hostname}:8000/api/`,
});

export default instance;
