<template>
  <h5 class="title is-5 has-text-centered">{{ t("orders.details.title") }}</h5>
  <table class="table is-bordered">
    <thead>
      <tr class="has-text-centered">
        <th>{{ t("products.name") }}</th>
        <th>{{ t("products.table.unit") }}</th>
        <th class="hide-on-small">{{ t("products.table.price") }}</th>
        <th>{{ t("orders.details.quantity") }}</th>
        <th class="hide-on-small">{{ t("orders.details.discount") }}</th>
        <th>{{ t("orders.details.cost") }}</th>
        <th style="width: 50px">{{ t("orders.details.edit") }}</th>
      </tr>
    </thead>
    <tbody>
      <OrderDetail
        v-for="detail in details"
        :key="detail.id"
        :detail="detail"
      />
    </tbody>
  </table>
  <div class="has-text-centered has-text-primary is-size-2">
    <span @click="toggleAdd" :title="t('orders.details.add')" class="icon"
      ><i class="fas fa-plus-circle"></i
    ></span>
  </div>
  <OrderDetailModal
    v-if="showAdd"
    :title="t('orders.details.add')"
    @close="toggleAdd"
    @save="addDetail"
  />
</template>

<script>
import { ref } from "vue";
import { useStore } from "vuex";

import RequiredInput from "../ui/RequiredInput.vue";
import OrderDetail from "./OrderDetail.vue";
import OrderDetailModal from "./OrderDetailModal.vue";

export default {
  components: { RequiredInput, OrderDetail, OrderDetailModal },
  props: ["orderId", "details"],
  inject: ["t"],
  setup(props) {
    const name = ref("");
    const price = ref(0);
    const showAdd = ref(false);
    const store = useStore();

    const toggleAdd = () => {
      showAdd.value = !showAdd.value;
    };
    const click = async () => {
      await store.dispatch("products/addOrderDetail", {
        product: props.productId,
        name: name.value,
        price: price.value,
      });
      name.value = "";
      price.value = 0;
    };

    const addDetail = async (payload) => {
      await store.dispatch("orders/addDetail", {
        order: props.orderId,
        ...payload,
      });
      showAdd.value = false;
    };

    return { name, price, showAdd, toggleAdd, click, addDetail };
  },
};
</script>

<style scoped>
h5.title {
  margin-top: 1rem;
}
table.table {
  width: 96vw;
  max-width: 1000px;
}
span.icon {
  cursor: pointer;
}
</style>