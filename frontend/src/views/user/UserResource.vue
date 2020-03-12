<template>
  <div>
    <image-list
      content_type="user"
      :options="options"
      :object_id="$route.params.id"
    >
    </image-list>
  </div>
</template>

<script>
import ImageList from "../common/ImageList";
export default {
  components: {
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
