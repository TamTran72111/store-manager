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
          <form @submit.prevent="editProfile">
            <table class="table is-bordered">
              <tbody>
                <tr>
                  <th>{{ t("products.table.product") }}</th>
                  <td style="max-width: 330px">
                    <Suggestion
                      :placeholder="t('products.namePlaceholder')"
                      action="products/fetchProducts"
                      getter="products/products"
                      v-model="product"
                      :initial="product"
                    />
                  </td>
                </tr>
                <tr>
                  <th>{{ t("products.table.unit") }}</th>
                  <td>
                    <div
                      v-if="units.length > 1"
                      class="select is-success"
                      :class="{ 'is-danger': unit === 0 }"
                    >
                      <select v-model="unit">
                        <option :value="0">
                          {{ t("orders.details.select") }}
                        </option>
                        <option
                          v-for="unit_ in units"
                          :key="unit_.id"
                          :value="unit_.id"
                        >
                          {{ unit_.name }}
                        </option>
                      </select>
                    </div>
                    <span v-else-if="units.length > 0">{{
                      units[0].name
                    }}</span>
                  </td>
                </tr>

                <tr>
                  <th>{{ t("products.table.price") }}</th>
                  <td>
                    <UnrequiredInput type="number" v-model="price" readonly />
                  </td>
                </tr>

                <tr>
                  <th>{{ t("orders.details.discount") }}</th>
                  <td>
                    <UnrequiredInput
                      type="number"
                      :placeholder="t('orders.discountPlaceholder')"
                      v-model="discount"
                    />
                  </td>
                </tr>

                <tr>
                  <th>{{ t("orders.details.priceAfterDiscount") }}</th>
                  <td>
                    <UnrequiredInput
                      type="number"
                      v-model="priceAfterDiscount"
                      readonly
                    />
                  </td>
                </tr>

                <tr>
                  <th>{{ t("orders.details.quantity") }}</th>
                  <td>
                    <RequiredInput
                      type="number"
                      :placeholder="t('orders.quantityPlaceholder')"
                      v-model="quantity"
                    />
                  </td>
                </tr>

                <tr>
                  <th>{{ t("orders.details.cost") }}</th>
                  <td>
                    <UnrequiredInput type="number" v-model="cost" readonly />
                  </td>
                </tr>

                <tr>
                  <th>{{ t("orders.details.ready") }}</th>
                  <td class="has-text-centered">
                    <input type="checkbox" v-model="ready" />
                  </td>
                </tr>
              </tbody>
            </table>

            <div class="field is-grouped is-justify-content-center">
              <div class="control">
                <button
                  type="submit"
                  :disabled="isInvalid"
                  class="button is-link"
                  @click="save"
                >
                  {{ t("save") }}
                </button>
              </div>
              <div class="control">
                <button @click.stop="close" class="button is-link is-light">
                  {{ t("cancel") }}
                </button>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  </teleport>
</template>

<script>
import { computed, ref, watch } from "vue";
import RequiredInput from "../ui/RequiredInput.vue";
import UnrequiredInput from "../ui/UnrequiredInput.vue";
import Suggestion from "../ui/Suggestion.vue";
import { useStore } from "vuex";

export default {
  props: ["title", "detail"],
  emits: ["save", "close"],
  components: { RequiredInput, UnrequiredInput, Suggestion },
  inject: ["t"],
  setup(props, context) {
    const store = useStore();
    const product = ref(props.detail?.product_id);
    const unit = ref(props.detail?.unit);
    const quantity = ref(props.detail?.quantity);
    // Tracking discount per unit
    const discount = ref(parseFloat(props.detail?.discount || 0));
    const ready = ref(false);

    const units = computed(() => {
      if (product.value) {
        const targetProduct = store.getters["products/products"].find(
          (prod) => prod.id === product.value
        );
        if (targetProduct) {
          return targetProduct.units;
        }
      }
      return [];
    });

    watch(units, () => {
      if (units.value?.length === 1) {
        unit.value = units.value[0].id;
      } else if (units.value?.length > 1) {
        if (units.value.find((u) => u.id === unit.value) === undefined) {
          unit.value = 0;
        }
      } else {
        unit.value = 0;
      }
    });

    const price = computed(() => {
      return units.value?.find((u) => u.id === unit.value)?.price || 0;
    });

    const priceAfterDiscount = computed(() => {
      // Convert to float to avoid comparing and calculating string values
      const pValue = parseFloat(price.value);
      const dValue = parseFloat(discount.value);

      if (dValue > 0 && pValue > dValue) {
        return pValue - dValue;
      } else {
        return pValue;
      }
    });

    const cost = computed(() => {
      if (price.value && quantity.value > 0 && discount.value >= 0) {
        return (price.value - discount.value) * quantity.value;
      }
      return 0;
    });

    const isInvalid = computed(() => {
      return !(
        unit.value > 0 &&
        quantity.value > 0 &&
        discount.value >= 0 &&
        cost.value >= 0
      );
    });

    const save = () => {
      context.emit("save", {
        unit: unit.value,
        quantity: quantity.value,
        discount: discount.value,
        ready: ready.value,
      });
    };

    const close = () => {
      context.emit("close");
    };

    return {
      product,
      unit,
      price,
      quantity,
      discount,
      priceAfterDiscount,
      cost,
      ready,
      isInvalid,
      units,
      save,
      close,
    };
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

button.button {
  width: 80px;
}
table.table {
  width: auto;
}

.select,
.select > select {
  width: 100%;
}
</style>