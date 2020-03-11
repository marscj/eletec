<template>
  <div>
    <a-collapse :bordered="false">
      <template v-slot:expandIcon="props">
        <a-icon type="caret-right" :rotate="props.isActive ? 90 : 0" />
      </template>
      <a-collapse-panel
        header="This is panel header 1"
        key="1"
        :style="customStyle"
      >
        <p>{{ text }}</p>
      </a-collapse-panel>
    </a-collapse>
  </div>
</template>

<script>
import { getFaqs, updateFaq, createFaq, deleteFaq } from "@/api/faq";
export default {
  data() {
    return {
      loading: false,
      uploading: false,
      listData: []
    };
  },
  mounted() {
    this.getListData();
  },
  methods: {
    getListData() {
      this.loading = true;
      getFaqs({ lanuage: "en" })
        .then(res => {
          this.listData = res.result;
        })
        .finally(() => {
          this.loading = false;
        });
    },
    deleteData(val) {
      this.loading = true;
      deleteFaq(val.id)
        .then(res => {
          this.getListData();
        })
        .finally(() => {
          this.loading = false;
        });
    }
  }
};
</script>

<style>
.avatar-uploader > .ant-upload {
  width: 128px;
  height: 128px;
}
.ant-upload-select-picture-card i {
  font-size: 32px;
  color: #999;
}

.ant-upload-select-picture-card .ant-upload-text {
  margin-top: 8px;
  color: #666;
}
</style>
