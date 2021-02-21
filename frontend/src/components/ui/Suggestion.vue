<template>
  <div class="suggestion-wrapper">
    <debounce-input
      :label="label"
      :placeholder="placeholder"
      type="text"
      v-model="value"
      :focus="focus"
      :blur="blur"
    />
    <div v-if="isFocusing" class="suggestions">
      <div>
        <strong
          class="suggestion"
          v-for="suggestion in suggestions"
          :key="suggestion.id"
          @click.stop="click(suggestion.id, suggestion.name)"
        >
          {{ suggestion.name }}
        </strong>
      </div>
    </div>
  </div>
</template>

<script>
import { computed, onBeforeMount, ref, watch } from "vue";
import DebounceInput from "./DebounceInput.vue";
import { useStore } from "vuex";

export default {
  components: { DebounceInput },
  props: [
    "label",
    "placeholder",
    "modelValue",
    "getter",
    "action",
    "initial",
    "paramName",
  ],
  emits: ["update:modelValue"],
  setup(props, context) {
    const invalid = ref(false);
    const isFocusing = ref(false);
    const store = useStore();
    const value = ref("");

    watch(value, () => {
      store.dispatch(props.action, { [props.paramName]: value.value });
    });

    onBeforeMount(() => {
      store.dispatch(props.action);

      setTimeout(() => {
        if (props.initial) {
          validate(props.initial);
        }
      }, 300);
    });

    const suggestions = computed(() => {
      return store.getters[props.getter];
    });

    const validate = (id) => {
      const suggestion = suggestions.value.find(
        (suggestion) =>
          id === suggestion.id ||
          suggestion.name.toLowerCase() === value.value.toLowerCase()
      );
      if (suggestion) {
        value.value = suggestion.name;
        invalid.value = false;
        context.emit("update:modelValue", suggestion.id);
      } else {
        invalid.value = true;
        context.emit("update:modelValue", null);
      }
    };

    const blur = () => {
      if (value.value === "") {
        invalid.value = true;
      }
      if (isFocusing.value) {
        validate(null);
        isFocusing.value = false;
      }
    };

    const focus = () => {
      invalid.value = false;
      isFocusing.value = true;
    };

    const click = (id) => {
      validate(id);
      isFocusing.value = false;
    };

    return {
      invalid,
      suggestions,
      isFocusing,
      focus,
      blur,
      value,
      click,
    };
  },
};
</script>

<style scoped>
.suggestion-wrapper {
  width: 300px;
}
.suggestions {
  position: relative;
  width: 300px;
}

.suggestions div {
  position: absolute;
  z-index: 10;
  display: flex;
  flex-direction: column;
  width: 300px;
  transform: translateY(-10px);
  background: white;
}

.suggestion {
  width: 100%;
  padding: 5px 0 5px 10px;
  border: 1px solid grey;
  border-bottom: none;
  position: relative;
  cursor: pointer;
}
.suggestion:last-child {
  border-bottom: 1px solid grey;
  border-bottom-left-radius: 7px;
  border-bottom-right-radius: 7px;
}
.suggestion:before {
  content: "";
  display: block;
  position: absolute;
  height: 100%;
  border-left: 6px solid blue;
  top: 0px;
  left: 0px;
}

.suggestion:last-child:before {
  border-bottom-left-radius: 7px;
}
</style>