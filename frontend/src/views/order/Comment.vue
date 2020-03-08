<template>
  <div>
    <div>
      <a-list
        class="comment-list"
        itemLayout="horizontal"
        :dataSource="form.comments"
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
  </div>
</template>

<script>
export default {};
</script>
