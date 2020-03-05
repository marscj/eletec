<template>
  <page-view :title="title">
    <a-card :bordered="false">
      <div>
        <description-list title="Base Info" v-if="form.category != undefined">
          <detail-list-item term="Category">
            {{ CategoryOptions[form.category].label }}</detail-list-item
          >
          <detail-list-item
            term="Main Info"
            v-if="form.main_info != undefined && form.category != undefined"
          >
            {{ MainInfoOptions[form.category][form.main_info] }}
          </detail-list-item>
          <detail-list-item
            term="Sub Info"
            v-if="
              form.sub_info != undefined &&
                form.main_info != undefined &&
                form.category != undefined
            "
            >{{
              SubInfoOptions[form.category][form.main_info][form.sub_info]
            }}</detail-list-item
          >
          <detail-list-item term="From Date">{{
            form.from_date | moment("YYYY-MM-DD HH:mm")
          }}</detail-list-item>
          <detail-list-item term="To Date">{{
            form.to_date | moment("YYYY-MM-DD HH:mm")
          }}</detail-list-item>
          <detail-list-item term="Create Date">{{
            form.create_at | moment("YYYY-MM-DD HH:mm")
          }}</detail-list-item>
          <detail-list-item term="Address" v-if="form.address">
            {{ form.address }}
          </detail-list-item>
        </description-list>

        <a-divider class="mb-10" />
      </div>

      <div v-if="form.lat && form.lng">
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

        <a-divider class="my-12" />
      </div>

      <div v-if="form.other_info || form.image">
        <description-list title="Other Info">
          <a-card>
            <img
              v-for="data in images"
              :key="data.id"
              :src="data.image.medium"
              alt="image"
              slot="cover"
              class="pb-2"
            />

            <a-card-meta :description="form.other_info"> </a-card-meta>
          </a-card>
        </description-list>

        <a-divider class="my-10" />
      </div>

      <div v-if="form.user">
        <description-list title="User Info">
          <detail-list-item term="Name">
            {{ form.user.name }}
          </detail-list-item>

          <detail-list-item term="Phone">
            {{ form.user.phone_number }}
          </detail-list-item>

          <detail-list-item term="Email">
            {{ form.user.email }}
          </detail-list-item>
        </description-list>

        <a-divider class="mb-10" />
      </div>

      <div class="title">Job</div>
      <s-table
        style="margin-bottom: 24px"
        row-key="id"
        :columns="goodsColumns"
        :data="loadGoodsData"
      >
      </s-table>
    </a-card>
  </page-view>
</template>

<script>
import { getOrder } from "@/api/order";
import { getUploads } from "@/api/upload";
import { PageView } from "@/layouts";
import { STable, DescriptionList } from "@/components";
const DetailListItem = DescriptionList.Item;

import {
  StatusOptions,
  CategoryOptions,
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
      CategoryOptions,
      MainInfoOptions,
      SubInfoOptions,
      form: {},
      images: [],
      markers: [],
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
      return this.$route.meta.title;
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
    getImages() {
      getUploads({ object_id: this.$route.params.id, content: 1 }).then(res => {
        this.images = res.result;
      });
    },
    getOrderData() {
      this.loading = true;
      getOrder(this.$route.params.id)
        .then(res => {
          const { result } = res;
          this.form = result;
          return this.getImages();
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
