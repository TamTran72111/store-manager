<template>
  <tr>
    <td>
      <span
        class="icon has-text-primary"
        v-if="detail.ready"
        :title="t('orders.details.ready')"
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
      <span :title="t('edit')" @click="toggleEdit" class="icon"
        ><i class="fas fa-pen"></i
      ></span>
    </td>
  </tr>
  <OrderDetailModal
    v-if="showEdit"
    :title="t('orders.details.')"
    :detail="detail"
    @close="toggleEdit"
    @save="edit"
  />
</template>

<script>
import { ref } from "vue";
import { useStore } from "vuex";

import OrderDetailModal from "./OrderDetailModal.vue";

export default {
  components: { OrderDetailModal },
  props: ["detail"],
  inject: ["t"],
  setup(props) {
    const showEdit = ref(false);
    const store = useStore();

    const toggleEdit = () => {
      showEdit.value = !showEdit.value;
    };

    const edit = async (payload) => {
      await store.dispatch("orders/editDetail", {
        id: props.detail.id,
        payload,
      });
      showEdit.value = false;
    };

    return { showEdit, toggleEdit, edit };
  },
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

