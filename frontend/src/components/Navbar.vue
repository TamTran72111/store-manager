<template>
  <nav class="navbar" role="navigation" aria-label="main navigation">
    <div class="navbar-brand">
      <a
        role="button"
        class="navbar-burger"
        aria-label="menu"
        aria-expanded="false"
        data-target="navbarBasicExample"
        @click="toggleShow"
        :class="{ 'is-active': show }"
      >
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
      </a>
    </div>

    <div
      id="navbarBasicExample"
      class="navbar-menu"
      :class="{ 'is-active': show }"
    >
      <div class="navbar-start">
        <router-link to="/" class="navbar-item"> Home </router-link>
      </div>
    </div>
  </nav>
</template>

<script>
import { ref } from "vue";

export default {
  setup() {
    const show = ref(false);
    const toggleShow = () => {
      show.value = !show.value;
    };

    return {
      show,
      toggleShow,
    };
  },
};
</script>