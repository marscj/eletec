<template>
  <page-view :title="title">
    <a-card :bordered="false">
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
      </description-list>
      <a-divider style="margin-bottom: 32px" />

      <description-list title="Other Info" v-if="form.other_info || form.image">
        <a-card>
          <img
            alt="example"
            src="http://127.0.0.1:8000/media/__sized__/resource/1/5-crop-c0-5__0-5-1280x720-70.jpg"
            slot="cover"
          />
          <a-card-meta :description="form.other_info">
            <!-- <template slot="description">www.instagram.com</template> -->
          </a-card-meta>
        </a-card>
        <a-divider style="margin-bottom: 32px" />
      </description-list>

      <description-list title="用户信息">
        <detail-list-item term="用户姓名">付小小</detail-list-item>
        <detail-list-item term="联系电话">18100000000</detail-list-item>
        <detail-list-item term="常用快递">菜鸟仓储</detail-list-item>
        <detail-list-item term="取货地址"
          >浙江省杭州市西湖区万塘路18号</detail-list-item
        >
        <detail-list-item term="备注"> 无</detail-list-item>
      </description-list>
      <a-divider style="margin-bottom: 32px" />

      <div class="title">退货商品</div>
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
  mounted() {
    this.getUserData();
  },
  methods: {
    moment,
    getUserData() {
      getOrder(this.$route.params.id).then(res => {
        const { result } = res;
        this.form = result;

        console.log(this.form);
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
</style>
