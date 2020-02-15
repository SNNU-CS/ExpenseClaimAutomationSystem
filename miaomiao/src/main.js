import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import vuetify from "./plugins/vuetify";
import "./plugins/element.js";
import api from "./api";
import ECharts from "vue-echarts";
Vue.component("v-chart", ECharts);
import "echarts/lib/chart/line";
import "echarts/lib/chart/pie";
import "echarts/lib/chart/bar";
import "echarts/lib/chart/graph";
// component examples:
import "echarts/lib/component/tooltip";
import "echarts/lib/component/title";
import "echarts/lib/component/toolbox";
import "echarts/lib/component/axis";
import "echarts/lib/component/legend";
Vue.config.productionTip = false;
Vue.prototype.$api = api;

new Vue({
  router,
  vuetify,
  render: (h) => h(App)
}).$mount("#app");
