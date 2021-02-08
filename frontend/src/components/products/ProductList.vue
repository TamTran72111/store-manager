<template>
  <h4 class="title is-4 has-text-centered mt-2">Product List</h4>
  <table class="table is-bordered mb-5">
    <thead>
      <tr>
        <th>Product</th>
        <th>Unit</th>
        <th>Price</th>
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
