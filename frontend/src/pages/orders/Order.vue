<template>
  <h3 class="title is-3 has-text-centered">{{ t("orders.detailTitle") }}</h3>
  <table class="table is-bordered">
    <tbody>
      <tr>
        <th>{{ t("customers.table.customer") }}</th>
        <td class="has-text-centered is-capitalized control has-icons-right">
          <router-link
            :to="{ name: 'customer-detail', params: { id: customer?.id } }"
            >{{ customer?.name }}</router-link
          >
          <span
            v-if="hasInfo"
            @click="toggleInfo"
            class="icon is-small is-right has-text-info clickable-icon"
          >
            <i class="fas fa-info-circle"></i>
          </span>
        </td>
      </tr>

      <tr>
        <th>{{ t("customers.table.debt") }}</th>
        <td class="has-text-centered">
          <strong>{{ n(parseFloat(order?.debt || 0), "currency") }}</strong>
        </td>
      </tr>
      <tr>
        <th>{{ t("orders.table.subtotal") }}</th>
        <td class="has-text-centered">
          <strong>{{ n(subtotal, "currency") }}</strong>
        </td>
      </tr>
      <tr>
        <th>{{ t("orders.table.total") }}</th>
        <td class="has-text-centered">
          <strong>{{ n(total, "currency") }}</strong>
        </td>
      </tr>
      <tr>
        <th>{{ t("orders.table.payment") }}</th>
        <td class="has-text-centered control has-icons-right">
          <strong>{{ n(parseFloat(order?.payment || 0), "currency") }}</strong>
          <span
            v-if="hasPaymentInfo"
            @click="togglePaymentInfo"
            class="icon is-small is-right has-text-info clickable-icon"
          >
            <i class="fas fa-info-circle"></i>
          </span>
        </td>
      </tr>

      <tr>
        <th>{{ t("orders.table.remain") }}</th>
        <td class="has-text-centered">
          <strong>{{ n(remain, "currency") }}</strong>
        </td>
      </tr>

      <tr>
        <th>{{ t("orders.table.status") }}</th>
        <td class="has-text-centered">
          <strong v-if="order">{{ t(`orders.status.${order.status}`) }}</strong>
        </td>
      </tr>
    </tbody>
  </table>
  <div class="has-text-centered mb-5 pb-4">
    <button @click="togglePayment" class="button is-info is-outlined">
      {{ t("orders.pay") }}
    </button>
  </div>
  <OrderDetails v-if="order" :orderId="order.id" :details="order.details" />
  <PaymentModal v-if="showPayment" :orderId="order.id" @close="togglePayment" />
  <CustomerInfoModal
    v-if="showInfo"
    @close="toggleInfo"
    :phone="customer?.phone"
    :address="customer?.address"
  />
  <PaymentInfoModal v-if="showPaymentInfo" @close="togglePaymentInfo" />
</template>

<script>
import { useStore } from "vuex";
import { useRoute } from "vue-router";
import { computed, inject, onBeforeMount, ref, watch } from "vue";

import OrderDetails from "../../components/orderDetails/OrderDetails.vue";
import RequiredInput from "../../components/ui/RequiredInput.vue";
import UnrequiredInput from "../../components/ui/UnrequiredInput.vue";
import PaymentModal from "../../components/orders/PaymentModal.vue";
import CustomerInfoModal from "../../components/orders/CustomerInfoModal.vue";
import PaymentInfoModal from "../../components/orders/PaymentInfoModal.vue";
import { capitalize } from "../../utils";

export default {
  components: {
    OrderDetails,
    RequiredInput,
    UnrequiredInput,
    PaymentModal,
    CustomerInfoModal,
    PaymentInfoModal,
  },
  inject: ["t", "n"],
  setup() {
    const route = useRoute();
    const store = useStore();
    const showPayment = ref(false);
    const showInfo = ref(false);
    const showPaymentInfo = ref(false);
    const websiteTitle = inject("websiteTitle");

    const order = computed(() => {
      return store.getters["orders/order"];
    });

    const customer = computed(() => {
      return store.getters["orders/customer"];
    });

    const subtotal = computed(() => {
      return store.getters["orders/subtotal"];
    });

    const total = computed(() => {
      if (order.value) {
        return parseFloat(order.value.debt) + subtotal.value;
      } else {
        return 0;
      }
    });

    onBeforeMount(() => {
      store.dispatch("orders/fetchOrder", route.params.id);
      store.dispatch("orders/fetchPayments", route.params.id);
    });
    watch(customer, () => {
      const capitalizedName = capitalize(customer.value.name);
      document.title = `${capitalizedName} - ${websiteTitle}`;
    });

    const remain = computed(() => {
      if (order.value) {
        return total.value - parseFloat(order.value.payment);
      }
      return 0;
    });

    const togglePayment = () => {
      showPayment.value = !showPayment.value;
    };

    const toggleInfo = () => {
      showInfo.value = !showInfo.value;
    };

    const togglePaymentInfo = () => {
      showPaymentInfo.value = !showPaymentInfo.value;
    };

    const hasInfo = computed(() => {
      return !!customer.value?.address || !!customer.value?.phone;
    });

    const hasPaymentInfo = computed(() => {
      return store.getters["orders/hasPayment"];
    });

    return {
      order,
      customer,
      subtotal,
      total,
      remain,
      showPayment,
      showInfo,
      showPaymentInfo,
      togglePayment,
      toggleInfo,
      togglePaymentInfo,
      hasInfo,
      hasPaymentInfo,
    };
  },
};
</script>

<style scoped>
table.table th {
  width: 250px;
  padding-left: 25px;
  vertical-align: middle;
  text-align: center;
}

div.button-group {
  margin-top: 0;
  margin-bottom: 2rem;
}
div.button-group button {
  width: 100px;
}
table.table {
  margin-bottom: 1rem;
}
.clickable-icon {
  pointer-events: auto !important;
  cursor: pointer;
}
</style>