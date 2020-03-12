<template>
  <page-view>
    <a-card>
      <div class="table-page-search-wrapper">
        <a-form layout="inline">
          <a-row :gutter="48">
            <a-col :md="8" :sm="24">
              <a-form-item label="Role">
                <a-select v-model="queryParam.role">
                  <a-select-option key="0" :value="null">All</a-select-option>
                  <a-select-option
                    v-for="data in RoleOptions"
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
        <template slot="active" slot-scope="data">
          <a-checkbox :checked="data" disabled />
        </template>

        <template slot="admin" slot-scope="data">
          <a-checkbox :checked="data" disabled />
        </template>

        <template slot="action" slot-scope="data">
          <template>
            <router-link :to="{ name: 'User', params: { id: data.id } }">
              <span>Detail</span>
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
import { RoleOptions } from "./const";

export default {
  components: {
    PageView,
    STable
  },
  data() {
    return {
      RoleOptions,
      queryParam: {
        role: null
      },
      columns: [
        {
          title: "NAME",
          dataIndex: "name"
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
          dataIndex: "role",
          customRender: (text, index, row) => {
            return <span>{RoleOptions[text].label}</span>;
          }
        },
        {
          title: "ADMIN",
          dataIndex: "is_superuser",
          width: "80px",
          scopedSlots: { customRender: "admin" }
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
