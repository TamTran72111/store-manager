<template>
  <div class="field">
    <div class="control">
      <input
        ref="inputRef"
        class="input has-text-right"
        type="text"
        :placeholder="placeholder"
        @input="handleInput"
        required
      />
    </div>
  </div>
</template>

<script>
import { onMounted, ref, watch } from "vue";
import { useI18n } from "vue-i18n";

export default {
  props: ["placeholder", "modelValue"],
  emits: ["update:modelValue"],
  setup(props, context) {
    const { n, locale } = useI18n();
    const inputRef = ref(null);

    onMounted(() => {
      inputRef.value.value = n(parseFloat(props.modelValue || 0), "currency");
    });

    watch(props, () => {
      const oldLength = inputRef.value.value.length;
      const oldPosition = inputRef.value.selectionStart;
      const newValue = n(parseFloat(props.modelValue), "currency");
      const newPosition = oldPosition + newValue.length - oldLength;
      inputRef.value.value = newValue;
      inputRef.value.setSelectionRange(newPosition, newPosition);
    });

    const handleInput = (e) => {
      let value = e.target.value;

      if (locale.value === "vi") {
        // Convert the vietnamese format to english format
        value = value.replace(/\./g, "");
        value = value.replace(/,/g, ".");
      }
      // Clean up
      value = value.replace(/,/g, "");
      value = value.replace(/[^\d.]/g, "");

      context.emit("update:modelValue", value);
    };

    return {
      handleInput,
      inputRef,
    };
  },
};
</script>