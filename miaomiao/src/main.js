import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import vuetify from "./plugins/vuetify";
import "./plugins/element.js";
import api from "./api";
Vue.config.productionTip = false;
Vue.prototype.$api = api;

new Vue({
  router,
  vuetify,
  render: (h) => h(App)
}).$mount("#app");
