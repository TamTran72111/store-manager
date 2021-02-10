<template>
  <ListSearch
    placeholder="orders.searchPlaceholder"
    actionName="orders/fetchOrders"
  />
</template>

<script>
import ListSearch from "../ListSearch.vue";

export default {
  components: { ListSearch },
};
</script>

