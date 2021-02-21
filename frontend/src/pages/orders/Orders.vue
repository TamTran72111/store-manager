<template>
  <div class="table-page">
    <div class="has-text-right">
      <router-link
        :to="{ name: 'order-add' }"
        class="button is-primary is-outlined"
        >{{ t("orders.addButton") }}</router-link
      >
    </div>
    <OrderSearch />
    <OrderList />
  </div>
</template>

<script>
import { onBeforeMount } from "vue";
import { useStore } from "vuex";

import OrderList from "../../components/orders/OrderList.vue";
import OrderSearch from "../../components/orders/OrderSearch.vue";

export default {
  components: { OrderList, OrderSearch },
  inject: ["t"],
  setup() {
    const store = useStore();

    onBeforeMount(() => {
      store.dispatch("orders/fetchOrders");
    });
  },
};
</script>

