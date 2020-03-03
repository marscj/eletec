import Vue from "vue";
import Router from "vue-router";
import store from "@/store";
import { ACCESS_TOKEN } from "@/store/mutation-types";
import { constantRouterMap, asyncRouterMap, defaultRoutePath } from "./config";
import { setDocumentTitle, domTitle } from "@/utils/domUtil";

// hack router push callback
const originalPush = Router.prototype.push;
Router.prototype.push = function push(location, onResolve, onReject) {
  if (onResolve || onReject)
    return originalPush.call(this, location, onResolve, onReject);
  return originalPush.call(this, location).catch(err => err);
};

Vue.use(Router);

const router = new Router({
  mode: "history",
  base: process.env.BASE_URL,
  scrollBehavior: () => ({ x: 0, y: 0 }),
  routes: constantRouterMap
});

router.beforeEach((to, from, next) => {
  to.meta &&
    typeof to.meta.title !== "undefined" &&
    setDocumentTitle(`${to.meta.title} - ${domTitle}`);
  if (Vue.ls.get(ACCESS_TOKEN)) {
    if (to.path === "/user/login") {
      next({ path: defaultRoutePath });
    } else {
      if (store.getters.groups.length === 0 && !store.getters.has_info) {
        store
          .dispatch("GetInfo")
          .then(res => {
            store.dispatch("GenerateRoutes", res).then(() => {
              router.addRoutes(store.getters.addRouters);
              const redirect = decodeURIComponent(
                from.query.redirect || to.path
              );
              if (to.path === redirect) {
                next({ ...to, replace: true });
              } else {
                next({ path: redirect });
              }
            });
          })
          .catch(() => {
            store.dispatch("Logout").then(() => {
              next({ path: "/user/login", query: { redirect: to.fullPath } });
            });
          });
      } else {
        next();
      }
    }
  } else {
    var whiteList = filterWhilteList(constantRouterMap, to);
    if (whiteList && whiteList.length) {
      next();
    } else {
      next({ path: "/user/login", query: { redirect: to.fullPath } });
    }
  }
});

function filterWhilteList(list, to) {
  return list
    .reduce(
      (f, item) => (item.children ? f.concat(item.children) : f.concat(item)),
      []
    )
    .filter(f => {
      return f.path === to.path;
    });
}

function filterAsyncRouter(list, to) {
  return list.filter(route => {
    if (route.children && route.children.length) {
      route.children = filterAsyncRouter(route.children, to);
    }
  });
}

export default router;
