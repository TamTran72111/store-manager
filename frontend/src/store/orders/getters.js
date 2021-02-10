export default {
  orders(state) {
    return state.orders;
  },
  order(state) {
    return state.order;
  },
  orderId(state) {
    return state.order?.id;
  },
  customer(state) {
    return state.customer;
  },
};
