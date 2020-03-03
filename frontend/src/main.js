import Vue from "vue";
import App from "./App.vue";

import router from "./router";
import store from "./store/";
import bootstrap from "./core/bootstrap";

import "./utils/action";

import PermissionHelper from "@/utils/permission";
Vue.use(PermissionHelper);

import "./core/";

import "@/assets/css/tailwind.css";

import _ from "lodash";
Object.defineProperty(Vue.prototype, "$_", { value: _ });

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  created: bootstrap,
  render: h => h(App)
}).$mount("#app");
