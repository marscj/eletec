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
    name: "admin",
    component: BasicLayout,
    meta: { title: "Admin" },
    redirect: "/admin/order"
  },
  {
    path: "/admin/order",
    name: "Order",
    component: PageView,
    meta: { title: "Order" },
    redirect: "/admin/order/list",
    children: [
      {
        path: "/admin/order/list",
        name: "OrderList",
        component: () => import("@/views/order/List.vue"),
        meta: { title: "OrderList", keepAlive: true, permission: [] }
      }
    ]
  },
  {
    path: "*",
    redirect: "/404",
    hidden: true
  }
];

export const constantRouterMap = [
  {
    path: "/404",
    component: () => import("@/views/error/404")
  }
];
