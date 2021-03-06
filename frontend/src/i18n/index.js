import { createI18n } from 'vue-i18n';

import en from './en';
import vi from './vi';

const messages = {
  en,
  vi,
};

const numberFormats = {
  en: {
    currency: {
      style: 'currency',
      currency: 'USD',
    },
  },
  vi: {
    currency: {
      style: 'currency',
      currency: 'VND',
    },
  },
};

const i18n = createI18n({
  locale: 'en', // set locale
  messages, // set locale messages
  numberFormats,
});

export default i18n;
