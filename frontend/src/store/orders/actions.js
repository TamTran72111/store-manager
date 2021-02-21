import api from '../../api';
import router from '../../router';

export default {
  async fetchOrders({ commit }, params = {}) {
    const response = await api.orders.fetchAll(params);
    commit('fetchOrders', response.data);
  },
  async fetchOrder({ commit }, id) {
    const response = await api.orders.fetchOneById(id);
    commit('fetchOrder', response.data);
    const resp = await api.customers.fetchOneById(response.data.customer);
    commit('fetchOrderCusomer', resp.data);
  },
  async addOrder(_, payload) {
    const response = await api.orders.add(payload);
    router.push({ name: 'order-detail', params: { id: response.data.id } });
  },
  async editOrder({ commit, getters }, payload) {
    await api.orders.updateById(getters.orderId, payload);
    commit('editOrder', payload);
  },
  async addDetail({ commit }, payload) {
    const response = await api.orderDetails.add(payload);
    commit('addDetail', response.data);
  },
  async editDetail({ commit }, { id, payload }) {
    const response = await api.orderDetails.updateById(id, payload);
    commit('editDetail', { id, detail: response.data });
  },
};
