<template>
  <ListSearch
    placeholder="customers.searchPlaceholder"
    actionName="customers/fetchCustomers"
  />
</template>

<script>
import ListSearch from "../ListSearch.vue";

export default {
  components: { ListSearch },
};
</script>

