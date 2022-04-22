<template>
  <tr>
    <td class="is-capitalized">
      <router-link :to="toLink" :class="{ deleted: !staffDetail.active }">{{
        staffDetail.name
      }}</router-link>
    </td>
    <td class="has-text-centered">
      <span class="has-text-primary icon" v-if="staffDetail.active">
        <i class="fas fa-check"></i>
      </span>
      <span class="has-text-danger icon" v-else>
        <i class="fas fa-xmark"></i>
      </span>
    </td>
  </tr>
</template>

<script>
import { computed } from "vue";
export default {
  props: ["staffDetail"],
  setup(props) {
    const toLink = computed(() => {
      return {
        name: "staff-detail",
        params: { id: props.staffDetail.id },
      };
    });

    return { toLink };
  },
};
</script>
