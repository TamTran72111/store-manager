<template>
  <div class="table-page">
    <div class="has-text-right">
      <router-link
        :to="{ name: 'product-add' }"
        class="button is-info is-outlined"
        >{{ t("products.addButton") }}</router-link
      >
    </div>
    <ProductSearch />
    <ProductList />
  </div>
</template>

<script>
import ProductList from "../../components/products/ProductList.vue";
import ProductSearch from "../../components/products/ProductSearch.vue";

export default {
  components: { ProductList, ProductSearch },
  inject: ["t", "websiteTitle"],
  created() {
    document.title = "Hàng Hóa - " + this.websiteTitle;
  },
};
</script>

