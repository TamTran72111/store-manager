export default {
  customers(state) {
    return state.customers;
  },
  customer(state) {
    return state.customer;
  },
  customerName(state) {
    return state.customer?.name ?? '';
  },
  customerId(state) {
    return state.customer?.id;
  },
};
