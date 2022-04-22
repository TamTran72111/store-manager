import api from '../../api';
import router from '../../router';

export default {
  async fetchProducts({ commit }, params = {}) {
    const response = await api.products.fetchAll(params);
    commit('fetchProducts', response.data);
  },
  async fetchProduct({ commit }, id) {
    const response = await api.products.fetchOneById(id);
    commit('fetchProduct', response.data);
  },
  async addProduct(_, payload) {
    const response = await api.products.add(payload);
    router.push(`/products/${response.data.id}`);
  },
  async editProduct({ commit, getters }, payload) {
    await api.products.updateById(getters.productId, payload);
    commit('editProduct', payload);
  },
  async activateProduct({ commit, getters }) {
    await api.products.activateProduct(getters.productId);
    commit('activateProduct');
  },
  async deactivateProduct({ commit, getters }) {
    await api.products.deactivateProduct(getters.productId);
    commit('deactivateProduct');
  },
  /********************************************************************/
  async addUnit({ commit }, payload) {
    const response = await api.products.addUnit(payload);
    commit('addUnit', response.data);
  },
  async editUnit({ commit }, { unitId, payload }) {
    await api.products.updateUnitById(unitId, payload);
    commit('editUnit', { unitId, payload });
  },
  async activateUnit({ commit }, unitId) {
    await api.products.activateUnit(unitId);
    commit('activateUnit', unitId);
  },
  async deactivateUnit({ commit }, unitId) {
    await api.products.deactivateUnit(unitId);
    commit('deactivateUnit', unitId);
  },
};
