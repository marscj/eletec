<template>
  <a-locale-provider :locale="locale">
    <div id="app">
      <router-view />
    </div>
  </a-locale-provider>
</template>

<script>
import en_US from "ant-design-vue/lib/locale-provider/en_US";
import { AppDeviceEnquire } from "@/utils/mixin";

export default {
  mixins: [AppDeviceEnquire],
  data() {
    return {
      locale: en_US
    };
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  height: 100%;
}
</style>
