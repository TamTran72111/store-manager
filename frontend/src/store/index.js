import { createStore } from 'vuex';

import products from './products';
import customers from './customers';
import orders from './orders';

export default createStore({
  modules: {
    products,
    customers,
    orders,
  },
});
