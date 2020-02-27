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
        path: "/admin/orders",
        name: "Orders",
        component: () => import("@/views/order/List.vue"),
        meta: {
          title: "Orders",
          icon: "file-text",
          permission: ["admin"]
        }
      },
      {
        path: "/admin/orders/:id",
        name: "Order",
        hidden: true,
        component: () => import("@/views/order/List.vue"),
        meta: {
          permission: ["admin"]
        }
      },
      {
        path: "/admin/jobs",
        name: "Jobs",
        component: () => import("@/views/job/List.vue"),
        meta: {
          title: "Jobs",
          icon: "calendar",
          permission: ["admin"]
        }
      },
      {
        path: "/admin/jobs/:id",
        name: "Job",
        hidden: true,
        component: () => import("@/views/order/List.vue"),
        meta: {
          permission: ["admin"]
        }
      },
      {
        path: "/admin/users/",
        name: "Users",
        component: () => import("@/views/user/List.vue"),
        hideChildrenInMenu: true,
        meta: {
          title: "Users",
          icon: "team",
          keepAlive: true,
          permission: ["admin"]
        }
      },
      {
        path: "/admin/users/:id",
        name: "User",
        hidden: true,
        component: () => import("@/views/user/Detail.vue"),
        meta: {
          title: "User",
          permission: ["admin"]
        }
      },
      {
        path: "/admin/groups",
        name: "Groups",
        component: () => import("@/views/group/List.vue"),
        meta: {
          title: "Groups",
          icon: "solution",
          permission: ["admin"]
        }
      },
      {
        path: "/admin/groups/:id",
        name: "Group",
        hidden: true,
        component: () => import("@/views/group/List.vue"),
        meta: {
          permission: ["admin"]
        }
      },
      {
        path: "/admin/settings",
        name: "Settings",
        component: PageView,
        redirect: "/admin/faqs/",
        meta: { title: "Settings", icon: "setting", permission: [] },
        children: [
          {
            path: "/admin/faqs",
            name: "FAQS",
            hideChildrenInMenu: true,
            component: () => import("@/views/setting/fqa/List.vue"),
            meta: {
              title: "FAQS",
              keepAlive: true,
              permission: ["admin"]
            }
          },
          {
            path: "/admin/faqs/:id",
            name: "FAQ",
            hidden: true,
            component: () => import("@/views/setting/faq/List.vue"),
            meta: {
              permission: ["admin"]
            }
          },
          {
            path: "/admin/app",
            name: "AppSetting",
            component: () => import("@/views/setting/app/List.vue"),
            meta: {
              title: "App",
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
        component: () => import("@/views/auth/Login")
      }
    ]
  },
  {
    path: "/404",
    component: () => import("@/views/error/404")
  }
];
