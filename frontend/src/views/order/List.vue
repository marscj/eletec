<template>
  <page-view>
    <a-card>
      <div class="table-page-search-wrapper">
        <a-form layout="inline">
          <a-row :gutter="48">
            <a-col :md="8" :sm="24">
              <a-form-item label="Status">
                <a-select v-model="queryParam.status">
                  <a-select-option key="0" :value="null">All</a-select-option>
                  <a-select-option
                    v-for="data in StatusOptions"
                    :key="data.value"
                    :value="data.value"
                    >{{ data.label }}</a-select-option
                  >
                </a-select>
              </a-form-item>
            </a-col>
            <a-col :md="8" :sm="24">
              <a-form-item>
                <a-button type="primary" @click="() => $refs.table.refresh()">
                  Search
                </a-button>
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

        <template slot="date" slot-scope="text">
          <span>
            {{ text | moment("MM-DD") }}
          </span>
        </template>

        <template slot="info" slot-scope="data">
          <ul style="padding: 0px 20px;">
            <li v-if="data.service != undefined">
              Service:
              <em class="font-bold text-blue-500">{{
                ServiceOptions[data.service].label
              }}</em>
            </li>
            <li v-if="data.main_info != undefined && data.service != undefined">
              MainInfo:
              <em class="font-bold text-blue-500">
                {{ MainInfoOptions[data.service][data.main_info] }}
              </em>
              <ul style="padding: 0px 20px;">
                <li
                  v-if="
                    data.sub_info != undefined &&
                      data.main_info != undefined &&
                      data.service != undefined
                  "
                >
                  SubInfo:
                  <em class="font-bold text-blue-500">
                    {{
                      SubInfoOptions[data.service][data.main_info][
                        data.sub_info
                      ]
                    }}
                  </em>
                </li>
              </ul>
            </li>

            <li v-if="data.from_date">
              From Date:
              <em class="font-bold text-blue-500">
                {{ data.from_date | moment("YYYY-MM-DD HH:mm") }}
              </em>
            </li>

            <li v-if="data.to_date">
              To Date:
              <em class="font-bold text-blue-500">
                {{ data.to_date | moment("YYYY-MM-DD HH:mm") }}
              </em>
            </li>
          </ul>
        </template>

        <template slot="job" slot-scope="data">
          <ul v-if="data" style="padding: 0px 20px;">
            <li v-for="job in data" :key="job.id">
              <ellipsis :length="30" tooltip>
                {{ job.orderID }}
              </ellipsis>
            </li>
          </ul>
        </template>

        <template slot="user" slot-scope="data">
          <p>{{ data.name }}</p>
          <p>{{ data.phone_number }}</p>
        </template>

        <template slot="action" slot-scope="data">
          <template>
            <router-link
              :to="{
                name: 'Order',
                params: { id: data.id },
                query: { tab: 'base' }
              }"
            >
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
  ServiceOptions,
  MainInfoOptions,
  SubInfoOptions
} from "./const";
import moment from "moment";

export default {
  components: {
    PageView,
    STable,
    Ellipsis
  },
  data() {
    return {
      StatusOptions,
      ServiceOptions,
      MainInfoOptions,
      SubInfoOptions,
      queryParam: {
        status: null
      },
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
          title: "JOB",
          dataIndex: "job",
          width: "172px",
          scopedSlots: { customRender: "job" }
        },
        {
          title: "USER",
          dataIndex: "user",
          width: "120px",
          scopedSlots: { customRender: "user" }
        },
        {
          title: "CREATE",
          dataIndex: "create_at",
          width: "80px",
          scopedSlots: { customRender: "date" }
        },
        {
          title: "STATUS",
          dataIndex: "status",
          width: "100px",
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
