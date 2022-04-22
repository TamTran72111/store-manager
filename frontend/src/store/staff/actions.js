import api from "../../api";
import router from "../../router";

export default {
  async fetchStaff({ commit }) {
    const response = await api.staff.fetchAll();
    commit("fetchStaff", response.data);
  },
  async addStaff({ commit }, payload) {
    const response = await api.staff.add(payload);
    commit("addStaff", response.data);
    router.push(`/staff/${response.data.id}`);
  },
  async editStaff({ commit, getters }, payload) {
    await api.staff.updateById(getters.staffId, payload);
    commit("editStaff", payload);
  },
};
