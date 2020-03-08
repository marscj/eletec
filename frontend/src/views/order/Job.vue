<template>
  <div>
    <s-table
      style="margin-bottom: 24px"
      row-key="id"
      :columns="goodsColumns"
      :data="loadGoodsData"
    >
    </s-table>
  </div>
</template>

<script>
import { STable } from "@/components";

export default {
  components: {
    STable
  },
  data() {
    return {
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
  }
};
</script>
