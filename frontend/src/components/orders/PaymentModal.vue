<template>
  <BaseModal :title="t('orders.payment.title')" @close="close">
    <form @submit.prevent="save">
      <table class="table is-bordered">
        <tbody>
          <tr>
            <th>{{ t("orders.payment.payment") }}</th>
            <td>
              <Currency
                :placeholder="t('orders.paymentPlaceholder')"
                v-model="payment"
              />
            </td>
          </tr>
        </tbody>
      </table>

      <div class="field is-grouped is-justify-content-center">
        <div class="control">
          <button type="submit" :disabled="isInvalid" class="button is-link">
            {{ t("save") }}
          </button>
        </div>
        <div class="control">
          <button
            type="button"
            @click.stop="close"
            class="button is-link is-light"
          >
            {{ t("cancel") }}
          </button>
        </div>
      </div>
    </form></BaseModal
  >
</template>

<script>
import { computed, onMounted, ref } from "vue";
import { useStore } from "vuex";

import BaseModal from "../ui/BaseModal.vue";
import Currency from "../ui/Currency.vue";

export default {
  emits: ["close"],
  inject: ["t"],
  components: { BaseModal, Currency },
  setup(_, context) {
    const store = useStore();
    const payment = ref(0);

    const close = () => {
      context.emit("close");
    };

    onMounted(() => {
      payment.value = store.getters["orders/payment"];
    });

    const save = async () => {
      await store.dispatch("orders/editOrder", {
        payment: payment.value,
      });
      close();
    };
    const isInvalid = computed(() => {
      return !(payment.value >= 0);
    });

    return {
      save,
      close,
      payment,
      isInvalid,
    };
  },
};
</script>


<style scoped>
table.table {
  width: auto;
}
table.table th {
  min-width: 200px;
  text-align: center;
}
.old-payment {
  padding-right: 39px;
}
</style>