export default {
  fetchCustomers(state, customers) {
    state.customers = customers;
  },
  fetchCustomer(state, customer) {
    state.customer = customer;
  },
};
