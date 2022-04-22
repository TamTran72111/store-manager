<template>
  <div class="table-page">
    <div class="has-text-right">
      <router-link
        :to="{ name: 'staff-add' }"
        class="button is-info is-outlined"
        >Thêm Nhân Viên</router-link
      >
    </div>
    <StaffList />
  </div>
</template>

<script>
import StaffList from "../../components/staff/StaffList.vue";

export default {
  components: { StaffList },
  inject: ["t", "websiteTitle"],
  created() {
    document.title = "Nhân Viên - " + this.websiteTitle;
  },
};
</script>

