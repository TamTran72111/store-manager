<template>
  <h5 class="title is-5 has-text-centered">{{ t("units.title") }}</h5>
  <table class="table is-bordered">
    <thead>
      <tr class="has-text-centered">
        <th>{{ t("units.name") }}</th>
        <th>{{ t("units.price") }}</th>
        <th colspan="2">{{ t("units.action") }}</th>
      </tr>
    </thead>
    <tbody>
      <Unit v-for="unit in units" :key="unit.id" :unit="unit" />
      <tr>
        <td>
          <RequiredInput
            type="text"
            :placeholder="t('units.namePlaceholder')"
            v-model="name"
          />
        </td>
        <td>
          <Currency
            v-model="price"
            :placeholder="t('units.pricePlaceholder')"
          />
          <!-- <RequiredInput
            type="number"
            :placeholder="t('units.pricePlaceholder')"
            v-model="price"
          /> -->
        </td>
        <td colspan="2" class="has-text-centered">
          <button
            :disabled="!name || !price"
            @click="click"
            class="button is-primary"
          >
            {{ t("add") }}
          </button>
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script>
import { ref } from "vue";
import { useStore } from "vuex";

import RequiredInput from "../ui/RequiredInput.vue";
import Currency from "../ui/Currency.vue";
import Unit from "./Unit.vue";

export default {
  components: { RequiredInput, Unit, Currency },
  props: ["productId", "units"],
  inject: ["t"],
  setup(props) {
    const name = ref("");
    const price = ref(0);
    const store = useStore();

    const click = async () => {
      await store.dispatch("products/addUnit", {
        product: props.productId,
        name: name.value,
        price: price.value,
      });
      name.value = "";
      price.value = 0;
    };
    return { name, price, click };
  },
};
</script>

<style scoped>
h5.title {
  margin-top: 1rem;
}

table.table {
  max-width: 500px;
}

table.table th {
  width: calc(50% - 70px);
}
table.table th:last-child {
  width: 140px;
}
</style>