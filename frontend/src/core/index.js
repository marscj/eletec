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

import moment from "moment";

import * as VueGoogleMaps from "vue2-google-maps";

Vue.filter("moment", function(dataStr, pattern = "YYYY-MM-DD HH:mm:ss") {
  return moment(dataStr).format(pattern);
});

Vue.use(Antd);
Vue.use(VueStorage, {
  namespace: "pro__", // key prefix
  name: "ls", // name variable Vue.[ls] or this.[$ls],
  storage: "local" // storage name session, local, memory
});
Vue.use(VueAxios);
Vue.component("ValidationProvider", ValidationProvider);
Vue.component("ValidationObserver", ValidationObserver);

Vue.use(VueGoogleMaps, {
  load: {
    key: "AIzaSyDzghr7PgoT1k_M9JR8UCC0OLmNyv884io",
    libraries: "places" // This is required if you use the Autocomplete plugin
    // OR: libraries: 'places,drawing'
    // OR: libraries: 'places,drawing,visualization'
    // (as you require)

    //// If you want to set the version, you can do so:
    // v: '3.26',
  },

  //// If you intend to programmatically custom event listener code
  //// (e.g. `this.$refs.gmap.$on('zoom_changed', someFunc)`)
  //// instead of going through Vue templates (e.g. `<GmapMap @zoom_changed="someFunc">`)
  //// you might need to turn this on.
  // autobindAllEvents: false,

  //// If you want to manually install components, e.g.
  //// import {GmapMarker} from 'vue2-google-maps/src/components/marker'
  //// Vue.component('GmapMarker', GmapMarker)
  //// then set installComponents to 'false'.
  //// If you want to automatically install all the components this property must be set to 'true':
  installComponents: true
});
