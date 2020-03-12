<template>
  <page-view>
    <image-list
      content_type="user"
      :options="options"
      :object_id="$route.params.id"
    >
    </image-list>
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
        { value: "EmiratesID", label: "EmiratesID" },
        { value: "Driver License", label: "Driver License" }
      ]
    };
  }
};
</script>
