export default {
  fetchCustomers(state, customers) {
    state.customers = customers;
  },
  fetchCustomer(state, customer) {
    state.customer = customer;
  },
  editCustomer(state, payload) {
    state.customer = { ...state.customer, ...payload };
  },
};
