export default {
  products(state) {
    return state.products;
  },
  product(state) {
    return state.product;
  },
  productId(state) {
    return state.product?.id;
  },
};
