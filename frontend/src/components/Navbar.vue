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
        <router-link :to="{ name: 'products' }" class="navbar-item">{{
          t("navbar.products")
        }}</router-link>
        <router-link :to="{ name: 'customers' }" class="navbar-item">{{
          t("navbar.customers")
        }}</router-link>
        <router-link :to="{ name: 'orders' }" class="navbar-item">{{
          t("navbar.orders")
        }}</router-link>
      </div>
    </div>
  </nav>
</template>

<script>
import { ref } from "vue";

export default {
  inject: ["t"],
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