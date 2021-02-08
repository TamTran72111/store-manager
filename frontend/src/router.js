import { createRouter, createWebHistory } from 'vue-router';

import Products from './pages/Products.vue';

const routes = [
  { path: '/', name: 'home', component: Products },
  { path: '/products', name: 'products', component: Products },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
