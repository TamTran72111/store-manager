import { createRouter, createWebHistory } from 'vue-router';

import Products from './pages/products/Products.vue';
import AddProduct from './pages/products/AddProduct.vue';
import Product from './pages/products/Product.vue';
import Customers from './pages/customers/Customers.vue';
import Customer from './pages/customers/Customer.vue';
import AddCustomer from './pages/customers/AddCustomer.vue';
import Orders from './pages/orders/Orders.vue';

const routes = [
  { path: '/', name: 'home', component: Products },
  { path: '/products', name: 'products', component: Products },
  {
    path: '/products/add',
    name: 'product-add',
    component: AddProduct,
  },
  { path: '/products/:id', name: 'product-detail', component: Product },
  { path: '/customers', name: 'customers', component: Customers },
  {
    path: '/customers/add',
    name: 'customer-add',
    component: AddCustomer,
  },
  { path: '/customers/:id', name: 'customer-detail', component: Customer },
  { path: '/orders', name: 'orders', component: Orders },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
