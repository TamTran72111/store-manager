<template>
  <h3 class="title is-3 has-text-centered">Thông Tin Nhân Viên</h3>
  <table class="table is-bordered">
    <tbody>
      <tr>
        <th>Tên Nhân Viên</th>
        <td class="has-text-centered">
          <strong class="is-capitalized">{{ staffDetail?.name }}</strong>
        </td>
      </tr>
      <tr>
        <th>{{ t("customers.table.phone") }}</th>
        <td class="has-text-centered">
          <UnrequiredInput
            v-if="isEditing"
            type="text"
            v-model="phone"
            placeholder="Nhập số điện thoại của nhân viên"
          />
          <strong v-else>{{ staffDetail?.phone }}</strong>
        </td>
      </tr>
      <tr>
        <th>{{ t("customers.table.address") }}</th>
        <td>
          <UnrequiredInput
            v-if="isEditing"
            type="text"
            v-model="address"
            placeholder="Nhập số địa chỉ của nhân viên"
          />
          <span v-else>{{ staffDetail?.address }}</span>
        </td>
      </tr>
      <tr>
        <th>Trạng Thái</th>
        <td v-if="!isEditing" class="has-text-centered">
          <span v-if="staffDetail?.active">Đang Làm</span>
          <span v-else>Đã Nghỉ</span>
        </td>
        <td v-else class="has-text-centered">
          <input type="checkbox" v-model="active" />
        </td>
      </tr>
    </tbody>
  </table>

  <div v-if="isEditing" class="has-text-centered button-group">
    <button @click="save" class="button is-info mx-5">
      {{ t("save") }}
    </button>
    <button @click="isEditing = false" class="button mx-5">
      {{ t("cancel") }}
    </button>
  </div>
  <div v-else class="has-text-centered button-group">
    <button @click="isEditing = true" class="button is-info mx-5">
      {{ t("edit") }}
    </button>
  </div>
</template>

<script>
import { useStore } from "vuex";
import { useRoute } from "vue-router";
import { computed, inject, onBeforeMount, ref, watch } from "vue";

import UnrequiredInput from "../../components/ui/UnrequiredInput.vue";

export default {
  components: { UnrequiredInput },
  inject: ["t", "n"],
  setup() {
    const route = useRoute();
    const store = useStore();
    const isEditing = ref(false);
    const phone = ref("");
    const address = ref("");
    const active = ref(true);
    const websiteTitle = inject("websiteTitle");

    onBeforeMount(async () => {
      await store.dispatch("staff/fetchStaff");
      store.commit("staff/setEditingStaff", parseInt(route.params.id));
      document.title = `Nhân Viên - ${websiteTitle}`;
    });

    const staffDetail = computed(() => {
      return store.getters["staff/editingStaff"];
    });

    watch(staffDetail, () => {
      phone.value = staffDetail.value?.phone;
      address.value = staffDetail.value?.address;
      active.value = staffDetail.value?.active;
    });

    const save = async () => {
      await store.dispatch("staff/editStaff", {
        phone: phone.value,
        address: address.value,
        active: active.value,
      });
      isEditing.value = false;
    };

    return {
      staffDetail,
      isEditing,
      phone,
      address,
      active,
      save,
    };
  },
};
</script>

<style scoped>
table.table th {
  width: 250px;
  padding-left: 25px;
  vertical-align: middle;
  text-align: center;
}

div.button-group {
  margin-top: 0;
  margin-bottom: 2rem;
}
div.button-group button {
  width: 140px;
}
</style>