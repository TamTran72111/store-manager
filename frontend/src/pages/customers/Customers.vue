<template>
  <div class="table-page">
    <div class="has-text-right">
      <router-link
        :to="{ name: 'customer-add' }"
        class="button is-primary is-outlined"
        >{{ t("customers.addButton") }}</router-link
      >
    </div>
    <CustomerSearch />
    <CustomerList />
  </div>
</template>

<script>
import CustomerList from "../../components/customers/CustomerList.vue";
import CustomerSearch from "../../components/customers/CustomerSearch.vue";

export default {
  components: { CustomerList, CustomerSearch },
  inject: ["t"],
};
</script>

