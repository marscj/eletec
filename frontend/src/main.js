import Vue from "vue";
import App from "./App.vue";

import router from "./router";
import store from "./store/";
import bootstrap from "./core/bootstrap";

import "./utils/action";

import PermissionHelper from "@/utils/permission";

import "./core/";

import "@/assets/css/tailwind.css";

import _ from "lodash";

import VueNativeSock from "vue-native-websocket";

Vue.use(PermissionHelper);

Object.defineProperty(Vue.prototype, "$_", { value: _ });

Vue.use(VueNativeSock, "ws://localhost:8002/notify/", {
  connectManually: true,
  store: store,
  format: "json"
});

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  created: bootstrap,
  render: h => h(App)
}).$mount("#app");
