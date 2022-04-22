<template>
  <h4 class="title is-4 has-text-centered">Thêm Nhân Viên</h4>
  <form @submit.prevent="onSubmit">
    <RequiredInput
      label="Tên Nhân Viên"
      placeholder="Tên Nhân Viên"
      v-model="name"
      type="text"
      @keydown="errorMessage = ''"
    />
    <ErrorMessage :errorMessage="errorMessage" />

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
          :to="{ name: 'staff' }"
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
import ErrorMessage from "../../components/ui/ErrorMessage.vue";

export default {
  components: { RequiredInput, ErrorMessage },
  inject: ["t"],
  setup() {
    const name = ref("");
    const store = useStore();
    const errorMessage = ref("");

    const onSubmit = async () => {
      try {
        await store.dispatch("staff/addStaff", {
          name: name.value.trim(),
        });
      } catch (e) {
        console.log(e);
        if (e.response.data.name) {
          errorMessage.value = "Khách Hàng đã tồn tại";
        }
      }
    };

    return { name, errorMessage, onSubmit };
  },
};
</script>

<style scoped>
form {
  max-width: 500px;
  margin: auto;
}
</style>