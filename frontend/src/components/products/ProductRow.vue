<template>
  <tr>
    <td :rowspan="rowSpan" class="product-name is-capitalized">
      <router-link :to="toLink" :class="{ deleted: !product.active }">{{
        product.name
      }}</router-link>
    </td>
    <td>{{ firstUnit?.name || "" }}</td>
    <td class="has-text-right">
      {{ firstUnit ? n(parseFloat(firstUnit.price), "currency") : "" }}
    </td>
  </tr>
  <tr v-for="unit in otherUnits" :key="unit.id">
    <td>{{ unit.name }}</td>
    <td class="has-text-right">{{ n(parseFloat(unit.price), "currency") }}</td>
  </tr>
</template>

<script>
import { computed } from "vue";
export default {
  props: ["product"],
  inject: ["n"],
  setup(props) {
    const firstUnit = computed(() => {
      if (props.product.active) {
        return props.product.units[0];
      } else {
        return undefined;
      }
    });
    const otherUnits = computed(() => {
      if (props.product.active) {
        return props.product.units.slice(1);
      } else {
        return [];
      }
    });
    const rowSpan = computed(() => {
      if (props.product.active) {
        return Math.max(props.product.units.length, 1);
      } else {
        return 1;
      }
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