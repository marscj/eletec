<template>
  <page-view :title="title">
    <a-card
      :bordered="false"
      :tabList="[
        {
          key: 'base',
          scopedSlots: { tab: 'tab_base' }
        },
        {
          key: 'addition',
          scopedSlots: { tab: 'tab_addition' }
        },
        {
          key: 'job',
          scopedSlots: { tab: 'tab_job' }
        },
        {
          key: 'comment',
          scopedSlots: { tab: 'tab_comment' }
        }
      ]"
      :activeTabKey="$route.query.tab"
      @tabChange="tabChange"
    >
      <template slot="tab_base">
        <span class="text-lg">Base</span>
      </template>

      <template slot="tab_addition">
        <a-badge :count="data.image_count" :offset="[12]">
          <span class="text-lg">Addition</span>
        </a-badge>
      </template>

      <template slot="tab_job">
        <a-badge :count="data.job_count" :offset="[12]">
          <span class="text-lg">Job</span>
        </a-badge>
      </template>

      <template slot="tab_comment">
        <a-badge :count="data.comment_count" :offset="[12]">
          <span class="text-lg">Comment</span>
        </a-badge>
      </template>

      <base-info v-if="tab === 'base'" @data="setData"></base-info>
      <addition v-else-if="tab === 'addition'"></addition>
      <job v-else-if="tab === 'job'"></job>
      <comment v-else-if="tab === 'comment'"></comment>
    </a-card>
  </page-view>
</template>

<script>
import { PageView } from "@/layouts";
import { BaseInfo, Addition, Job, Comment } from "./index";

export default {
  components: {
    PageView,
    BaseInfo,
    Addition,
    Job,
    Comment
  },
  data() {
    return {
      data: {},
      title: "Order"
    };
  },
  computed: {
    tab() {
      return this.$route.query.tab ? this.$route.query.tab : "base";
    }
  },
  methods: {
    setData(val) {
      this.data = val;
      this.title = "Order: " + val.orderID;
    },
    tabChange(val) {
      this.$router.push({
        ...this.$route,
        name: this.$route.name,
        query: Object.assign({}, this.$route.query, {
          tab: val
        })
      });
    }
  }
};
</script>
