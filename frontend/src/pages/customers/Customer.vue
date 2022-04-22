<template>
  <h3 class="title is-3 has-text-centered">{{ t("customers.detailTitle") }}</h3>
  <table class="table is-bordered">
    <tbody>
      <tr>
        <th>{{ t("customers.table.customer") }}</th>
        <td class="has-text-centered">
          <RequiredInput
            v-if="isEditing"
            type="text"
            v-model="name"
            :placeholder="t('customers.namePlaceholder')"
          />
          <strong class="is-capitalized" v-else>{{ customer?.name }}</strong>
        </td>
      </tr>
      <tr>
        <th>{{ t("customers.table.phone") }}</th>
        <td class="has-text-centered">
          <UnrequiredInput
            v-if="isEditing"
            type="text"
            v-model="phone"
            :placeholder="t('customers.phonePlaceholder')"
          />
          <strong v-else>{{ customer?.phone }}</strong>
        </td>
      </tr>
      <tr>
        <th>{{ t("customers.table.address") }}</th>
        <td>
          <UnrequiredInput
            v-if="isEditing"
            type="text"
            v-model="address"
            :placeholder="t('customers.addressPlaceholder')"
          />
          <span v-else>{{ customer?.address }}</span>
        </td>
      </tr>
      <tr>
        <th>{{ t("customers.description") }}</th>
        <td>
          <div v-if="isEditing" class="control">
            <textarea
              class="textarea"
              :placeholder="t('customers.descriptionPlaceholder')"
              v-model="description"
            ></textarea>
          </div>
          <span v-else>{{ customer?.description }}</span>
        </td>
      </tr>
      <tr v-if="!isEditing">
        <th>{{ t("customers.table.debt") }}</th>
        <td class="has-text-centered">
          <strong>{{ n(parseFloat(customer?.debt || 0), "currency") }}</strong>
        </td>
      </tr>
    </tbody>
  </table>

  <div v-if="isEditing" class="has-text-centered button-group">
    <button @click="save" :disabled="!name" class="button is-info mx-5">
      {{ t("save") }}
    </button>
    <button @click="isEditing = false" class="button mx-5">
      {{ t("cancel") }}
    </button>
  </div>
  <div v-else class="has-text-centered button-group">
    <button @click="isEditing = true" class="button is-info mx-5">
      {{ t("edit") }}
    </button>
    <button @click="addOrder" class="button is-info mx-5">
      {{ t("orders.addButton") }}
    </button>
  </div>

  <OrderList />
</template>

<script>
import { useStore } from "vuex";
import { useRoute } from "vue-router";
import { computed, inject, onBeforeMount, ref, watch } from "vue";

import Units from "../../components/units/Units.vue";
import RequiredInput from "../../components/ui/RequiredInput.vue";
import UnrequiredInput from "../../components/ui/UnrequiredInput.vue";
import OrderList from "../../components/orders/OrderList.vue";
import { capitalize } from "../../utils";

export default {
  components: { Units, RequiredInput, UnrequiredInput, OrderList },
  inject: ["t", "n"],
  setup() {
    const route = useRoute();
    const store = useStore();
    const isEditing = ref(false);
    const name = ref("");
    const phone = ref("");
    const address = ref("");
    const description = ref("");
    const websiteTitle = inject("websiteTitle");

    onBeforeMount(async () => {
      await store.dispatch("customers/fetchCustomer", route.params.id);
      await store.dispatch("orders/fetchOrders", {
        customer: store.getters["customers/customerName"],
      });
      const capitalizedName = capitalize(name.value);
      document.title = `${capitalizedName} - ${websiteTitle}`;
    });

    const customer = computed(() => {
      return store.getters["customers/customer"];
    });

    watch(customer, () => {
      name.value = customer.value.name;
      phone.value = customer.value.phone;
      address.value = customer.value.address;
      description.value = customer.value.description;
    });

    const save = async () => {
      await store.dispatch("customers/editCustomer", {
        name: name.value.trim().toLowerCase(),
        phone: phone.value,
        address: address.value,
        description: description.value,
      });
      isEditing.value = false;
    };

    const addOrder = () => {
      store.dispatch("orders/addOrder", {
        customer: store.getters["customers/customerId"],
      });
    };

    return {
      customer,
      isEditing,
      name,
      phone,
      address,
      description,
      save,
      addOrder,
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
  width: 140px;
}
</style>