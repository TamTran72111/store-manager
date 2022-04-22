export default {
  fetchStaff(state, staff) {
    state.staff = staff;
  },
  addStaff(state, staff) {
    state.staff.push(staff);
  },
  setEditingStaff(state, id) {
    state.editingStaff = state.staff.find((staff) => staff.id === id);
  },
  editStaff(state, payload) {
    state.staff = state.staff.map((staff) => {
      if (staff.id !== state.editingStaff?.id) {
        return staff;
      }
      return { ...staff, ...payload };
    });
    state.editingStaff = { ...state.editingStaff, ...payload };
  },
};
