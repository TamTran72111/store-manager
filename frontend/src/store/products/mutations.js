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
  activateUnit(state, unitId) {
    state.product.units.forEach((unit) => {
      if (unitId === unit.id) {
        unit.active = true;
      }
    });
  },
  deactivateUnit(state, unitId) {
    state.product.units.forEach((unit) => {
      if (unitId === unit.id) {
        unit.active = false;
      }
    });
  },
  editUnit(state, { unitId, payload }) {
    state.product.units = state.product.units.map((unit) => {
      if (unitId === unit.id) {
        return {
          ...unit,
          ...payload,
        };
      }
      return unit;
    });
  },
};
