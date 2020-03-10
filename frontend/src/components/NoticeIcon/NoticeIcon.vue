<template>
  <a-popover
    v-model="visible"
    trigger="click"
    :getPopupContainer="() => $refs.noticeRef.parentElement"
    :autoAdjustOverflow="true"
    :arrowPointAtCenter="true"
    :overlayStyle="{ width: '400px', top: '50px' }"
  >
    <template slot="content">
      <a-tabs>
        <a-tab-pane key="1">
          <template slot="tab">
            <a-badge :count="order_count" :offset="[12]">
              Order
            </a-badge>
          </template>
          <a-list :dataSource="orderData" itemLayout="vertical">
            <a-list-item slot="renderItem" slot-scope="item">
              <a-list-item-meta
                :description="item.date | moment('YYYY-MM-DD HH:mm')"
              >
                <template slot="title">
                  <router-link :to="{ name: 'Order', params: { id: item.pk } }">
                    {{ item.message }} {{ item.objectID }}
                  </router-link>
                </template>
              </a-list-item-meta>
              <template slot="extra">
                <a-icon type="delete" @click="removeMessage(item)" />
              </template>
            </a-list-item>
          </a-list>
        </a-tab-pane>
        <a-tab-pane key="2">
          <template slot="tab">
            <a-badge :count="job_count" :offset="[12]">
              Job
            </a-badge>
          </template>
          <a-list :dataSource="jobData" itemLayout="vertical">
            <a-list-item slot="renderItem" slot-scope="item">
              <a-list-item-meta
                :description="item.date | moment('YYYY-MM-DD HH:mm')"
              >
                <template slot="title">
                  <router-link :to="{ name: 'Order', params: { id: item.pk } }">
                    {{ item.message }} {{ item.objectID }}
                  </router-link>
                </template>
              </a-list-item-meta>
              <template slot="extra">
                <a-icon type="delete" @click="removeMessage(item)" />
              </template>
            </a-list-item>
          </a-list>
        </a-tab-pane>
        <a-tab-pane key="3">
          <template slot="tab">
            <a-badge :count="comment_count" :offset="[12]">
              Comment
            </a-badge>
          </template>
          <a-list :dataSource="commentData" itemLayout="vertical">
            <a-list-item slot="renderItem" slot-scope="item">
              <a-list-item-meta
                :description="item.date | moment('YYYY-MM-DD HH:mm')"
              >
                <template slot="title">
                  <router-link :to="{ name: 'Order', params: { id: item.pk } }">
                    {{ item.message }} {{ item.objectID }}
                  </router-link>
                </template>
              </a-list-item-meta>
              <template slot="extra">
                <a-icon type="delete" @click="removeMessage(item)" />
              </template>
            </a-list-item>
          </a-list>
        </a-tab-pane>
      </a-tabs>
    </template>
    <span
      @click="fetchNotice"
      class="header-notice"
      ref="noticeRef"
      style="padding: 0 18px"
    >
      <a-badge :count="count">
        <a-icon style="font-size: 16px; padding: 4px" type="bell" />
      </a-badge>
    </span>
  </a-popover>
</template>

<script>
export default {
  name: "HeaderNotice",
  data() {
    return {
      visible: false
    };
  },
  computed: {
    count() {
      return this.$store.getters.message.length;
    },
    order_count() {
      return this.$store.getters.message.filter(f => f.msg_type == 0).length;
    },
    job_count() {
      return this.$store.getters.message.filter(f => f.msg_type == 1).length;
    },
    comment_count() {
      return this.$store.getters.message.filter(f => f.msg_type == 2).length;
    },
    orderData() {
      return this.$store.getters.message.filter(f => f.msg_type == 0);
    },
    jobData() {
      return this.$store.getters.message.filter(f => f.msg_type == 1);
    },
    commentData() {
      return this.$store.getters.message.filter(f => f.msg_type == 2);
    }
  },
  methods: {
    fetchNotice() {
      this.visible = !this.visible;
    },
    removeMessage(item) {
      this.$store.dispatch("removeMessage", item);
    }
  }
};
</script>

<style lang="css">
.header-notice-wrapper {
  top: 50px !important;
}
</style>
<style lang="less" scoped>
.header-notice {
  display: inline-block;
  transition: all 0.3s;

  span {
    vertical-align: initial;
  }
}
</style>
