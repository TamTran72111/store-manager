<template>
  <h4 class="title is-4 has-text-centered mt-2">{{ t("orders.list") }}</h4>
  <table class="table is-bordered mb-5">
    <thead>
      <tr class="has-text-centered">
        <th>{{ t("customers.table.customer") }}</th>
        <th>{{ t("orders.table.date") }}</th>
        <th style="width: 130px">{{ t("orders.table.total") }}</th>
        <th style="width: 130px">{{ t("orders.table.payment") }}</th>
        <th>{{ t("orders.table.status") }}</th>
      </tr>
    </thead>
    <tbody>
      <OrderRow v-for="order in orders" :key="order.id" :order="order" />
    </tbody>
  </table>
</template>

<script>
import { computed } from "vue";
import { useStore } from "vuex";

import OrderRow from "./OrderRow.vue";

export default {
  components: { OrderRow },
  inject: ["t"],
  setup() {
    const store = useStore();

    const orders = computed(() => {
      return store.getters["orders/orders"];
    });

    return { orders };
  },
};
</script>


