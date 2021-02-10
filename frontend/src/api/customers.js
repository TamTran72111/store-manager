import axios from './axios';

const BASE_ENDPOINT = 'customers';

export default {
  fetchAll(searchName) {
    return axios.get(`${BASE_ENDPOINT}/?name=${searchName}`);
  },
  fetchOneById(id) {
    return axios.get(`${BASE_ENDPOINT}/${id}/`);
  },
  add(payload) {
    return axios.post(`${BASE_ENDPOINT}/`, payload);
  },
  updateById(id, payload) {
    return axios.patch(`${BASE_ENDPOINT}/${id}/`, payload);
  },
};
