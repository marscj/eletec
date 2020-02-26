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
        <template slot="date_joined" slot-scope="text">
          <span>
            {{ text | moment("YYYY-MM-DD") }}
          </span>
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

import { getUsers } from "@/api/user";

export default {
  components: {
    PageView,
    STable
  },
  data() {
    return {
      queryParam: {},
      columns: [
        {
          title: "#",
          dataIndex: "id",
          width: "100px"
        },
        {
          title: "PHONE",
          dataIndex: "phone_number"
        },
        {
          title: "ROLE",
          dataIndex: "role"
        },
        {
          title: "DATE JOIN",
          dataIndex: "date_joined",
          scopedSlots: { customRender: "date_joined" }
        },
        {
          title: "ACTION",
          width: "100px",
          scopedSlots: { customRender: "action" }
        }
      ],
      loadData: parameter => {
        return getUsers(Object.assign(parameter, this.queryParam)).then(res => {
          return res.result;
        });
      }
    };
  }
};
</script>
