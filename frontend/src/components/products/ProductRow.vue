<template>
  <tr>
    <td :rowspan="rowSpan" class="product-name">
      <router-link :to="toLink">{{ product.name }}</router-link>
    </td>
    <td>{{ firstUnit?.name || "" }}</td>
    <td class="has-text-right">{{ firstUnit?.price || "" }}</td>
  </tr>
  <tr v-for="unit in otherUnits" :key="unit.id">
    <td>{{ unit.name }}</td>
    <td class="has-text-right">{{ unit.price }}</td>
  </tr>
</template>
0
<script>
import { computed } from "vue";
export default {
  props: ["product"],
  setup(props) {
    const firstUnit = computed(() => {
      return props.product.units[0];
    });
    const otherUnits = computed(() => {
      return props.product.units.slice(1);
    });
    const rowSpan = computed(() => {
      return Math.max(props.product.units.length, 1);
    });

    const toLink = computed(() => {
      return {
        name: "product-detail",
        params: { id: props.product.id },
      };
    });

    return {
      firstUnit,
      otherUnits,
      rowSpan,
      toLink,
    };
  },
};
</script>

<style scoped>
td.product-name {
  vertical-align: middle;
}
</style>