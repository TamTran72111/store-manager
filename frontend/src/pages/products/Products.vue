<template>
  <div class="products-page">
    <div class="has-text-right">
      <router-link
        :to="{ name: 'product-add' }"
        class="button is-primary is-outlined"
        >Add Product</router-link
      >
    </div>
    <ProductList />
  </div>
</template>

<script>
import ProductList from "../../components/products/ProductList.vue";

export default {
  components: { ProductList },
};
</script>

<style scoped>
.products-page {
  width: 80vw;
  max-width: 800px;
  margin: auto;
}
</style>