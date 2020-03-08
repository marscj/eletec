<template>
  <div :title="title">
    <validation-observer ref="observer">
      <validation-provider vid="non_field_errors" v-slot="{ errors }">
        <span class="errorText">{{ errors[0] }}</span>
      </validation-provider>

      <validation-provider vid="address" v-slot="{ errors }">
        <span class="errorText" v-if="errors.length"
          >Address: {{ errors[0] }}</span
        >
      </validation-provider>

      <validation-provider
        vid="contract_id"
        name="contract"
        v-slot="{ errors }"
      >
        <span class="errorText" v-if="errors.length">
          Contract: {{ errors[0] }}</span
        >
      </validation-provider>

      <a-card
        :bordered="false"
        :tabList="[
          {
            key: 'order',
            tab: 'Order'
          },
          {
            key: 'job',
            tab: 'Job'
          }
        ]"
        :activeTabKey="tabKey"
        @tabChange="
          key => {
            tabKey = key;
          }
        "
        :loading="loading"
      >
        <div v-if="tabKey === 'order'">
          <a-form :form="form" :submit="submit">
            <div class="title">Base Info</div>
            <a-row :gutter="16">
              <a-col :span="8">
                <a-form-item label="Service">
                  <a-select v-model="form.service" disabled>
                    <a-select-option
                      v-for="data in ServiceOptions"
                      :key="data.value"
                      :value="data.value"
                      >{{ data.label }}</a-select-option
                    >
                  </a-select>
                </a-form-item>
              </a-col>

              <a-col :span="8">
                <a-form-item label="Main Info">
                  <a-select
                    v-model="form.main_info"
                    v-if="form.service != null"
                    disabled
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

              <a-col :span="8">
                <a-form-item label="Sub Info">
                  <a-select
                    v-model="form.sub_info"
                    v-if="form.service != null && form.main_info != null"
                    disabled
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

              <a-col :span="8">
                <a-form-item label="From Date">
                  <a-input v-model="form.from_date" disabled></a-input>
                </a-form-item>
              </a-col>

              <a-col :span="8">
                <a-form-item label="To Date">
                  <a-input v-model="form.to_date" disabled></a-input>
                </a-form-item>
              </a-col>

              <a-col :span="8">
                <a-form-item label="Status">
                  <a-select v-model="form.status">
                    <a-select-option
                      v-for="data in StatusOptions"
                      :key="data.value"
                      :value="data.value"
                      >{{ data.label }}</a-select-option
                    >
                  </a-select>
                </a-form-item>
              </a-col>

              <a-col :span="24">
                <a-form-item label="Address">
                  <a-input v-model="form.address"></a-input>
                </a-form-item>
              </a-col>

              <a-col :span="24">
                <a-form-item label="Contract">
                  <a-select v-model="form.contract_id" allowClear>
                    <a-select-option
                      v-for="data in contracts"
                      :key="data.id"
                      :value="data.id"
                    >
                      <a-popover>
                        <template slot="content">
                          <ul class="px-4">
                            <li>Option: {{ Options[data.option].label }}</li>
                            <li>Issue: {{ data.issue_date }}</li>
                            <li>Expiry: {{ data.expiry_date }}</li>
                            <li v-if="data.visits.length">
                              <span>Usage Count:</span>
                              <ul class="px-4">
                                <li
                                  v-for="(item, index) in data.visits"
                                  :key="index"
                                >
                                  <span>
                                    {{ ServiceOptions[item.service].label }} :
                                    {{ item.count }}
                                  </span>
                                </li>
                              </ul>
                            </li>
                            <li v-else>
                              Usage Count: No data
                            </li>
                            <li>Address: {{ data.address }}</li>
                            <li>Remark: {{ data.remark }}</li>
                          </ul>
                        </template>
                        {{ data.contractID }}
                      </a-popover>
                    </a-select-option>
                  </a-select>
                </a-form-item>
              </a-col>
            </a-row>

            <div align="right">
              <a-button type="primary" html-type="submit" @click="submit">
                Submit
              </a-button>
            </div>
          </a-form>

          <div v-if="form.other_info || form.image" class="pt-10">
            <description-list title="Other Info">
              <a-card>
                <img
                  v-for="data in form.images"
                  :key="data.id"
                  :src="data.image.medium"
                  alt="image"
                  slot="cover"
                  class="pb-2"
                />

                <a-card-meta :description="form.other_info"> </a-card-meta>
              </a-card>
            </description-list>
          </div>

          <div v-if="form.lat && form.lng" class="pt-10">
            <div class="title">Map</div>
            <gmap-map
              class="map"
              :center="{ lat: form.lat, lng: form.lng }"
              :zoom="16"
              map-type-id="satellite"
            >
              <gmap-marker
                :key="index"
                v-for="(m, index) in markers"
                :position="m.position"
                :clickable="true"
                :draggable="true"
                @click="center = m.position"
              />
            </gmap-map>
          </div>

          <div v-if="form.user" class="pt-10">
            <description-list title="User Info">
              <detail-list-item term="Name">
                <router-link
                  :to="{ name: 'UserProfile', id: this.form.user.id }"
                >
                  {{ form.user.name }}
                </router-link>
              </detail-list-item>

              <detail-list-item term="Phone">
                <router-link
                  :to="{ name: 'UserProfile', id: this.form.user.id }"
                >
                  {{ form.user.phone_number }}
                </router-link>
              </detail-list-item>

              <detail-list-item term="Email">
                <router-link
                  :to="{ name: 'UserProfile', id: this.form.user.id }"
                >
                  {{ form.user.email }}
                </router-link>
              </detail-list-item>
            </description-list>
          </div>

          <div v-if="form.comments" class="pt-10">
            <div class="title">Comments</div>
            <div>
              <a-list
                class="comment-list"
                itemLayout="horizontal"
                :dataSource="form.comments"
              >
                <a-list-item slot="renderItem" slot-scope="item">
                  <a-comment
                    :author="
                      item.user.name ? item.user.name : item.user.username
                    "
                    :avatar="
                      item.user.photo ? item.user.photo.image.thumbnail : null
                    "
                  >
                    <div slot="content">
                      <p>{{ item.comment }}</p>
                      <a-rate v-model="item.rating" />
                    </div>
                    <span slot="datetime">{{ item.create_at }}</span>
                  </a-comment>
                </a-list-item>
              </a-list>
            </div>
          </div>
        </div>

        <div v-else-if="tabKey === 'job'">
          <s-table
            style="margin-bottom: 24px"
            row-key="id"
            :columns="goodsColumns"
            :data="loadGoodsData"
          >
          </s-table>
        </div>
      </a-card>
    </validation-observer>
  </div>
