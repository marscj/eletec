<template>
  <page-view :title="title">
    <a-card
      :bordered="false"
      :tabList="[
        {
          key: 'order',
          tab: 'Order'
        },
        {
          key: 'contract',
          tab: 'Contract'
        },
        {
          key: 'job',
          tab: 'Job'
        }
      ]"
      :activeTabKey="tabKey"
      @tabChange="onTabChange"
    >
      <div v-if="tabKey === 'order'">
        <a-form :form="form">
          <div class="title">Base Info</div>
          <a-row :gutter="16">
            <a-col :span="8">
              <a-form-item label="Service">
                <validation-provider vid="service" v-slot="{ errors }">
                  <a-select v-model="form.service" disabled>
                    <a-select-option
                      v-for="data in ServiceOptions"
                      :key="data.value"
                      :value="data.value"
                      >{{ data.label }}</a-select-option
                    >
                  </a-select>
                  <span class="errorText">{{ errors[0] }}</span>
                </validation-provider>
              </a-form-item>
            </a-col>

            <a-col :span="8">
              <a-form-item label="Main Info">
                <validation-provider
                  vid="main_info"
                  name="main info"
                  v-slot="{ errors }"
                >
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
                  <span class="errorText">{{ errors[0] }}</span>
                </validation-provider>
              </a-form-item>
            </a-col>

            <a-col :span="8">
              <a-form-item label="Sub Info">
                <validation-provider
                  vid="sub_info"
                  name="sub info"
                  v-slot="{ errors }"
                >
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
                  <span class="errorText">{{ errors[0] }}</span>
                </validation-provider>
              </a-form-item>
            </a-col>

            <a-col :span="8">
              <a-form-item label="From Date">
                <validation-provider
                  vid="from_date"
                  name="from date"
                  v-slot="{ errors }"
                >
                  <a-input v-model="form.from_date" disabled></a-input>
                  <span class="errorText">{{ errors[0] }}</span>
                </validation-provider>
              </a-form-item>
            </a-col>

            <a-col :span="8">
              <a-form-item label="To Date">
                <validation-provider
                  vid="to_date"
                  name="to date"
                  v-slot="{ errors }"
                >
                  <a-input v-model="form.to_date" disabled></a-input>
                  <span class="errorText">{{ errors[0] }}</span>
                </validation-provider>
              </a-form-item>
            </a-col>

            <a-col :span="8">
              <a-form-item label="Status">
                <validation-provider vid="status" v-slot="{ errors }">
                  <a-select v-model="form.status">
                    <a-select-option
                      v-for="data in StatusOptions"
                      :key="data.value"
                      :value="data.value"
                      >{{ data.label }}</a-select-option
                    >
                  </a-select>
                  <span class="errorText">{{ errors[0] }}</span>
                </validation-provider>
              </a-form-item>
            </a-col>

            <a-col :span="24">
              <a-form-item label="Address">
                <validation-provider vid="address" v-slot="{ errors }">
                  <a-input v-model="form.address"></a-input>
                  <span class="errorText">{{ errors[0] }}</span>
                </validation-provider>
              </a-form-item>
            </a-col>
          </a-row>

          <div align="right">
            <a-button type="primary">
              Submit
            </a-button>
          </div>
        </a-form>

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

        <div v-if="form.user" class="pt-10">
          <description-list title="User Info">
            <detail-list-item term="Name">
              <router-link :to="{ name: 'UserProfile', id: this.form.user.id }">
                {{ form.user.name }}
              </router-link>
            </detail-list-item>

            <detail-list-item term="Phone">
              <router-link :to="{ name: 'UserProfile', id: this.form.user.id }">
                {{ form.user.phone_number }}
              </router-link>
            </detail-list-item>

            <detail-list-item term="Email">
              <router-link :to="{ name: 'UserProfile', id: this.form.user.id }">
                {{ form.user.email }}
              </router-link>
            </detail-list-item>
          </description-list>

          <a-divider class="mb-10" />
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
      <div v-else-if="tabKey === 'contract'">
        contract
      </div>
      <div v-else>
        comment
      </div>
    </a-card>
  </page-view>
</template>

<script>
import { getOrder } from "@/api/order";
import { PageView } from "@/layouts";
import { STable, DescriptionList } from "@/components";
const DetailListItem = DescriptionList.Item;

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
    DescriptionList,
    DetailListItem,
    STable
  },
  data() {
    return {
      StatusOptions,
      ServiceOptions,
      MainInfoOptions,
      SubInfoOptions,
      form: {},
      markers: [],
      tabKey: "order",
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
        })
        .finally(() => {
          this.loading = false;
        });
    },
    onTabChange(key) {
      this.tabKey = key;
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
