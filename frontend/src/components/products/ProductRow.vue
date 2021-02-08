<template>
  <tr>
    <td :rowspan="rowSpan" class="product-name">
      {{ product.name }}
    </td>
    <td>{{ firstUnit?.name || "" }}</td>
    <td class="has-text-right">{{ firstUnit?.price || "" }}</td>
  </tr>
  <tr v-for="unit in otherUnits" :key="unit.id">
    <td>{{ unit.name }}</td>
    <td class="has-text-right">{{ unit.price }}</td>
  </tr>
</template>

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

    return {
      firstUnit,
      otherUnits,
      rowSpan,
    };
  },
};
</script>

<style scoped>
td.product-name {
  vertical-align: middle;
}
</style>