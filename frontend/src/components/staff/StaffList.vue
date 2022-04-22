<template>
  <h4 class="title is-4 has-text-centered mt-2">Danh sách Nhân Viên</h4>
  <table class="table is-bordered mb-5">
    <thead>
      <tr class="has-text-centered">
        <th>Tên Nhân Viên</th>
        <th>Đang làm</th>
      </tr>
    </thead>
    <tbody>
      <StaffRow
        v-for="staffDetail in staff"
        :key="staffDetail.id"
        :staffDetail="staffDetail"
      />
    </tbody>
  </table>
</template>

<script>
import { computed, onBeforeMount } from "vue";
import { useStore } from "vuex";

import StaffRow from "./StaffRow.vue";

export default {
  components: { StaffRow },
  inject: ["t"],
  setup() {
    const store = useStore();

    onBeforeMount(() => {
      store.dispatch("staff/fetchStaff");
    });

    const staff = computed(() => {
      return store.getters["staff/staff"];
    });

    return { staff };
  },
};
</script>
