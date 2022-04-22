<template>
  <BaseModal title="Thông tin thanh toán" @close="close">
    <table class="table is-bordered">
      <thead>
        <tr class="has-text-centered">
          <th>Ngày</th>
          <th>Tên Người Nhận</th>
          <th>Số Tiền</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="payment in payments" :key="payment.id">
          <td>{{ payment.created_at }}</td>
          <td>{{ payment.staff_name }}</td>
          <td>
            <strong>{{
              n(parseFloat(payment.amount || 0), "currency")
            }}</strong>
          </td>
        </tr>
      </tbody>
    </table>
  </BaseModal>
</template>

<script>
import { computed } from "vue";
import { useStore } from "vuex";

import BaseModal from "../ui/BaseModal.vue";

export default {
  emits: ["close"],
  inject: ["n"],
  components: { BaseModal },
  setup(_, context) {
    const store = useStore();
    const close = () => {
      context.emit("close");
    };

    const payments = computed(() => {
      return store.getters["orders/payments"];
    });

    return { close, payments };
  },
};
</script>


<style scoped>
table.table {
  width: auto;
}
table.table th,
table.table td {
  min-width: 200px;
  text-align: center;
}
</style>