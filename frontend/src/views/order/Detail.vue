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
          scopedSlots: { tab: 'tab_other' }
        },
        {
          key: 'Job',
          scopedSlots: { tab: 'tab_job' }
        },
        {
          key: 'Comment',
          scopedSlots: { tab: 'tab_comment' }
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
        <span>{{ item.key }}</span>
      </template>

      <template slot="tab_other" slot-scope="item">
        <a-badge :count="data.image_count">
          <span>{{ item.key }}</span>
        </a-badge>
      </template>

      <template slot="tab_job" slot-scope="item">
        <a-badge :count="data.job_count">
          <span>{{ item.key }}</span>
        </a-badge>
      </template>

      <template slot="tab_comment" slot-scope="item">
        <a-badge :count="data.comment_count">
          <span>{{ item.key }}</span>
        </a-badge>
      </template>

      <base-info v-if="tabKey === 'Base'" @data="setData"> </base-info>
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
      data: {},
      title: "Order",
      tabKey: "Base"
    };
  },
  methods: {
    setData(val) {
      this.data = val;
      this.title = "Order: " + val.orderID;
    }
  }
};
</script>
