<template>
  <div class="layout--full-page h-screen flex flex-col">
    <route-view class="h-full"></route-view>

    <div class="text-center">
      <div class="m-10">
        Copyright &copy; 2020 Eletec
      </div>
    </div>
  </div>
</template>

<script>
import RouteView from "./RouteView";
import { mixinDevice } from "@/utils/mixin";

export default {
  name: "UserLayout",
  components: { RouteView },
  mixins: [mixinDevice],
  data() {
    return {};
  },
  mounted() {
    document.body.classList.add("userLayout");
  },
  beforeDestroy() {
    document.body.classList.remove("userLayout");
  }
};
</script>

<style lang="less" scoped>
.layout--full-page {
  background: #e3e5e9 url(~@/assets/background.svg) no-repeat 50%;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
}
</style>
