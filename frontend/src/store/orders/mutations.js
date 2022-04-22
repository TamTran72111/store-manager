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
    const isReady = state.order.details.every((detail) => detail.ready);
    const isOrdered = state.order.details.every((detail) => !detail.ready);
    if (isReady) {
      state.order.status = "r";
    } else if (isOrdered) {
      state.order.status = "o";
    } else {
      state.order.status = "p";
    }
  },
  pay(state, payment) {
    state.payments.unshift(payment);
    state.order.payment += parseFloat(payment.amount);
  },
  fetchPayments(state, payments) {
    state.payments = payments;
  },
};
