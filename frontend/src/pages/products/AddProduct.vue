<template>
  <h4 class="title is-4 has-text-centered">Add Product</h4>
  <form @submit.prevent="onSubmit">
    <RequiredInput
      label="Name"
      placeholder="Enter product name"
      v-model="name"
      type="text"
    />
    <div class="field">
      <label class="label">Description</label>
      <div class="control">
        <textarea
          class="textarea"
          placeholder="Enter product description"
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
          Add
        </button>
      </div>
      <div class="control">
        <router-link
          :to="{ name: 'products' }"
          class="button is-link is-light"
          style="width: 100px"
        >
          Cancel
        </router-link>
      </div>
    </div>
  </form>
</template>

<script>
import { ref } from "vue";
import { useStore } from "vuex";
import { useI18n } from "vue-i18n";

import RequiredInput from "../../components/ui/RequiredInput.vue";

export default {
  components: { RequiredInput },
  setup() {
    const name = ref("");
    const description = ref("");
    const store = useStore();
    const { t } = useI18n();

    const onSubmit = async () => {
      await store.dispatch("products/addProduct", {
        name: name.value,
        description: description.value,
      });
    };

    return { name, description, onSubmit, t };
  },
};
</script>

<style scoped>
form {
  max-width: 500px;
  margin: auto;
}
</style>