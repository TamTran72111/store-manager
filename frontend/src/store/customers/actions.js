import api from '../../api';

export default {
  async fetchCustomers({ commit }, searchName = '') {
    const response = await api.customers.fetchAll(searchName);
    commit('fetchCustomers', response.data);
  },
  async fetchCustomer({ commit }, id) {
    const response = await api.fetchOneById(id);
    commit('fetchCustomer', response.data);
  },
};
