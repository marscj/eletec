<template>
  <div>
    <image-list content_type="order" :object_id="$route.params.id">
    </image-list>
  </div>
</template>

<script>
import ImageList from "../common/ImageList";
export default {
  components: {
    ImageList
  }
};
</script>
