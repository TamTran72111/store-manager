<template>
  <div class="container">
    <Navbar />
    <router-view></router-view>
  </div>
</template>



<script>
import Navbar from "./components/Navbar.vue";

export default {
  components: { Navbar },
};
</script>

<style>
table.table {
  width: 80vw;
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