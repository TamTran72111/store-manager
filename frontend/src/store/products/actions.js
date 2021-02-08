import api from '../../api';

export default {
  async fetchProducts({ commit }) {
    const response = await api.fetchProducts();
    commit('fetchProducts', response.data);
  },
};
