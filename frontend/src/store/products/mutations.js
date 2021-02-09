export default {
  fetchProducts(state, products) {
    state.products = products;
  },
  fetchProduct(state, product) {
    state.product = product;
  },
  addUnit(state, unit) {
    state.product.units.push(unit);
  },
};
