<template>
  <h4 class="title is-4 has-text-centered mt-2">{{ t("products.list") }}</h4>
  <table class="table is-bordered mb-5">
    <thead>
      <tr class="has-text-centered">
        <th>{{ t("products.table.product") }}</th>
        <th>{{ t("products.table.unit") }}</th>
        <th>{{ t("products.table.price") }}</th>
      </tr>
    </thead>
    <tbody>
      <ProductRow
        v-for="product in products"
        :key="product.id"
        :product="product"
      />
    </tbody>
  </table>
</template>

<script>
import { computed, onBeforeMount } from "vue";
import { useStore } from "vuex";

import ProductRow from "./ProductRow.vue";

export default {
  components: { ProductRow },
  inject: ["t"],
  setup() {
    const store = useStore();

    onBeforeMount(() => {
      store.dispatch("products/fetchProducts");
    });

    const products = computed(() => {
      return store.getters["products/products"];
    });

    return { products };
  },
};
</script>
