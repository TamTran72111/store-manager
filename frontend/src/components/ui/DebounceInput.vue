<template>
  <UnrequiredInput
    :type="type"
    :icon="icon"
    :placeholder="placeholder"
    :label="label"
    v-model="value"
    :blur="blur"
    :focus="focus"
  />
</template>

<script>
import { ref, watch } from "vue";
import UnrequiredInput from "./UnrequiredInput.vue";

export default {
  components: { UnrequiredInput },
  props: [
    "type",
    "icon",
    "placeholder",
    "modelValue",
    "label",
    "time",
    "blur",
    "focus",
  ],
  emits: ["update:modelValue"],
  setup(props, context) {
    let timer = null;
    const value = ref(props.modelValue);

    watch(props, () => {
      if (props.modelValue !== value.value) {
        value.value = props.modelValue;
      }
    });

    watch(value, () => {
      if (timer) {
        clearTimeout(timer);
      }
      timer = setTimeout(() => {
        context.emit("update:modelValue", value.value);
      }, props.time || 400);
    });

    return {
      value,
    };
  },
};
</script>