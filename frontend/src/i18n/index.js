import { createI18n } from 'vue-i18n';

import en from './en';
import vi from './vi';

const messages = {
  en,
  vi,
};

const i18n = createI18n({
  locale: 'en', // set locale
  messages, // set locale messages
});

export default i18n;
