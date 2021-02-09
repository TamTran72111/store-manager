<template>
  <tr>
    <td>
      <router-link :to="'/'"
        ><span>{{ customer.name }}</span></router-link
      >
    </td>
    <td class="has-text-center">
      <span>{{ customer.phone }}</span>
    </td>
    <td class="ellipsis">
      <span>{{ customer.address }}</span>
    </td>
    <td class="has-text-right">{{ parseFloat(customer.debt).toFixed(2) }}</td>
  </tr>
</template>

<script>
export default {
  props: ["customer"],
};
</script>


<style scoped>
.ellipsis {
  position: relative;
}
.ellipsis:before {
  content: "&nbsp;";
  visibility: hidden;
}
.ellipsis span {
  position: absolute;
  left: 8px;
  right: 8px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

a.ellipsis span {
  left: 0px;
}
</style>