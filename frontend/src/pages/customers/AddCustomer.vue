<template>
  <h4 class="title is-4 has-text-centered">{{ t("customers.addTitle") }}</h4>
  <form @submit.prevent="onSubmit">
    <RequiredInput
      :label="t('customers.table.customer')"
      :placeholder="t('customers.namePlaceholder')"
      v-model="name"
      isName
      type="text"
      @keydown="errorMessage = ''"
    />
    <ErrorMessage :errorMessage="errorMessage" />
    <UnrequiredInput
      type="text"
      :label="t('customers.table.phone')"
      :placeholder="t('customers.phonePlaceholder')"
      v-model="phone"
    />
    <UnrequiredInput
      type="text"
      :label="t('customers.table.address')"
      :placeholder="t('customers.addressPlaceholder')"
      v-model="address"
    />

    <div class="field">
      <label class="label">{{ t("customers.description") }}</label>
      <div class="control">
        <textarea
          class="textarea"
          :placeholder="t('customers.descriptionPlaceholder')"
          v-model="description"
        ></textarea>
      </div>
    </div>

    <Currency
      v-model="debt"
      :label="t('customers.table.debt')"
      :placeholder="t('customers.table.debt')"
    />

    <div class="field is-grouped is-grouped-centered">
      <div class="control">
        <button
          type="submit"
          class="button is-info"
          style="width: 100px"
          :disabled="!name"
        >
          {{ t("add") }}
        </button>
      </div>
      <div class="control">
        <router-link
          :to="{ name: 'customers' }"
          class="button is-link is-light"
          style="width: 100px"
        >
          {{ t("cancel") }}
        </router-link>
      </div>
    </div>
  </form>
</template>

<script>
import { ref } from "vue";
import { useStore } from "vuex";

import RequiredInput from "../../components/ui/RequiredInput.vue";
import UnrequiredInput from "../../components/ui/UnrequiredInput.vue";
import Currency from "../../components/ui/Currency.vue";
import ErrorMessage from "../../components/ui/ErrorMessage.vue";

export default {
  components: { RequiredInput, UnrequiredInput, Currency, ErrorMessage },
  inject: ["t"],
  setup() {
    const name = ref("");
    const phone = ref("");
    const address = ref("");
    const description = ref("");
    const debt = ref(0);
    const store = useStore();
    const errorMessage = ref("");

    const onSubmit = async () => {
      try {
        await store.dispatch("customers/addCustomer", {
          name: name.value.trim().toLowerCase(),
          phone: phone.value,
          address: address.value,
          description: description.value,
          debt: debt.value,
        });
      } catch (e) {
        if (e.response.data.name) {
          errorMessage.value = "Khách Hàng đã tồn tại";
        }
      }
    };

    return {
      name,
      phone,
      address,
      description,
      debt,
      errorMessage,
      onSubmit,
    };
  },
};
</script>

<style scoped>
form {
  max-width: 500px;
  margin: auto;
}
</style>