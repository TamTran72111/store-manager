import axios from './axios';
import BaseAPI from './base';

class ProductAPI extends BaseAPI {
  activateProduct(id) {
    return axios.patch(`products/${id}/`, { active: true });
  }
  deactivateProduct(id) {
    return axios.patch(`products/${id}/`, { active: false });
  }
  /********************************************************************/
  addUnit(payload) {
    return axios.post('units/', payload);
  }
  updateUnitById(id, unit) {
    return axios.patch(`units/${id}/`, unit);
  }
  activateUnit(id) {
    return axios.patch(`units/${id}/`, { active: true });
  }
  deactivateUnit(id) {
    return axios.patch(`units/${id}/`, { active: false });
  }
}

export default new ProductAPI('products');
