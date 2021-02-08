import { createRouter, createWebHistory } from 'vue-router';

import Product from './components/products/Product.vue';

const routes = [{ path: '/', name: 'home', component: Product }];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
