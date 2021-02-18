<template>
  <tr>
    <td>
      <RequiredInput
        v-if="isEditing"
        type="text"
        v-model="name"
        :placeholder="t('units.namePlaceholder')"
      />
      <span v-else :class="{ deleted: !unit.active }">{{ unit.name }}</span>
    </td>
    <td class="has-text-right">
      <Currency
        v-if="isEditing"
        v-model="price"
        :placeholder="t('units.pricePlaceholder')"
      />
      <span v-else :class="{ deleted: !unit.active }">{{
        n(parseFloat(unit.price), "currency")
      }}</span>
    </td>
    <td v-if="isEditing" class="v-align">
      <span class="icon has-text-info" @click="save" :title="t('save')"
        ><i class="fas fa-save"></i
      ></span>
    </td>
    <td v-else-if="unit.active">
      <span
        class="icon has-text-info"
        @click="isEditing = true"
        :title="t('edit')"
        ><i class="fas fa-pen"></i
      ></span>
    </td>
    <td v-else colspan="2" class="has-text-centered">
      <span
        @click="activate"
        class="icon has-text-primary"
        :title="t('recover')"
        ><i class="fas fa-history"></i
      ></span>
    </td>
    <td v-if="isEditing" class="v-align">
      <span @click="isEditing = false" class="icon" :title="t('cancel')"
        ><i class="fas fa-history"></i
      ></span>
    </td>
    <td v-else-if="unit.active">
      <span
        @click="deactivate"
        class="icon has-text-danger"
        :title="t('delete')"
        ><i class="fas fa-trash-alt"></i
      ></span>
    </td>
  </tr>
</template>

<script>
import { ref } from "vue";
import { useStore } from "vuex";

import RequiredInput from "../ui/RequiredInput.vue";
import Currency from "../ui/Currency.vue";

export default {
  components: { RequiredInput, Currency },
  props: ["unit"],
  inject: ["t", "n"],
  setup(props) {
    const isEditing = ref(false);
    const name = ref(props.unit.name);
    const price = ref(props.unit.price);
    const store = useStore();

    const deactivate = () => {
      store.dispatch("products/deactivateUnit", props.unit.id);
    };

    const activate = () => {
      store.dispatch("products/activateUnit", props.unit.id);
    };

    const save = async () => {
      if (name.value && price.value) {
        await store.dispatch("products/editUnit", {
          unitId: props.unit.id,
          payload: {
            name: name.value,
            price: price.value,
          },
        });
        isEditing.value = false;
      }
    };
    return {
      isEditing,
      name,
      price,
      deactivate,
      activate,
      save,
    };
  },
};
</script>

<style scoped>
span.icon {
  cursor: pointer;
}

.v-align {
  vertical-align: middle;
}
</style>

