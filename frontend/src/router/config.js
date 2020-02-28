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
          permission: ["order"]
        }
      },
      {
        path: "/admin/orders/:id",
        name: "Order",
        hidden: true,
        component: () => import("@/views/order/List.vue"),
        meta: {
          permission: ["order"]
        }
      },
      {
        path: "/admin/jobs",
        name: "Jobs",
        component: () => import("@/views/job/List.vue"),
        meta: {
          title: "Jobs",
          icon: "calendar",
          permission: ["job"]
        }
      },
      {
        path: "/admin/jobs/:id",
        name: "Job",
        hidden: true,
        component: () => import("@/views/order/List.vue"),
        meta: {
          permission: ["job"]
        }
      },
      {
        path: "/admin/users/",
        name: "Users",
        component: () => import("@/views/user/List.vue"),
        meta: {
          title: "Users",
          icon: "team",
          keepAlive: true,
          permission: ["user"]
        }
      },
      {
        path: "/admin/users/:id",
        name: "User",
        hidden: true,
        component: () => import("@/views/user/Index"),
        redirect: "/admin/users/:id/profile",
        hideChildrenInMenu: true,
        meta: {
          title: "User",
          permission: ["user"]
        },
        children: [
          {
            path: "/admin/users/:id/profile",
            name: "UserProfile",
            component: () => import("@/views/user/UserProfile.vue"),
            meta: {
              title: "Profile",
              hideHeader: true,
              permission: ["user"]
            }
          },
          {
            path: "/admin/users/:id/address",
            name: "UserAddress",
            component: () => import("@/views/user/UserAddress.vue"),
            meta: {
              title: "Address",
              hideHeader: true,
              permission: ["user"]
            }
          },
          {
            path: "/admin/users/:id/skill",
            name: "UserSkill",
            component: () => import("@/views/user/UserSkill.vue"),
            meta: {
              title: "Skill",
              hideHeader: true,
              permission: ["user"]
            }
          },
          {
            path: "/admin/users/:id/worktime",
            name: "UserWorkTime",
            component: () => import("@/views/user/UserWorkTime.vue"),
            meta: {
              title: "WorkTime",
              hideHeader: true,
              permission: ["user"]
            }
          }
        ]
      },
      {
        path: "/admin/groups",
        name: "Groups",
        component: () => import("@/views/group/List.vue"),
        meta: {
          title: "Groups",
          icon: "solution",
          permission: ["group"]
        }
      },
      {
        path: "/admin/groups/:id",
        name: "Group",
        hidden: true,
        component: () => import("@/views/group/List.vue"),
        meta: {
          permission: ["group"]
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
            component: () => import("@/views/setting/faq/List.vue"),
            meta: {
              title: "FAQS",
              keepAlive: true,
              permission: ["faq"]
            }
          },
          {
            path: "/admin/faqs/:id",
            name: "FAQ",
            hidden: true,
            component: () => import("@/views/setting/faq/List.vue"),
            meta: {
              permission: ["faq"]
            }
          },
          {
            path: "/admin/app",
            name: "AppSetting",
            component: () => import("@/views/setting/app/List.vue"),
            meta: {
              title: "App",
              permission: []
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
