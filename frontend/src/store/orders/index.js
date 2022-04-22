import getters from "./getters";
import mutations from "./mutations";
import actions from "./actions";

export default {
  namespaced: true,
  state() {
    return {
      orders: [],
      order: null,
      customer: null,
      payments: [],
    };
  },
  getters,
  mutations,
  actions,
};
