<template>
  <div>
    <a-list
      class="comment-list"
      itemLayout="horizontal"
      :dataSource="comments"
      :loading="loading"
    >
      <a-list-item slot="renderItem" slot-scope="item">
        <a-comment
          :author="item.user.name ? item.user.name : item.user.username"
          :avatar="item.user.photo ? item.user.photo.image.thumbnail : null"
        >
          <div slot="content">
            <p>{{ item.comment }}</p>
            <a-rate v-model="item.rating" />
          </div>
          <span slot="datetime">{{ item.create_at }}</span>
        </a-comment>
      </a-list-item>
    </a-list>
  </div>
</template>

<script>
import { getComments } from "@/api/comment";
export default {
  data() {
    return {
      loading: false,
      comments: []
    };
  },
  mounted() {
    getComments({ object_id: this.$route.params.id, content_type: "order" })
      .then(res => {
        this.comments = res.result;
      })
      .finally(() => {
        this.loading = false;
      });
  }
};
</script>
