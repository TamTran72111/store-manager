<template>
  <h4 class="title is-4 has-text-centered">{{ t("orders.addButton") }}</h4>
  <form @submit.prevent="submit">
    <Suggestion
      action="customers/fetchCustomers"
      getter="customers/customers"
      :initial="initial"
      v-model="customer"
      :placeholder="t('customers.namePlaceholder')"
      :label="t('customers.table.customer')"
      paramName="name"
    />
    <div class="has-text-centered mt-5 pt-3">
      <button
        :disabled="!customer"
        type="submit"
        class="button is-primary is-outlined"
      >
        {{ t("orders.addButton") }}
      </button>
    </div>
  </form>
</template>

<script>
import { computed, ref } from "vue";
import { useRoute } from "vue-router";

import Suggestion from "../../components/ui/Suggestion.vue";
import { useStore } from "vuex";

export default {
  components: { Suggestion },
  inject: ["t"],
  setup() {
    const route = useRoute();
    const store = useStore();
    const customer = ref(null);

    // The initial is from query parameter
    const initial = computed(() => {
      const customer = parseInt(route.query.customer);
      if (!isNaN(customer)) {
        return customer;
      } else {
        return null;
      }
    });

    const submit = () => {
      // Double check
      if (customer.value) {
        store.dispatch("orders/addOrder", {
          customer: customer.value,
        });
      }
    };

    return { submit, customer, initial };
  },
};
</script>

<style scoped>
form {
  max-width: 300px;
  margin: auto;
}
</style>