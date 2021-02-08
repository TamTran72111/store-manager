import axios from 'axios';
const instance = axios.create({
  baseURL: 'http://localhost:8000/api/',
});

export default {
  fetchProducts() {
    return instance.get('products/');
  },
  addProduct(payload) {
    return instance.post('products/', payload);
  },
};