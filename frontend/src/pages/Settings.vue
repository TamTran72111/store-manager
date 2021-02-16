<template>
  <h3 class="title is-3 has-text-centered">{{ t("settings.title") }}</h3>
  <div class="language">
    <p>
      <strong>{{ t("settings.selectLanguage") }}</strong>
    </p>
    <div class="select">
      <select :value="language" @change="change">
        <option value="en">English</option>
        <option value="vi">Tiếng Việt</option>
      </select>
    </div>
  </div>
</template>

<script>
import { computed } from "vue";
import { useStore } from "vuex";
export default {
  inject: ["t"],
  setup() {
    const store = useStore();
    const language = computed(() => {
      return store.getters.language;
    });

    const change = (e) => {
      store.dispatch("changeLanguage", e.target.value);
    };
    return { language, change };
  },
};
</script>

<style scoped>
.language {
  width: 400px;
  margin: 1rem auto;
  border: 1px solid black;
  border-radius: 10px;
  padding: 10px;
}
.language > p {
  margin-bottom: 0.5rem;
}
</style>