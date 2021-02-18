<template>
  <div class="field">
    <div class="control">
      <input
        class="input has-text-right"
        type="text"
        :placeholder="placeholder"
        :value="value"
        @blur="validateInput"
        @focus="focus"
        required
      />
    </div>
  </div>
</template>

<script>
import { computed, ref } from "vue";
import { useI18n } from "vue-i18n";

export default {
  props: ["placeholder", "modelValue"],
  emits: ["update:modelValue"],
  setup(props, context) {
    const { n } = useI18n();
    const isEditing = ref(false);

    const validateInput = (e) => {
      isEditing.value = false;
      const value = parseFloat(e.target.value);
      if (isNaN(value)) {
        context.emit("update:modelValue", 0);
      } else {
        context.emit("update:modelValue", value);
      }
    };

    const value = computed(() => {
      if (isEditing.value) {
        return parseFloat(props.modelValue);
      }
      return n(parseFloat(props.modelValue), "currency");
    });

    const focus = () => {
      isEditing.value = true;
    };

    return {
      validateInput,
      value,
      focus,
    };
  },
};
</script>