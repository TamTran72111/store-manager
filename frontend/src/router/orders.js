import Orders from '../pages/orders/Orders.vue';
import Order from '../pages/orders/Order.vue';

export default [
  { path: '/orders', name: 'orders', component: Orders },
  { path: '/orders/:id', name: 'order-detail', component: Order },
];
