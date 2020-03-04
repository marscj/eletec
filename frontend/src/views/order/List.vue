<template>
  <page-view>
    <a-card>
      <div class="table-page-search-wrapper">
        <a-form layout="inline">
          <a-row :gutter="48">
            <a-col :md="8" :sm="24">
              <a-form-item label="">
                <a-input v-model="queryParam.id" placeholder="" />
              </a-form-item>
            </a-col>
          </a-row>
        </a-form>
      </div>

      <div class="table-operator">
        <a-button type="primary" icon="plus" @click="$refs.createModal.add()"
          >New</a-button
        >
      </div>

      <s-table
        ref="table"
        size="default"
        :rowKey="record => record.id"
        :columns="columns"
        :data="loadData"
        :pageURI="true"
        showPagination="auto"
        bordered
      >
        <template slot="datetime" slot-scope="text">
          <span>
            {{ text | moment("YYYY-MM-DD HH:mm") }}
          </span>
        </template>

        <template slot="info" slot-scope="data">
          <div v-if="data.category != undefined">
            Category:
            <em class="font-bold text-blue-500">{{
              CategoryOptions[data.category].label
            }}</em>
          </div>
          <div v-if="data.main_info != undefined && data.category != undefined">
            MainInfo:
            <em class="font-bold text-blue-500">
              {{ MainInfoOptions[data.category][data.main_info] }}
            </em>
          </div>
          <div
            v-if="
              data.sub_info != undefined &&
                data.main_info != undefined &&
                data.category != undefined
            "
          >
            SubInfo:
            <em class="font-bold text-blue-500">
              {{ SubInfoOptions[data.category][data.main_info][data.sub_info] }}
            </em>
          </div>
          <div v-if="data.other_info">
            <span>OtherInfo:</span>
            <em class="font-bold text-blue-500">
              {{ data.other_info }}
            </em>
          </div>
          <div v-if="data.from_date">
            Form:
            <em class="font-bold text-blue-500">
              {{ data.from_date | moment("YYYY-MM-DD HH:mm") }}
            </em>
          </div>

          <div v-if="data.to_date">
            To:
            <em class="font-bold text-blue-500">
              {{ data.to_date | moment("YYYY-MM-DD HH:mm") }}
            </em>
          </div>
        </template>

        <template slot="action" slot-scope="data">
          <template>
            <router-link :to="{ name: 'User', params: { id: data.id } }">
              <span>Edit</span>
            </router-link>
          </template>
        </template>
      </s-table>
    </a-card>
  </page-view>
</template>

<script>
import { PageView, RouteView } from "@/layouts";
import { STable, Ellipsis } from "@/components";
import { getOrders } from "@/api/order";
import {
  StatusOptions,
  CategoryOptions,
  MainInfoOptions,
  SubInfoOptions
} from "./const";
import moment from "moment";

export default {
  components: {
    PageView,
    STable
  },
  data() {
    return {
      StatusOptions,
      CategoryOptions,
      MainInfoOptions,
      SubInfoOptions,
      queryParam: {},
      columns: [
        {
          title: "#",
          dataIndex: "orderID",
          width: "140px"
        },
        {
          title: "INFO",
          scopedSlots: { customRender: "info" }
        },
        {
          title: "CREATE",
          dataIndex: "create_at",
          scopedSlots: { customRender: "datetime" }
        },
        {
          title: "STATUS",
          dataIndex: "status",
          customRender: (text, index, row) => {
            return <span>{StatusOptions[text].label}</span>;
          }
        },
        {
          title: "ACTION",
          width: "80px",
          scopedSlots: { customRender: "action" }
        }
      ],
      loadData: parameter => {
        return getOrders(Object.assign(parameter, this.queryParam)).then(
          res => {
            return res.result;
          }
        );
      }
    };
  },
  methods: {
    moment
  }
};
</script>
