import { createRouter, createWebHistory } from 'vue-router';

import products from './products';
import customers from './customers';
import orders from './orders';

const routes = [];

routes.push(...products);
routes.push(...customers);
routes.push(...orders);

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
