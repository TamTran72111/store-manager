export default {
  staff(state) {
    return state.staff;
  },
  activeStaff(state) {
    return state.staff.filter((staff) => staff.active);
  },
  staffId(state) {
    return state.editingStaff?.id;
  },
  editingStaff(state) {
    return state.editingStaff;
  },
};
