<template>
  <h5 class="title is-5 has-text-centered">Units</h5>
  <table class="table is-bordered">
    <thead>
      <tr class="has-text-centered">
        <th>Name</th>
        <th>Price</th>
        <th colspan="2">Action</th>
      </tr>
    </thead>
    <tbody>
      <Unit v-for="unit in units" :key="unit.id" :unit="unit" />
      <tr>
        <td>
          <RequiredInput type="text" placeholder="Enter name" v-model="name" />
        </td>
        <td>
          <RequiredInput
            type="number"
            placeholder="Enter price"
            v-model="price"
          />
        </td>
        <td colspan="2" class="has-text-centered">
          <button
            :disabled="!name || !price"
            @click="click"
            class="button is-primary"
          >
            Add
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
import Unit from "./Unit.vue";

export default {
  components: { RequiredInput, Unit },
  props: ["productId", "units"],
  setup(props) {
    const name = ref("");
    const price = ref(0);
    const store = useStore();
    const t = useI18n();

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
  width: calc(50% - 50px);
}
table.table th:last-child {
  width: 100px;
}
</style>