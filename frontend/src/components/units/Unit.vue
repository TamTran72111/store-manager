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
    <td v-if="isEditing" class="v-align has-text-centered">
      <button class="button is-small is-info has-text-weight-medium" @click="save" :title="t('save')"
        >Lưu</button>
    </td>
    <td v-else-if="unit.active" class="has-text-centered">
      <button
        class="button is-small is-info has-text-weight-medium"
        @click="isEditing = true"
        :title="t('edit')"
        >Sửa</button>
    </td>
    <td v-else colspan="2" class="has-text-centered">
      <span
        @click="activate"
        class="button is-small is-primary has-text-black has-text-weight-medium"
        :title="t('recover')"
        >Phục hồi</span>
    </td>
    <td v-if="isEditing" class="v-align">
      <button @click="isEditing = false" class="button is-small is-dark has-text-weight-medium" :title="t('cancel')"
        >Hủy</button>
    </td>
    <td v-else-if="unit.active">
      <button
        @click="deactivate"
        class="button is-small is-danger has-text-weight-medium"
        :title="t('delete')"
        >Xóa</button>
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

