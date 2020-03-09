<template>
  <page-view :title="title">
    <a-card
      :bordered="false"
      :tabList="[
        {
          key: 'Base',
          scopedSlots: { tab: 'tab_base' }
        },
        {
          key: 'Other',
          tab: 'Other'
        },
        {
          key: 'Job',
          tab: 'Job'
        },
        {
          key: 'Comment',
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
      <template slot="tab_base" slot-scope="item">
        <a-badge :dot="null">
          <span href="#" class="head-example">{{ item.key }}</span>
        </a-badge>
      </template>

      <base-info v-if="tabKey === 'Base'" @title="setTitle"> </base-info>
      <other-info v-else-if="tabKey === 'Other'"></other-info>
      <job v-else-if="tabKey === 'Job'"></job>
      <comment v-else-if="tabKey === 'Comment'"></comment>
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
      tabKey: "Base"
    };
  },
  methods: {
    setTitle(val) {
      this.title = "Order: " + val;
    }
  }
};
</script>
