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
          style="background: #f7f7f7; border-radius: 4px; margin-bottom: 14px; border: 0; overflow: hidden"
        >
          <p class="whitespace-pre-line">{{ data.content }}</p>
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
