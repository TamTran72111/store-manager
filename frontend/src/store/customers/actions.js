import api from '../../api';

export default {
  async fetchCustomers({ commit }, searchName = '') {
    const response = await api.customers.fetchAll(searchName);
    commit('fetchCustomers', response.data);
  },
  async fetchCustomer({ commit }, id) {
    const response = await api.customers.fetchOneById(id);
    commit('fetchCustomer', response.data);
  },
  async editCustomer({ commit, getters }, payload) {
    await api.customers.updateById(getters.customerId, payload);
    commit('editCustomer', payload);
  },
};
