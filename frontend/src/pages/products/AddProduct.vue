<template>
  <h4 class="title is-4 has-text-centered">{{ t("products.addTitle") }}</h4>
  <form @submit.prevent="onSubmit">
    <RequiredInput
      :label="t('products.name')"
      :placeholder="t('products.namePlaceholder')"
      v-model="name"
      type="text"
      @keydown="errorMessage = ''"
    />
    <ErrorMessage :errorMessage="errorMessage" />
    <div class="field">
      <label class="label">{{ t("products.description") }}</label>
      <div class="control">
        <textarea
          class="textarea"
          :placeholder="t('products.descriptionPlaceholder')"
          v-model="description"
        ></textarea>
      </div>
    </div>

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
          :to="{ name: 'products' }"
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

export default {
  components: { RequiredInput },
  inject: ["t"],
  setup() {
    const name = ref("");
    const description = ref("");
    const store = useStore();
    const errorMessage = ref("");

    const onSubmit = async () => {
      try {
        await store.dispatch("products/addProduct", {
          name: name.value.trim().toLowerCase(),
          description: description.value,
        });
      } catch (e) {
        if (e.response.data.name) {
          errorMessage.value = "Khách Hàng đã tồn tại";
        }
      }
    };

    return { name, description, errorMessage, onSubmit };
  },
};
</script>

<style scoped>
form {
  max-width: 500px;
  margin: auto;
}
</style>