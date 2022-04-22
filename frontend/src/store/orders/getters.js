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
  subtotal(state) {
    return (
      state.order?.details.reduce(
        (subtotal, detail) => subtotal + parseFloat(detail.cost),
        0
      ) || 0
    );
  },
  payment(state) {
    return state.order?.payment || 0;
  },
  hasPayment(state) {
    return state.payments.length > 0;
  },
  payments(state) {
    return state.payments;
  },
};
