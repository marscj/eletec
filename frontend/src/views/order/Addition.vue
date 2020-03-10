<template>
  <a-spin :spinning="loading">
    <a-card v-for="data in images" :key="data.id">
      <img :src="data.image.medium" alt="image" slot="cover" class="pb-2" />
      <a-card-meta :description="data.tag"> </a-card-meta>
    </a-card>
  </a-spin>
</template>

<script>
import { getImages } from "@/api/image";
export default {
  mounted() {
    this.loading = true;
    getImages({ object_id: this.$route.params.id, content_type: "order" })
      .then(res => {
        this.images = res.result;
      })
      .finally(() => {
        this.loading = false;
      });
  },
  data() {
    return {
      loading: false,
      images: []
    };
  }
};
</script>

<style lang="less" scoped>
.title {
  color: rgba(0, 0, 0, 0.85);
  font-size: 16px;
  font-weight: 500;
  margin-bottom: 16px;
}
</style>
