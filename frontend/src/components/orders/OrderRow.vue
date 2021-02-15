<template>
  <tr>
    <td>
      <router-link :to="{ name: 'order-detail', params: { id: order.id } }"
        ><span>{{ order.customer_name }}</span></router-link
      >
    </td>
    <td class="has-text-centered">
      <span>{{ new Date(order.created_at).toLocaleDateString() }}</span>
    </td>
    <td class="has-text-right">
      <span>{{ total.toFixed(2) }}</span>
    </td>
    <td class="has-text-centered">{{ t(`orders.status.${order.status}`) }}</td>
  </tr>
</template>

<script>
import { computed } from "vue";
export default {
  props: ["order"],
  inject: ["t"],
  setup(props) {
    const subtotal = computed(() => {
      return parseFloat(props.order.subtotal);
    });

    const total = computed(() => {
      return subtotal.value + parseFloat(props.order.debt);
    });

    return {
      total,
    };
  },
};
</script>

