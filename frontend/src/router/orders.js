import Orders from '../pages/orders/Orders.vue';
import Order from '../pages/orders/Order.vue';
import AddOrder from '../pages/orders/AddOrder.vue';

export default [
  { path: '/orders', name: 'orders', component: Orders },
  { path: '/orders/add', name: 'order-add', component: AddOrder },
  { path: '/orders/:id', name: 'order-detail', component: Order },
];
