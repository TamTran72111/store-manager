import { createStore } from 'vuex';

import products from './products';
import customers from './customers';
import orders from './orders';
import i18n from '../i18n';

export default createStore({
  modules: {
    products,
    customers,
    orders,
  },
  state: {
    language: localStorage.getItem('language') || 'en',
  },
  getters: {
    language(state) {
      return state.language;
    },
  },
  mutations: {
    changeLanguage(state, language) {
      localStorage.setItem('language', language);
      state.language = language;
      i18n.global.locale = language;
    },
  },
  actions: {
    changeLanguage({ commit }, language) {
      commit('changeLanguage', language);
    },
    setLanguage({ getters }) {
      i18n.global.locale = getters.language;
    },
  },
});
