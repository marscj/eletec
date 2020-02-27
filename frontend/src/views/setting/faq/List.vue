<template>
  <div>
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
        <span slot="date_joined" slot-scope="text">
          <span>
            {{ text | moment("YYYY-MM-DD") }}
          </span>
        </span>
        <span slot="action">
          <template>
            <a @click="handleEdit(record)">Edit</a>
          </template>
        </span>
      </s-table>
    </a-card>
  </div>
</template>

<script>
import { STable, Ellipsis } from "@/components";

import { getUsers } from "@/api/user";

export default {
  components: {
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
