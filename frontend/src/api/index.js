import axios from 'axios';
const instance = axios.create({
  baseURL: 'http://localhost:8000/api/',
});

export default {
  fetchProducts(searchName) {
    return instance.get(`products/?name=${searchName}`);
  },
  addProduct(payload) {
    return instance.post('products/', payload);
  },
  fetchProduct(id) {
    return instance.get(`products/${id}/`);
  },
  activateProduct(id) {
    return instance.patch(`products/${id}/`, { active: true });
  },
  deactivateProduct(id) {
    return instance.patch(`products/${id}/`, { active: false });
  },
  editProduct(id, payload) {
    return instance.patch(`products/${id}/`, payload);
  },
  deleteProduct(id) {
    return instance.delete(`products/${id}/`);
  },
  addUnit(payload) {
    return instance.post('units/', payload);
  },
  activateUnit(id) {
    return instance.patch(`units/${id}/`, { active: true });
  },
  deactivateUnit(id) {
    return instance.patch(`units/${id}/`, { active: false });
  },
  editUnit(id, unit) {
    return instance.patch(`units/${id}/`, unit);
  },
};
