<template>
  <a-popover
    v-model="visible"
    trigger="click"
    placement="bottomRight"
    overlayClassName="header-notice-wrapper"
    :getPopupContainer="() => $refs.noticeRef.parentElement"
    :autoAdjustOverflow="true"
    :arrowPointAtCenter="true"
    :overlayStyle="{ width: '300px', top: '50px' }"
  >
    <template slot="content">
      <a-spin :spinning="loading">
        <a-tabs>
          <a-tab-pane tab="order" key="1">
            <a-list :dataSource="unreadData">
              <a-list-item slot="renderItem" slot-scope="item">
                <a-list-item-meta
                  :title="item.message"
                  :description="item.date | moment('YYYY-MM-DD HH:mm')"
                >
                </a-list-item-meta>
                <a-icon type="message" @click="readMessage(item)"></a-icon>
              </a-list-item>
            </a-list>
          </a-tab-pane>
          <a-tab-pane tab="job" key="2">
            <a-list :dataSource="readData">
              <a-list-item slot="renderItem" slot-scope="item">
                <a-icon type="delete" @click="removeMessage(item)"></a-icon>
                <a-list-item-meta
                  :title="item.message"
                  :description="item.date | moment('YYYY-MM-DD HH:mm')"
                >
                </a-list-item-meta>
              </a-list-item>
            </a-list>
          </a-tab-pane>
          <a-tab-pane tab="comment" key="2">
            <a-list :dataSource="readData">
              <a-list-item slot="renderItem" slot-scope="item">
                <a-icon type="delete" @click="removeMessage(item)"></a-icon>
                <a-list-item-meta
                  :title="item.message"
                  :description="item.date | moment('YYYY-MM-DD HH:mm')"
                >
                </a-list-item-meta>
              </a-list-item>
            </a-list>
          </a-tab-pane>
        </a-tabs>
      </a-spin>
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
      loading: false,
      visible: false
    };
  },
  computed: {
    count() {
      return this.$store.getters.message.filter(f => !f.read).length;
    },
    unreadData() {
      return this.$store.getters.message.filter(f => !f.read);
    },
    readData() {
      return this.$store.getters.message.filter(f => f.read);
    }
  },
  methods: {
    fetchNotice() {
      this.visible = !this.visible;
    },
    readMessage(item) {
      this.$store.dispatch("readMessage", item);
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
