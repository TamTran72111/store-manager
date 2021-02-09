import axios from './axios';

export default {
  fetchAll(searchName) {
    return axios.get(`products/?name=${searchName}`);
  },
  fetchOneById(id) {
    return axios.get(`products/${id}/`);
  },
  addProduct(payload) {
    return axios.post('products/', payload);
  },
  updateProductById(id, payload) {
    return axios.patch(`products/${id}/`, payload);
  },
  activateProduct(id) {
    return axios.patch(`products/${id}/`, { active: true });
  },
  deactivateProduct(id) {
    return axios.patch(`products/${id}/`, { active: false });
  },
  /********************************************************************/
  addUnit(payload) {
    return axios.post('units/', payload);
  },
  updateUnitById(id, unit) {
    return axios.patch(`units/${id}/`, unit);
  },
  activateUnit(id) {
    return axios.patch(`units/${id}/`, { active: true });
  },
  deactivateUnit(id) {
    return axios.patch(`units/${id}/`, { active: false });
  },
};
