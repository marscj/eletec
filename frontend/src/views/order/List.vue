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
        <!-- <template slot="date_joined" slot-scope="text">
          <span>
            {{ text | moment("YYYY-MM-DD") }}
          </span>
        </template> -->

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

const StatusOptions = [
  { value: 0, label: "New" },
  { value: 1, label: "Confirm" },
  { value: 2, label: "Complete" },
  { value: 3, label: "Pending" },
  { value: 4, label: "Cancel" },
  { value: 5, label: "Delete" }
];

const categoryOptions = [
  { value: 0, label: "Air Conditioner" },
  { value: 1, label: "Electrical" },
  { value: 2, label: "Plumbing" },
  { value: 3, label: "House Cleaning" }
];

export default {
  components: {
    PageView,
    STable
  },
  data() {
    return {
      StatusOptions,
      categoryOptions,
      queryParam: {},
      columns: [
        {
          title: "#",
          dataIndex: "orderID",
          width: "140px"
        },
        {
          title: "Category",
          dataIndex: "category",
          customRender: (text, index, row) => {
            return <span>{categoryOptions[text].label}</span>;
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
  }
};
</script>
