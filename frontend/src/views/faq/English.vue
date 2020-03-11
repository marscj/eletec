<template>
  <a-spin :spinning="loading">
    <div v-if="listData.length">
      <a-collapse :bordered="false">
        <template v-slot:expandIcon="props">
          <a-icon type="caret-right" :rotate="props.isActive ? 90 : 0" />
        </template>
        <a-collapse-panel
          v-for="data in listData"
          :key="data.id"
          :header="data.title"
          class="bg-gray-400 rounded mb-10 border-none overflow-hidden"
        >
          <p>{{ data.content }}</p>
        </a-collapse-panel>
      </a-collapse>
    </div>
    <a-empty v-else />
  </a-spin>
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
