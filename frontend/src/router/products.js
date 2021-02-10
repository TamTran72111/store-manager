import Products from '../pages/products/Products.vue';
import AddProduct from '../pages/products/AddProduct.vue';
import Product from '../pages/products/Product.vue';

export default [
  { path: '/', name: 'home', component: Products },
  { path: '/products', name: 'products', component: Products },
  {
    path: '/products/add',
    name: 'product-add',
    component: AddProduct,
  },
  { path: '/products/:id', name: 'product-detail', component: Product },
];
