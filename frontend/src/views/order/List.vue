<template>
  <page-view>
    <a-card>
      <div class="table-page-search-wrapper">
        <a-form layout="inline" :form="form">
          <a-row :gutter="24">
            <a-col :md="8" :sm="24">
              <a-form-item label="Search">
                <a-input v-model="queryParam.search"></a-input>
              </a-form-item>
            </a-col>
            <a-col :md="8" :sm="24">
              <a-form-item label="From Date">
                <a-range-picker
                  :value="rangeDay"
                  @change="value => (rangeDay = value)"
                />
              </a-form-item>
            </a-col>

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
            <a-col :md="12" :sm="24">
              <a-form-item>
                <a-button
                  type="primary"
                  html-type="submit"
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

      <a-modal v-model="modal" title="Create User" @ok="submit">
        <validation-observer ref="observer">
          <validation-provider name="non_field_errors" v-slot="{ errors }">
            <span class="errorText">{{ errors[0] }}</span>
          </validation-provider>
          <a-form :form="form" :submit="submit">
            <a-row :gutter="16">
              <a-col :span="12">
                <a-form-item label="Service">
                  <a-select v-model="form.service">
                    <a-select-option
                      v-for="data in ServiceOptions"
                      :key="data.value"
                      :value="data.value"
                      >{{ data.label }}</a-select-option
                    >
                  </a-select>
                </a-form-item>
              </a-col>

              <a-col :span="12">
                <a-form-item label="User ID">
                  <validation-provider vid="user_id" v-slot="{ errors }">
                    <a-input v-model="form.user_id"> </a-input>
                    <span class="errorText">{{ errors[0] }}</span>
                  </validation-provider>
                </a-form-item>
              </a-col>

              <a-col :span="12">
                <a-form-item label="Main Info">
                  <a-select
                    v-model="form.main_info"
                    v-if="form.service != null"
                  >
                    <a-select-option
                      v-for="(data, index) in MainInfoOptions[form.service]"
                      :key="index"
                      :value="index"
                      >{{ data }}</a-select-option
                    >
                  </a-select>
                </a-form-item>
              </a-col>

              <a-col :span="12">
                <a-form-item label="Sub Info">
                  <a-select
                    v-model="form.sub_info"
                    v-if="form.service != null && form.main_info != null"
                  >
                    <a-select-option
                      v-for="(data, index) in SubInfoOptions[form.service][
                        form.main_info
                      ]"
                      :key="index"
                      :value="index"
                      >{{ data }}</a-select-option
                    >
                  </a-select>
                </a-form-item>
              </a-col>

              <a-col :span="12">
                <a-form-item label="From Date">
                  <a-date-picker
                    v-model="from"
                    format="YYYY-MM-DD HH:mm"
                    class="w-full"
                  ></a-date-picker>
                </a-form-item>
              </a-col>

              <a-col :span="12">
                <a-form-item label="To Date">
                  <a-date-picker
                    v-model="to"
                    format="YYYY-MM-DD HH:mm"
                    class="w-full"
                  ></a-date-picker>
                </a-form-item>
              </a-col>

              <a-col :span="24">
                <a-form-item label="Address">
                  <validation-provider name="address" v-slot="{ errors }">
                    <a-input v-model="form.address"></a-input>
                    <span class="errorText">{{ errors[0] }}</span>
                  </validation-provider>
                </a-form-item>
              </a-col>
            </a-row>
          </a-form>
        </validation-observer>
      </a-modal>
    </a-card>
  </page-view>
</template>

<script>
import { PageView, RouteView } from "@/layouts";
import { STable, Ellipsis } from "@/components";
import { getOrders, createOrder } from "@/api/order";
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
      rangeDay: undefined,
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
      },
      modal: false,
      from: moment(new Date()),
      to: moment(new Date()),
      form: {}
    };
  },
  watch: {
    rangeDay(newQuestion, oldQuestion) {
      if (
        newQuestion != null &&
        newQuestion != undefined &&
        newQuestion.length > 0
      ) {
        this.queryParam.start = newQuestion[0].format("YYYY-MM-DD 00:00:00");
        this.queryParam.end = newQuestion[1].format("YYYY-MM-DD 23:59:59");
      } else {
        this.queryParam.start = undefined;
        this.queryParam.end = undefined;
      }
    }
  },
  methods: {
    moment,
    openModal() {
      this.modal = true;
      this.form = {
        service: 0,
        main_info: 0,
        sub_info: 0
      };
    },
    submit() {
      createOrder(
        Object.assign(this.form, {
          from_date: this.from.format("YYYY-MM-DD HH:mm:ss"),
          to_date: this.to.format("YYYY-MM-DD HH:mm:ss")
        })
      )
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
