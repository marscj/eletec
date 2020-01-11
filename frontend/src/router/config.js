import {
  UserLayout,
  BasicLayout,
  RouteView,
  BlankLayout,
  PageView
} from "@/layouts";

export const asyncRouterMap = [
  {
    path: "/admin",
    name: "index",
    component: BasicLayout,
    meta: { title: "Admin" },
    redirect: "/admin/order"
  },
  {
    path: "/admin/order",
    name: "Order",
    component: PageView,
    meta: { title: "Order" },
    redirect: "order-list",
    children: [
      {
        path: "/admin/order/list",
        name: "OrderList",
        component: () => import("@/views/order/List.vue"),
        meta: { title: "OrderList", keepAlive: true, permission: [] }
      }
    ]
  }
];
