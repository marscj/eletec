<template>
  <page-view>
    <a-card>
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

        <template slot="action" slot-scope="data">
          <a href="#" @click="apply(data)">Apply</a>
          <a-divider type="vertical"></a-divider>
          <router-link :to="{ name: 'User', params: { id: data.id } }">
            <span>Detail</span>
          </router-link>
        </template>
      </s-table>
    </a-card>
  </page-view>
</template>

<script>
import { PageView, RouteView } from "@/layouts";
import { STable, Ellipsis } from "@/components";
import { getApplications, updateApplication } from "@/api/application";
import { RoleOptions } from "./const";

export default {
  components: {
    PageView,
    STable
  },
  data() {
    return {
      RoleOptions,
      queryParam: {},
      columns: [
        {
          title: "NAME",
          dataIndex: "user.name",
          align: "center"
        },
        {
          title: "PHONE",
          dataIndex: "user.phone_number",
          align: "center"
        },
        {
          title: "EMAIL",
          dataIndex: "user.email",
          align: "center"
        },
        {
          title: "CREATE",
          dataIndex: "create_at",
          width: "160px",
          scopedSlots: { customRender: "datetime" },
          align: "center"
        },
        {
          title: "ACTION",
          width: "140px",
          scopedSlots: { customRender: "action" },
          align: "center"
        }
      ],
      loadData: parameter => {
        return getApplications(Object.assign(parameter, this.queryParam)).then(
          res => {
            return res.result;
          }
        );
      }
    };
  },
  methods: {
    apply(val) {
      updateApplication(
        val.id,
        Object.assign(val, {
          apply: true
        })
      ).then(res => {
        this.$refs.table.refresh();
      });
    }
  }
};
</script>
