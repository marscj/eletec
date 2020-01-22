import Vue from "vue";
import VueStorage from "vue-ls";

import "@/components/global.less";

import Antd from "ant-design-vue";
import "ant-design-vue/dist/antd.css";

import { VueAxios } from "@/utils/request";

import {
  ValidationProvider,
  ValidationObserver
} from "vee-validate/dist/vee-validate.full";

Vue.use(Antd);
Vue.use(VueStorage, {
  namespace: "pro__", // key prefix
  name: "ls", // name variable Vue.[ls] or this.[$ls],
  storage: "local" // storage name session, local, memory
});
Vue.use(VueAxios);
Vue.component("ValidationProvider", ValidationProvider);
Vue.component("ValidationObserver", ValidationObserver);
