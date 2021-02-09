<template>
  <div class="product-search">
    <DebounceInput
      type="text"
      v-model="searchName"
      :label="t('products.search')"
      :placeholder="t('products.searchPlaceholder')"
    />
  </div>
</template>

<script>
import { ref, watch } from "vue";
import { useStore } from "vuex";

import DebounceInput from "../../components/ui/DebounceInput.vue";

export default {
  components: { DebounceInput },
  inject: ["t"],
  setup() {
    const searchName = ref("");
    const store = useStore();

    watch(searchName, () => {
      store.dispatch("products/fetchProducts", searchName.value);
    });
    return { searchName };
  },
};
</script>

<style scoped>
.product-search {
  margin-top: 1rem;
  margin-bottom: 1rem;
}
</style>