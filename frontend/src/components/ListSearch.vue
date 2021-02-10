<template>
  <div class="list-search">
    <DebounceInput
      type="text"
      v-model="searchName"
      :label="label"
      :placeholder="placeholder"
    />
  </div>
</template>

<script>
import { computed, inject, ref, watch } from "vue";
import { useStore } from "vuex";

import DebounceInput from "./ui/DebounceInput.vue";

export default {
  components: { DebounceInput },
  props: {
    label: {
      type: String,
      default: "search",
    },
    placeholder: {
      type: String,
      default: "",
    },
    actionName: {
      type: String,
      default: "",
    },
  },
  setup(props) {
    const searchName = ref("");
    const store = useStore();
    const t = inject("t"); // Translator

    watch(searchName, () => {
      if (props.actionName !== "") {
        store.dispatch(props.actionName, searchName.value);
      }
    });

    const label = computed(() => {
      if (props.label !== "") {
        return t(props.label);
      } else {
        return "";
      }
    });

    const placeholder = computed(() => {
      if (props.placeholder !== "") {
        return t(props.placeholder);
      } else {
        return "";
      }
    });
    return { searchName, label, placeholder };
  },
};
</script>

<style scoped>
.list-search {
  margin-top: 1rem;
  margin-bottom: 1rem;
}
</style>