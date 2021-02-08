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
};
