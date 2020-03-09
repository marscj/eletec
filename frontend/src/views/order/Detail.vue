<template>
  <page-view :title="title">
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
      <base-info v-if="tabKey === 'base'" @title="setTitle"> </base-info>
      <other-info v-else-if="tabKey === 'other'"></other-info>
      <job v-else-if="tabKey === 'job'"></job>
      <comment v-else-if="tabKey === 'comment'"></comment>
    </a-card>
  </page-view>
</template>

<script>
import { PageView } from "@/layouts";
import { BaseInfo, OtherInfo, Job, Comment } from "./index";

export default {
  components: {
    PageView,
    BaseInfo,
    OtherInfo,
    Job,
    Comment
  },
  data() {
    return {
      title: "Order",
      tabKey: "base"
    };
  },
  methods: {
    setTitle(val) {
      this.title = "Order: " + val;
    }
  }
};
</script>
