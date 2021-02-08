import { createRouter, createWebHistory } from 'vue-router';

import Products from './pages/Products.vue';
import AddProduct from './pages/products/AddProduct.vue';

const routes = [
  { path: '/', name: 'home', component: Products },
  { path: '/products', name: 'products', component: Products },
  {
    path: '/products/add',
    name: 'product-add',
    component: AddProduct,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;