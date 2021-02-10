<template>
  <h4 class="title is-4 has-text-centered">{{ t("customers.addTitle") }}</h4>
  <form @submit.prevent="onSubmit">
    <RequiredInput
      :label="t('customers.table.customer')"
      :placeholder="t('customers.namePlaceholder')"
      v-model="name"
      type="text"
    />
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

    <div class="field is-grouped is-grouped-centered">
      <div class="control">
        <button
          type="submit"
          class="button is-primary"
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

export default {
  components: { RequiredInput, UnrequiredInput },
  inject: ["t"],
  setup() {
    const name = ref("");
    const phone = ref("");
    const address = ref("");
    const description = ref("");
    const store = useStore();

    const onSubmit = async () => {
      await store.dispatch("customers/addCustomer", {
        name: name.value,
        phone: phone.value,
        address: address.value,
        description: description.value,
      });
    };

    return { name, phone, address, description, onSubmit };
  },
};
</script>

<style scoped>
form {
  max-width: 500px;
  margin: auto;
}
</style>