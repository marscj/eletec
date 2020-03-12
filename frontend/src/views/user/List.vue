<template>
  <page-view>
    <a-card>
      <div class="table-page-search-wrapper">
        <a-form layout="inline">
          <a-row :gutter="48">
            <a-col :md="8" :sm="24">
              <a-form-item label="Search">
                <a-input v-model="queryParam.search"></a-input>
              </a-form-item>
            </a-col>
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
                <a-button
                  type="primary"
                  html-type="submit"
                  icon="search"
                  @click="() => $refs.table.refresh()"
                >
                  Search
                </a-button>
              </a-form-item>
            </a-col>
          </a-row>
        </a-form>
      </div>

      <div class="table-operator">
        <a-button type="primary" icon="plus" @click="openModal">New</a-button>
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

      <a-modal v-model="modal" title="Create User" @ok="submit">
        <validation-observer ref="observer">
          <validation-provider name="non_field_errors" v-slot="{ errors }">
            <span class="errorText">{{ errors[0] }}</span>
          </validation-provider>

          <a-form
            :form="form"
            :submit="submit"
            :label-col="{ span: 6 }"
            :wrapper-col="{ span: 12 }"
          >
            <a-form-item label="Phone Number">
              <validation-provider
                vid="phone_number"
                name="phone number"
                v-slot="{ errors }"
              >
                <a-input v-model="form.phone_number">
                  <a-icon
                    slot="prefix"
                    type="mobile"
                    :style="{ color: 'rgba(0,0,0,.25)' }"
                  />
                  <a-select
                    slot="addonBefore"
                    defaultValue="+971"
                    style="width:80px"
                  >
                    <a-select-option value="+971">+971</a-select-option>
                  </a-select>
                </a-input>
                <span class="errorText">{{ errors[0] }}</span>
              </validation-provider>
            </a-form-item>
          </a-form>
        </validation-observer>
      </a-modal>
    </a-card>
  </page-view>
</template>

<script>
import { PageView, RouteView } from "@/layouts";
import { STable, Ellipsis } from "@/components";
import { getUsers, createUser } from "@/api/user";
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
          title: "ID",
          dataIndex: "id"
        },
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
      },
      modal: false,
      form: {}
    };
  },
  methods: {
    openModal() {
      this.modal = true;
      this.form = {};
    },
    submit() {
      createUser({
        username: "+971" + this.form.phone_number,
        phone_number: "+971" + this.form.phone_number
      })
        .then(res => {
          this.modal = false;
          this.$refs.table.refresh();
        })
        .catch(error => {
          if (error.response) {
            this.$refs.observer.setErrors(error.response.data.result);
          }
        });
    }
  }
};
</script>
