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
          v-if="item.user"
          :author="item.user.name"
          :avatar="item.user.photo ? item.user.photo.image.thumbnail : null"
        >
          <div slot="content">
            <p>{{ item.comment }}</p>
            <a-rate v-model="item.rating" />
          </div>
          <span slot="datetime">{{ item.create_at }}</span>
          <a @click="openModal(item)">Reply to</a>

          <div v-for="(child, index) in item.child" :key="child.id">
            <a-comment
              v-if="child.user"
              :author="child.user.username"
              :avatar="
                child.user.photo ? child.user.photo.image.thumbnail : null
              "
            >
              <div slot="content">
                <img
                  v-if="child.image && child.image.medium"
                  :src="child.image.medium"
                  alt="image"
                />
                <p class="pt-4">{{ child.comment }}</p>
                <a-divider v-if="index < item.child.length - 1"></a-divider>
              </div>
              <span slot="datetime">{{ item.create_at }}</span>
            </a-comment>
          </div>
        </a-comment>
      </a-list-item>
    </a-list>
    <a-modal v-model="modal" title="Reply to" @ok="submit">
      <validation-observer ref="observer">
        <validation-provider name="non_field_errors" v-slot="{ errors }">
          <span class="errorText">{{ errors[0] }}</span>
        </validation-provider>

        <a-form :form="from">
          <a-form-item>
            <validation-provider vid="comment" v-slot="{ errors }">
              <a-input v-model="form.comment"></a-input>
              <span class="errorText">{{ errors[0] }}</span>
            </validation-provider>
          </a-form-item>
        </a-form>
      </validation-observer>
    </a-modal>
  </div>
</template>

<script>
import { getComments, createComment } from "@/api/comment";
export default {
  data() {
    return {
      modal: false,
      form: {},
      loading: false,
      comments: []
    };
  },
  mounted() {
    this.getListData();
  },
  methods: {
    openModal(val) {
      this.form = {
        object_id: val.id
      };
      this.modal = true;
    },
    getListData() {
      getComments({ object_id: this.$route.params.id, content_type: "order" })
        .then(res => {
          this.comments = res.result;
        })
        .finally(() => {
          this.loading = false;
        });
    },
    submit() {
      createComment({
        object_id: this.form.object_id,
        content_type: "comment",
        user_id: this.$store.getters.id,
        comment: this.form.comment,
        rating: null
      })
        .then(res => {
          this.modal = false;
          return this.getListData();
        })
        .catch(error => {
          if (error.response) {
            this.$refs.observer.setErrors(error.response.data.result);
          }
        });
    }
  }
};
</script>
