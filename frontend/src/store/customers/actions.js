import api from '../../api';
import router from '../../router';

export default {
  async fetchCustomers({ commit }, params = {}) {
    const response = await api.customers.fetchAll(params);
    commit('fetchCustomers', response.data);
  },
  async fetchCustomer({ commit }, id) {
    const response = await api.customers.fetchOneById(id);
    commit('fetchCustomer', response.data);
  },
  async addCustomer(_, payload) {
    const response = await api.customers.add(payload);
    router.push({ name: 'customer-detail', params: { id: response.data.id } });
  },
  async editCustomer({ commit, getters }, payload) {
    await api.customers.updateById(getters.customerId, payload);
    commit('editCustomer', payload);
  },
};
