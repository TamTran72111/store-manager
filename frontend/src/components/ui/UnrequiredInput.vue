<template>
  <div class="field">
    <label v-if="label" class="label">{{ label }}</label>
    <div class="control" :class="{ 'has-icons-left': !!icon }">
      <input
        ref="inputRef"
        class="input"
        :class="{ 'has-text-right': type === 'number' }"
        :type="type"
        :placeholder="placeholder"
        :value="modelValue"
        @input="handleInput"
        @blur="blur_"
        @focus="focus"
        @keypress.enter="enter"
        :readonly="readonly"
      />
      <span v-if="!!icon" class="icon is-small is-left">
        <i :class="`fas ${icon}`"></i>
      </span>
    </div>
  </div>
</template>

<script>
import { ref } from "vue";
export default {
  props: {
    type: {
      type: String,
      default: "text",
    },
    icon: {
      type: String,
      default: "",
    },
    placeholder: {
      type: String,
      default: "",
    },
    modelValue: {
      required: true,
    },
    label: { type: String, default: "" },
    blur: { type: Function, default: () => {} },
    focus: { type: Function, default: () => {} },
    readonly: {
      type: Boolean,
      default: false,
    },
  },
  emits: ["update:modelValue"],
  setup(props, context) {
    const inputRef = ref(null);
    const handleInput = (e) => {
      context.emit("update:modelValue", e.target.value);
    };

    const blur_ = () => {
      // Delay to allow other event happen
      setTimeout(props.blur, 200);
    };

    const enter = () => {
      inputRef.value.blur();
    };

    return {
      handleInput,
      blur_,
      enter,
      inputRef,
    };
  },
};
</script>