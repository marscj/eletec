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
        <template slot="active" slot-scope="data">
          <a-checkbox :checked="data" disabled />
        </template>

        <template slot="name" slot-scope="data">
          <span>{{ data.first_name }} {{ data.last_name }} </span>
        </template>

        <template slot="groups" slot-scope="data">
          <span>{{
            $_.join(
              data.map(f => f.name),
              ", "
            )
          }}</span>
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
          width: "80px"
        },
        {
          title: "NAME",
          scopedSlots: { customRender: "name" }
        },
        {
          title: "PHONE",
          dataIndex: "phone_number"
        },
        {
          title: "EMAIL",
          dataIndex: "email"
        },
        {
          title: "ROLE",
          dataIndex: "role"
        },
        {
          title: "GROUP",
          dataIndex: "groups",
          scopedSlots: { customRender: "groups" }
        },
        {
          title: "ACTIVE",
          dataIndex: "is_active",
          width: "80px",
          scopedSlots: { customRender: "active" }
        },
        {
          title: "ACTION",
          width: "80px",
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
