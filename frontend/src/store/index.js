import { createStore } from 'vuex';

import products from './products';
import customers from './customers';

export default createStore({
  modules: {
    products,
    customers,
  },
});
