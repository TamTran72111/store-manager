<template>
  <ListSearch
    placeholder="products.searchPlaceholder"
    actionName="products/fetchProducts"
  />
</template>

<script>
import ListSearch from "../ListSearch.vue";

export default {
  components: { ListSearch },
};
</script>

