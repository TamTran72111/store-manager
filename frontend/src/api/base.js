import axios from './axios';

class BaseAPI {
  constructor(baseEndpoint) {
    this.BASE_ENDPOINT = baseEndpoint;
  }

  fetchAll(searchName, extraQueries = '') {
    return axios.get(
      `${this.BASE_ENDPOINT}/?name=${searchName}${extraQueries}`
    );
  }
  fetchOneById(id) {
    return axios.get(`${this.BASE_ENDPOINT}/${id}/`);
  }
  add(payload) {
    return axios.post(`${this.BASE_ENDPOINT}/`, payload);
  }
  updateById(id, payload) {
    return axios.patch(`${this.BASE_ENDPOINT}/${id}/`, payload);
  }
}

export default BaseAPI;
