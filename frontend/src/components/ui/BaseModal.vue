<template>
  <teleport to="body">
    <div class="modal is-active">
      <div class="modal-background" @click="close"></div>
      <div class="modal-content">
        <div class="box">
          <div class="control has-icons-right">
            <h4 class="title is-4 has-text-centered">{{ title }}</h4>
            <span class="icon is-small is-right" @click="close">
              <i class="fas fa-times-circle"></i>
            </span>
          </div>
          <hr class="mb-3" />

          <slot></slot>
        </div>
      </div>
    </div>
  </teleport>
</template>

<script>
export default {
  props: ["title"],
  emits: ["close"],
  setup(_, context) {
    const close = () => {
      context.emit("close");
    };
    return { close };
  },
};
</script>

<style scoped>
i.fa-times-circle {
  pointer-events: auto;
  cursor: pointer;
  transform: translateY(-0.7rem);
  font-size: 2rem;
}
i.fa-times-circle:hover {
  color: #c0c0c0;
}
</style>