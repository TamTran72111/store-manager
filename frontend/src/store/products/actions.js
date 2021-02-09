import api from '../../api';
import router from '../../router';

export default {
  async fetchProducts({ commit }) {
    const response = await api.fetchProducts();
    commit('fetchProducts', response.data);
  },
  async addProduct(_, payload) {
    const response = await api.addProduct(payload);
    router.push(`/products/${response.data.id}`);
  },
  async fetchProduct({ commit }, id) {
    const response = await api.fetchProduct(id);
    commit('fetchProduct', response.data);
  },
  async activateProduct({ commit, getters }) {
    await api.activateProduct(getters.productId);
    commit('activateProduct');
  },
  async deactivateProduct({ commit, getters }) {
    await api.deactivateProduct(getters.productId);
    commit('deactivateProduct');
  },
  async editProduct({ commit, getters }, payload) {
    await api.editProduct(getters.productId, payload);
    commit('editProduct', payload);
  },
  async addUnit({ commit }, payload) {
    const response = await api.addUnit(payload);
    console.log(response.data);
    commit('addUnit', response.data);
  },
  async activateUnit({ commit }, unitId) {
    await api.activateUnit(unitId);
    commit('activateUnit', unitId);
  },
  async deactivateUnit({ commit }, unitId) {
    await api.deactivateUnit(unitId);
    commit('deactivateUnit', unitId);
  },
  async editUnit({ commit }, { unitId, payload }) {
    await api.editUnit(unitId, payload);
    commit('editUnit', { unitId, payload });
  },
};
