import {
  UserLayout,
  BasicLayout,
  RouteView,
  BlankLayout,
  PageView
} from "@/layouts";

export const defaultRoutePath = "/admin/orders";

export const asyncRouterMap = [
  {
    path: "/admin",
    name: "admin",
    component: BasicLayout,
    meta: { title: "Admin" },
    redirect: defaultRoutePath,
    children: [
      {
        path: "/admin/orders/:pageNo([1-9]\\d*)?",
        name: "Orders",
        component: () => import("@/views/order/List.vue"),
        meta: {
          title: "Orders",
          icon: "file-text",
          keepAlive: true,
          permission: ["admin"]
        }
      },
      {
        path: "/admin/order/:id",
        name: "Order",
        hidden: true,
        component: () => import("@/views/order/List.vue"),
        meta: {
          keepAlive: true,
          permission: ["admin"]
        }
      },
      {
        path: "/admin/jobs/:pageNo([1-9]\\d*)?",
        name: "Jobs",
        component: () => import("@/views/order/List.vue"),
        meta: {
          title: "Jobs",
          icon: "calendar",
          keepAlive: true,
          permission: ["admin"]
        }
      },
      {
        path: "/admin/job/:id",
        name: "Job",
        hidden: true,
        component: () => import("@/views/order/List.vue"),
        meta: {
          keepAlive: true,
          permission: ["admin"]
        }
      },
      {
        path: "/admin/users/:pageNo([1-9]\\d*)?",
        name: "Users",
        component: () => import("@/views/order/List.vue"),
        meta: {
          title: "Users",
          icon: "team",
          keepAlive: true,
          permission: ["admin"]
        }
      },
      {
        path: "/admin/user/:id",
        name: "User",
        hidden: true,
        component: () => import("@/views/order/List.vue"),
        meta: {
          keepAlive: true,
          permission: ["admin"]
        }
      },
      {
        path: "/admin/permissions/:pageNo([1-9]\\d*)?",
        name: "Permissions",
        component: () => import("@/views/order/List.vue"),
        meta: {
          title: "Permissions",
          icon: "solution",
          keepAlive: true,
          permission: ["admin"]
        }
      },
      {
        path: "/admin/permission/:id",
        name: "Permission",
        hidden: true,
        component: () => import("@/views/order/List.vue"),
        meta: {
          keepAlive: true,
          permission: ["admin"]
        }
      },
      {
        path: "/admin/settings",
        name: "Settings",
        component: RouteView,
        redirect: "/admin/FAQS/",
        meta: { title: "Settings", icon: "setting", permission: [] },
        children: [
          {
            path: "/admin/FAQS/:pageNo([1-9]\\d*)?",
            name: "FAQS",
            component: () => import("@/views/order/List.vue"),
            meta: {
              title: "FAQS",
              keepAlive: true,
              permission: ["admin"]
            }
          },
          {
            path: "/admin/FAQ/:id",
            name: "FAQ",
            hidden: true,
            component: () => import("@/views/order/List.vue"),
            meta: {
              keepAlive: true,
              permission: ["admin"]
            }
          },
          {
            path: "/admin/app/:pageNo([1-9]\\d*)?",
            name: "AppSetting",
            component: () => import("@/views/order/List.vue"),
            meta: {
              title: "App",
              keepAlive: true,
              permission: ["admin"]
            }
          }
        ]
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
