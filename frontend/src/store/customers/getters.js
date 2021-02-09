export default {
  customers(state) {
    return state.customers;
  },
  customer(state) {
    return state.customer;
  },
  customerId(state) {
    return state.customer?.id;
  },
};
