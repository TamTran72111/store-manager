import Staff from "../pages/staff/Staff.vue";
import StaffDetail from "../pages/staff/StaffDetail.vue";
import AddStaff from "../pages/staff/AddStaff.vue";

export default [
  { path: "/staff", name: "staff", component: Staff },
  { path: "/staff/add", name: "staff-add", component: AddStaff },
  { path: "/staff/:id", name: "staff-detail", component: StaffDetail },
];
