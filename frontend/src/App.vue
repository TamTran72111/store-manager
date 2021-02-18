<template>
  <div class="container">
    <Navbar />
    <router-view></router-view>
  </div>
</template>



<script>
import Navbar from "./components/Navbar.vue";
import { useI18n } from "vue-i18n";
import { onBeforeMount } from "vue";
import { useStore } from "vuex";

export default {
  components: { Navbar },
  provide() {
    return {
      t: this.t,
      n: this.n,
    };
  },
  setup() {
    const { t, n } = useI18n();
    const store = useStore();
    onBeforeMount(() => {
      store.dispatch("setLanguage");
    });
    return { t, n };
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

th.hide-on-small,
td.hide-on-small {
  display: none;
}

@media (min-width: 700px) {
  th.hide-on-small,
  td.hide-on-small {
    display: table-cell;
  }
}
</style>