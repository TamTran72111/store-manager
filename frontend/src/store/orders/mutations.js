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
  fetchOrderCusomer(state, customer) {
    state.customer = customer;
  },
  addDetail(state, detail) {
    state.order.details.push(detail);
  },
  editDetail(state, { id, detail }) {
    state.order.details = state.order.details.map((detail_) => {
      if (detail_.id === id) {
        return detail;
      } else {
        return detail_;
      }
    });
  },
};
