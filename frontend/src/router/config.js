import {
  UserLayout,
  BasicLayout,
  RouteView,
  BlankLayout,
  PageView
} from "@/layouts";

export const defaultRoutePath = "/admin/order";

export const asyncRouterMap = [
  {
    path: "/admin",
    name: "admin",
    component: BasicLayout,
    meta: { title: "Admin" },
    redirect: defaultRoutePath
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
    path: "/",
    component: BlankLayout,
    redirect: "/home",
    hidden: true,
    children: [
      {
        path: "/home",
        name: "home",
        component: () => import("@/views/Home")
      }
    ]
  },
  {
    path: "/user",
    component: UserLayout,
    redirect: "/user/login",
    hidden: true,
    children: [
      {
        path: "/user/login",
        name: "login",
        component: () => import("@/views/user/Login")
      }
    ]
  },
  {
    path: "/404",
    component: () => import("@/views/error/404")
  }
];
