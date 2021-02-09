import { createRouter, createWebHistory } from 'vue-router';

import Products from './pages/products/Products.vue';
import AddProduct from './pages/products/AddProduct.vue';
import Product from './pages/products/Product.vue';

const routes = [
  { path: '/', name: 'home', component: Products },
  { path: '/products', name: 'products', component: Products },
  {
    path: '/products/add',
    name: 'product-add',
    component: AddProduct,
  },
  { path: '/products/:id', name: 'droduct-detail', component: Product },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
