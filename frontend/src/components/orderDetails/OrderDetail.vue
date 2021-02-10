<template>
  <tr>
    <td>
      <span class="icon has-text-primary" v-if="detail.ready"
        ><i class="fas fa-check"></i
      ></span>
      <span>{{ detail.product_name }}</span>
    </td>
    <td class="has-text-centered">
      <span>{{ detail.unit_name }}</span>
    </td>

    <td class="has-text-right hide-on-small">{{ detail.price }}</td>
    <td class="has-text-right">{{ detail.quantity }}</td>
    <td class="has-text-right hide-on-small">{{ detail.discount }}</td>
    <td class="has-text-right">{{ detail.cost }}</td>
    <td class="has-text-centered has-text-info">
      <span :title="t('edit')" class="icon"><i class="fas fa-pen"></i></span>
    </td>
  </tr>
</template>

<script>
export default {
  props: ["detail"],
  inject: ["t"],
};
</script>

<style scoped>
span.icon {
  cursor: pointer;
}

.v-align {
  vertical-align: middle;
}
</style>

