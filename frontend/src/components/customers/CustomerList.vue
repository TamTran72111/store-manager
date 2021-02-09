<template>
  <h4 class="title is-4 has-text-centered mt-2">{{ t("customers.list") }}</h4>
  <table class="table is-bordered mb-5">
    <thead>
      <tr class="has-text-centered">
        <th>{{ t("customers.table.customer") }}</th>
        <th style="width: 110px">{{ t("customers.table.phone") }}</th>
        <th>{{ t("customers.table.address") }}</th>
        <th style="width: 130px">{{ t("customers.table.debt") }}</th>
      </tr>
    </thead>
    <tbody>
      <CustomerRow
        v-for="customer in customers"
        :key="customer.id"
        :customer="customer"
      />
    </tbody>
  </table>
</template>

<script>
import { computed, onBeforeMount } from "vue";
import { useStore } from "vuex";

import CustomerRow from "./CustomerRow.vue";

export default {
  components: { CustomerRow },
  inject: ["t"],
  setup() {
    const store = useStore();

    onBeforeMount(() => {
      store.dispatch("customers/fetchCustomers");
    });

    const customers = computed(() => {
      return store.getters["customers/customers"];
    });

    return { customers };
  },
};
</script>


