<template>
  <tr>
    <td>
      <span :class="{ deleted: !unit.active }">{{ unit.name }}</span>
    </td>
    <td class="has-text-right">
      <span :class="{ deleted: !unit.active }">{{ unit.price }}</span>
    </td>
    <td v-if="unit.active">
      <span class="icon" title="Edit"><i class="fas fa-pen"></i></span>
    </td>
    <td v-else colspan="2" class="has-text-centered">
      <span @click="activate" class="icon" title="Recover"
        ><i class="fas fa-history"></i
      ></span>
    </td>
    <td v-if="unit.active">
      <span @click="deactivate" class="icon" title="Delete"
        ><i class="fas fa-trash-alt"></i
      ></span>
    </td>
  </tr>
</template>

<script>
import { ref } from "vue";
import { useStore } from "vuex";
export default {
  props: ["unit"],
  setup(props) {
    const isEditting = ref(false);
    const name = ref(props.unit.name);
    const price = ref(props.unit.price);
    const store = useStore();

    const deactivate = () => {
      store.dispatch("products/deactivateUnit", props.unit.id);
    };

    const activate = () => {
      store.dispatch("products/activateUnit", props.unit.id);
    };

    return {
      isEditting,
      name,
      price,
      deactivate,
      activate,
    };
  },
};
</script>

<style scoped>
span.icon {
  cursor: pointer;
}
</style>

