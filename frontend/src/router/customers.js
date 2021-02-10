import Customers from '../pages/customers/Customers.vue';
import Customer from '../pages/customers/Customer.vue';
import AddCustomer from '../pages/customers/AddCustomer.vue';

export default [
  { path: '/customers', name: 'customers', component: Customers },
  {
    path: '/customers/add',
    name: 'customer-add',
    component: AddCustomer,
  },
  { path: '/customers/:id', name: 'customer-detail', component: Customer },
];
