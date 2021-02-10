<template>
  <tr>
    <td>
      <router-link :to="{ name: 'orders', params: { id: order.id } }"
        ><span>{{ order.customer_name }}</span></router-link
      >
    </td>
    <td class="has-text-centered">
      <span>{{ new Date(order.created_at).toLocaleDateString() }}</span>
    </td>
    <td class="has-text-right">
      <span>{{ order.total.toFixed(2) }}</span>
    </td>
    <td class="has-text-centered">{{ t(`orders.status.${order.status}`) }}</td>
  </tr>
</template>

<script>
export default {
  props: ["order"],
  inject: ["t"],
};
</script>

