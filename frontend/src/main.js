import Vue from "vue";
import App from "./App.vue";

import router from "./router";
import store from "./store/";
import bootstrap from "./core/bootstrap";

import "./core/";

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  created: bootstrap,
  render: h => h(App)
}).$mount("#app");
