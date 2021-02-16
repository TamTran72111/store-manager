import { createRouter, createWebHistory } from 'vue-router';

import products from './products';
import customers from './customers';
import orders from './orders';
import Settings from '../pages/Settings.vue';

const routes = [];

routes.push(...products);
routes.push(...customers);
routes.push(...orders);
routes.push({ path: '/settings', name: 'settings', component: Settings });

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
