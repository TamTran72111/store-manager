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
                v-model="amount"
              />
            </td>
          </tr>
          <tr>
            <th>Người Nhận</th>
            <td>
              <div
                class="select is-success"
                :class="{ 'is-danger': staffId === 0 }"
              >
                <select v-model="staffId">
                  <option :value="0">Chọn người nhận</option>
                  <option
                    v-for="staff_ in staff"
                    :key="staff_.id"
                    :value="staff_.id"
                  >
                    {{ staff_.name }}
                  </option>
                </select>
              </div>
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
  props: ["orderId"],
  components: { BaseModal, Currency },
  setup({ orderId }, context) {
    const store = useStore();
    const amount = ref(0);
    const staffId = ref(0);

    const close = () => {
      context.emit("close");
    };

    const staff = computed(() => {
      return store.getters["staff/activeStaff"];
    });

    onMounted(async () => {
      // payment.value = store.getters["orders/payment"];
      await store.dispatch("staff/fetchStaff");
    });

    const save = async () => {
      await store.dispatch("orders/pay", {
        amount: amount.value,
        order: orderId,
        staff: staffId.value,
      });
      close();
    };
    const isInvalid = computed(() => {
      return parseInt(amount.value) <= 0 || !staffId.value;
    });

    return {
      save,
      close,
      amount,
      staff,
      staffId,
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