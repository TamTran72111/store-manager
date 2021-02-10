<template>
  <div class="container">
    <Navbar />
    <router-view></router-view>
  </div>
</template>



<script>
import Navbar from "./components/Navbar.vue";
import { useI18n } from "vue-i18n";

export default {
  components: { Navbar },
  provide() {
    return {
      t: this.t,
    };
  },
  setup() {
    const { t } = useI18n();
    return { t };
  },
};
</script>

<style>
.table-page,
table.table {
  width: 92vw;
  max-width: 800px;
  margin: auto;
}

th {
  position: sticky;
  top: 0;
  background: yellow;
}

.deleted {
  text-decoration: line-through !important;
  color: grey !important;
}
</style>