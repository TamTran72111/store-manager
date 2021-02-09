<template>
  <h5 class="title is-5 has-text-centered">Units</h5>
  <table class="table is-bordered">
    <thead>
      <tr class="has-text-centered">
        <th>Name</th>
        <th>Price</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="unit in units" :key="unit.id">
        <td>{{ unit.name }}</td>
        <td class="has-text-right">{{ unit.price }}</td>
      </tr>
      <tr>
        <td>
          <RequiredInput
            type="text"
            placeholder="Enter unit name"
            v-model="name"
          />
        </td>
        <td>
          <RequiredInput
            type="number"
            placeholder="Enter unit price"
            v-model="price"
          />
        </td>
      </tr>
    </tbody>
  </table>
  <div class="has-text-centered">
    <button
      :disabled="!name || !price"
      @click="click"
      class="button is-primary"
    >
      Thêm đơn vị đo
    </button>
  </div>
</template>

<script>
import { ref } from "vue";
import { useStore } from "vuex";

import RequiredInput from "../ui/RequiredInput.vue";

export default {
  components: { RequiredInput },
  props: ["productId", "units"],
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
  width: 50%;
}
</style>