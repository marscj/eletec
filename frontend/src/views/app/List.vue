<template>
  <page-view class="bg-white">
    <image-list content_type="image" :options="options"> </image-list>
  </page-view>
</template>

<script>
import { PageView } from "@/layouts";
import ImageList from "../common/ImageList";
export default {
  components: {
    PageView,
    ImageList
  },
  data() {
    return {
      options: [
        { value: "Advertising", label: "Advertising" },
        { value: "Banner", label: "Banner" }
      ]
    };
  }
};
</script>
