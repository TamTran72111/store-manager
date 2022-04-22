<template>
  <p v-if="!!errorMessage" class="notification is-danger has-background-danger">
    {{ errorMessage }}
  </p>
</template>

<script>
export default {
  props: ["errorMessage"],
};
</script>
