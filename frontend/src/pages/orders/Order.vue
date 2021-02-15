<template>
  <h3 class="title is-3 has-text-centered">{{ t("orders.detailTitle") }}</h3>
  <table class="table is-bordered">
    <tbody>
      <tr>
        <th>{{ t("customers.table.customer") }}</th>
        <td class="has-text-centered">
          <router-link
            :to="{ name: 'customer-detail', params: { id: customer?.id } }"
            >{{ customer?.name }}</router-link
          >
        </td>
      </tr>
      <tr>
        <th>{{ t("customers.table.phone") }}</th>
        <td class="has-text-centered">
          <strong>{{ customer?.phone }}</strong>
        </td>
      </tr>
      <tr>
        <th>{{ t("customers.table.address") }}</th>
        <td>
          <span>{{ customer?.address }}</span>
        </td>
      </tr>

      <tr>
        <th>{{ t("customers.table.debt") }}</th>
        <td class="has-text-centered">
          <strong>{{ parseFloat(order?.debt).toFixed(2) }}</strong>
        </td>
      </tr>
      <tr>
        <th>{{ t("orders.table.subtotal") }}</th>
        <td class="has-text-centered">
          <strong>{{ subtotal.toFixed(2) }}</strong>
        </td>
      </tr>
      <tr>
        <th>{{ t("orders.table.total") }}</th>
        <td class="has-text-centered">
          <strong>{{ total.toFixed(2) }}</strong>
        </td>
      </tr>

      <tr>
        <th>{{ t("orders.table.status") }}</th>
        <td class="has-text-centered">
          <strong v-if="order">{{ t(`orders.status.${order.status}`) }}</strong>
        </td>
      </tr>
    </tbody>
  </table>

  <OrderDetails v-if="order" :orderId="order.id" :details="order.details" />
</template>

<script>
import { useStore } from "vuex";
import { useRoute } from "vue-router";
import { computed, onBeforeMount, ref, watch } from "vue";

import OrderDetails from "../../components/orderDetails/OrderDetails.vue";
import RequiredInput from "../../components/ui/RequiredInput.vue";
import UnrequiredInput from "../../components/ui/UnrequiredInput.vue";

export default {
  components: { OrderDetails, RequiredInput, UnrequiredInput },
  inject: ["t"],
  setup() {
    const route = useRoute();
    const store = useStore();

    onBeforeMount(() => {
      store.dispatch("orders/fetchOrder", route.params.id);
    });

    const order = computed(() => {
      return store.getters["orders/order"];
    });

    const customer = computed(() => {
      return store.getters["orders/customer"];
    });

    const subtotal = computed(() => {
      return store.getters["orders/subtotal"];
    });

    const total = computed(() => {
      if (order.value) {
        return parseFloat(order.value.debt) + subtotal.value;
      } else {
        return 0;
      }
    });

    return {
      order,
      customer,
      subtotal,
      total,
    };
  },
};
</script>

<style scoped>
table.table th {
  width: 250px;
  padding-left: 25px;
  vertical-align: middle;
  text-align: center;
}

div.button-group {
  margin-top: 0;
  margin-bottom: 2rem;
}
div.button-group button {
  width: 100px;
}
table.table {
  margin-bottom: 3rem;
}
</style>