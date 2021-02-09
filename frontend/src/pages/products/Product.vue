<template>
  <h3 class="title is-3 has-text-centered">{{ t("products.detailTitle") }}</h3>
  <table class="table is-bordered">
    <tbody>
      <tr>
        <th>{{ t("products.name") }}</th>
        <td class="has-text-centered">
          <RequiredInput
            v-if="isEditing"
            type="text"
            v-model="name"
            :placeholder="t('products.namePlaceholder')"
          />
          <strong v-else :class="deleted">{{ product?.name }}</strong>
        </td>
      </tr>
      <tr>
        <th>{{ t("products.description") }}</th>
        <td>
          <div v-if="isEditing" class="control">
            <textarea
              class="textarea"
              :placeholder="t('products.descriptionPlaceholder')"
              v-model="description"
            ></textarea>
          </div>
          <span v-else :class="deleted">{{ product?.description }}</span>
        </td>
      </tr>
    </tbody>
  </table>
  <div v-if="!product?.active" class="has-text-centered button-group">
    <button @click="activate" class="button is-primary">
      {{ t("recover") }}
    </button>
  </div>
  <div v-else-if="isEditing" class="has-text-centered button-group">
    <button @click="save" class="button is-info mx-5">
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
    <button @click="deactivate" class="button is-danger mx-5">
      {{ t("delete") }}
    </button>
  </div>

  <Units
    v-if="product?.active"
    :productId="product?.id"
    :units="product?.units"
  />
</template>

<script>
import { useStore } from "vuex";
import { useRoute } from "vue-router";
import { computed, onBeforeMount, ref, watch } from "vue";

import Units from "../../components/units/Units.vue";
import RequiredInput from "../../components/ui/RequiredInput.vue";

export default {
  components: { Units, RequiredInput },
  inject: ["t"],
  setup() {
    const route = useRoute();
    const store = useStore();
    const isEditing = ref(false);
    const name = ref("");
    const description = ref("");

    onBeforeMount(() => {
      store.dispatch("products/fetchProduct", route.params.id);
    });

    const product = computed(() => {
      return store.getters["products/product"];
    });

    watch(product, () => {
      name.value = product.value.name;
      description.value = product.value.description;
    });

    const save = async () => {
      if (name.value) {
        await store.dispatch("products/editProduct", {
          name: name.value,
          description: description.value,
        });
        isEditing.value = false;
      }
    };

    const activate = async () => {
      await store.dispatch("products/activateProduct");
    };

    const deactivate = async () => {
      await store.dispatch("products/deactivateProduct");
    };

    const deleted = computed(() => {
      if (product.value?.active) {
        return "";
      } else {
        return "deleted";
      }
    });

    return {
      product,
      isEditing,
      name,
      description,
      save,
      activate,
      deactivate,
      deleted,
    };
  },
};
</script>

<style scoped>
table.table th {
  width: 160px;
  padding-left: 25px;
  vertical-align: middle;
}

div.button-group {
  margin-top: 0;
  margin-bottom: 2rem;
}
div.button-group button {
  width: 100px;
}
</style>