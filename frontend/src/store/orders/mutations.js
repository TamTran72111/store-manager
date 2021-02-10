export default {
  fetchOrders(state, orders) {
    state.orders = orders;
  },
  fetchOrder(state, order) {
    state.order = order;
  },
  editOrder(state, payload) {
    state.order = { ...state.order, ...payload };
  },
};