</template>

<script>
import { PageView } from "@/layouts";
import { STable, DescriptionList } from "@/components";
const DetailListItem = DescriptionList.Item;

import { getOrder, updateOrder } from "@/api/order";
import { getContracts } from "@/api/user";

import {
  StatusOptions,
  ServiceOptions,
  MainInfoOptions,
  SubInfoOptions
} from "./const";

import { Options } from "../user/const";

import moment from "moment";

export default {
  components: {
    DescriptionList,
    DetailListItem,
    STable
  },
  data() {
    return {
      Options,
      StatusOptions,
      ServiceOptions,
      MainInfoOptions,
      SubInfoOptions,
      form: {},
      contracts: [],
      markers: [],
      tabKey: "order",
      loading: false,
      goodsColumns: [
        {
          title: "商品编号",
          dataIndex: "id",
          key: "id"
        },
        {
          title: "商品名称",
          dataIndex: "name",
          key: "name"
        },
        {
          title: "商品条码",
          dataIndex: "barcode",
          key: "barcode"
        },
        {
          title: "单价",
          dataIndex: "price",
          key: "price",
          align: "right"
        },
        {
          title: "数量（件）",
          dataIndex: "num",
          key: "num",
          align: "right"
        },
        {
          title: "金额",
          dataIndex: "amount",
          key: "amount",
          align: "right"
        }
      ],
      // 加载数据方法 必须为 Promise 对象
      loadGoodsData: () => {
        return new Promise(resolve => {
          resolve({
            data: [
              {
                id: "1234561",
                name: "矿泉水 550ml",
                barcode: "12421432143214321",
                price: "2.00",
                num: "1",
                amount: "2.00"
              },
              {
                id: "1234562",
                name: "凉茶 300ml",
                barcode: "12421432143214322",
                price: "3.00",
                num: "2",
                amount: "6.00"
              },
              {
                id: "1234563",
                name: "好吃的薯片",
                barcode: "12421432143214323",
                price: "7.00",
                num: "4",
                amount: "28.00"
              },
              {
                id: "1234564",
                name: "特别好吃的蛋卷",
                barcode: "12421432143214324",
                price: "8.50",
                num: "3",
                amount: "25.50"
              }
            ],
            pageSize: 10,
            pageNo: 1,
            totalPage: 1,
            totalCount: 10
          });
        }).then(res => {
          return res;
        });
      }
    };
  },
  filters: {
    statusFilter(status) {
      const statusMap = {
        processing: "进行中",
        success: "完成",
        failed: "失败"
      };
      return statusMap[status];
    }
  },
  computed: {
    title() {
      return this.form.orderID ? "Order: " + this.form.orderID : "Order";
    }
  },
  watch: {
    form(val) {
      if (val) {
        this.markers.push({
          id: this.lastId,
          position: {
            lat: val.lat,
            lng: val.lng
          },
          opacity: 1,
          draggable: true,
          enabled: true,
          clicked: 0,
          rightClicked: 0,
          dragended: 0,
          ifw: false
        });
      }
    }
  },
  mounted() {
    this.getOrderData();
  },
  methods: {
    moment,
    getOrderData() {
      this.loading = true;
      getOrder(this.$route.params.id)
        .then(res => {
          const { result } = res;
          this.form = result;

          return getContracts({ user_id: this.form.user.id }).then(res => {
            this.contracts = res.result;
          });
        })
        .finally(() => {
          this.loading = false;
        });
    },
    submit() {
      this.loading = true;
      updateOrder(this.$route.params.id, {
        status: this.form.status,
        address: this.form.address,
        user_id: this.form.user_id,
        contract_id: this.form.contract_id
      })
        .then(res => {
          const { result } = res;
          this.form = result;

          return getContracts({ user_id: this.form.user.id }).then(res => {
            this.contracts = res.result;
          });
        })
        .catch(error => {
          if (error.response) {
            this.$refs.observer.setErrors(error.response.data.result);
          }
        })
        .finally(() => {
          this.loading = false;
        });
    }
  }
};
</script>

<style lang="less" scoped>
.title {
  color: rgba(0, 0, 0, 0.85);
  font-size: 16px;
  font-weight: 500;
  margin-bottom: 16px;
}

.map {
  width: 100%;
  height: 600px;
  display: block;
}
</style>
