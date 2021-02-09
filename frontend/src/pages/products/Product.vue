<template>
  <h3 class="title is-3 has-text-centered">{{ t("products.detailTitle") }}</h3>
  <table class="table is-bordered">
    <tbody>
      <tr>
        <th>{{ t("products.name") }}</th>
        <td class="has-text-centered">
          <strong>{{ product?.name }}</strong>
        </td>
      </tr>
      <tr>
        <th>{{ t("products.description") }}</th>
        <td>{{ product?.description }}</td>
      </tr>
    </tbody>
  </table>
  <Units :productId="product?.id" :units="product?.units" />
</template>

<script>
import { useStore } from "vuex";
import { useRoute } from "vue-router";
import { computed, onBeforeMount } from "vue";

import Units from "../../components/units/Units.vue";

export default {
  components: { Units },
  inject: ["t"],
  setup() {
    const route = useRoute();
    const store = useStore();

    onBeforeMount(() => {
      store.dispatch("products/fetchProduct", route.params.id);
    });

    const product = computed(() => {
      return store.getters["products/product"];
    });
    return { product };
  },
};
</script>

<style scoped>
table.table th {
  width: 160px;
  padding-left: 25px;
  vertical-align: middle;
}
</style>