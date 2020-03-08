<template>
  <div :title="title">
    <a-card
      :bordered="false"
      :tabList="[
        {
          key: 'base',
          tab: 'Base'
        },
        {
          key: 'other',
          tab: 'Other'
        },
        {
          key: 'job',
          tab: 'Job'
        },
        {
          key: 'comment',
          tab: 'Comment'
        }
      ]"
      :activeTabKey="tabKey"
      @tabChange="
        key => {
          tabKey = key;
        }
      "
    >
      <base-info v-if="tabKey === 'base'"> </base-info>
      <div v-else-if="tabKey === 'other'"></div>
      <div v-else-if="tabKey === 'job'"></div>
      <div v-else-if="tabKey === 'comment'"></div>
    </a-card>
  </div>
</template>

<script>
import { PageView } from "@/layouts";
import { BaseInfo } from "./index";

export default {
  components: {
    BaseInfo
  },
  data() {
    return {
      tabKey: "base"
    };
  }
  // computed: {
  //   title() {
  //     return this.form.orderID ? "Order: " + this.form.orderID : "Order";
  //   }
  // }
};
</script>
