<template>
  <BaseModal title="Thông tin khách hàng" @close="close">
    <table class="table is-bordered">
      <tbody>
        <tr>
          <th>{{ t("customers.table.phone") }}</th>
          <td class="has-text-centered">
            <strong>{{ phone }}</strong>
          </td>
        </tr>
        <tr>
          <th>{{ t("customers.table.address") }}</th>
          <td>
            <span>{{ address }}</span>
          </td>
        </tr>
      </tbody>
    </table>
  </BaseModal>
</template>

<script>
import BaseModal from "../ui/BaseModal.vue";

export default {
  emits: ["close"],
  inject: ["t"],
  props: ["address", "phone"],
  components: { BaseModal },
  setup(_, context) {
    const close = () => {
      context.emit("close");
    };

    return { close };
  },
};
</script>


<style scoped>
table.table {
  width: auto;
}
table.table th,
table.table td {
  min-width: 200px;
  text-align: center;
}
</style>