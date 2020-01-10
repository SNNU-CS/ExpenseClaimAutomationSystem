import Vue from "vue";
import Vuetify from "vuetify/lib";
Vue.use(Vuetify);
import zhHans from "vuetify/es5/locale/zh-Hans";
import en from "vuetify/es5/locale/en";

export default new Vuetify({
  icons: {
    iconfont: "mdi"
  },
  lang: {
    locales: { zhHans, en },
    current: "zhHans"
  }
});
