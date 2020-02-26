import Vue from "vue";
import { phoneValidate, getInfo, logout } from "@/api/auth";
import { ACCESS_TOKEN } from "@/store/mutation-types";

const user = {
  state: {
    id: "",
    token: "",
    displayName: "",
    photoURL: "",
    groups: [],
    is_superuser: false,
    has_info: false
  },

  mutations: {
    SET_ID: (state, id) => {
      state.id = id;
    },

    SET_TOKEN: (state, token) => {
      state.token = token;
    },

    SET_NAME: (state, name) => {
      state.displayName = name;
    },

    SET_PHOTO: (state, url) => {
      state.photoURL = url;
    },

    SET_GROUPS: (state, groups) => {
      state.groups = groups;
    },

    SET_SUPERUSER: (state, is_superuser) => {
      state.is_superuser = is_superuser;
    },

    SET_HAS_INFO: (state, info) => {
      state.has_info = info;
    }
  },

  actions: {
    // 登录
    Login({ commit }, userInfo) {
      return new Promise((resolve, reject) => {
        phoneValidate(userInfo)
          .then(response => {
            const result = response.result;
            Vue.ls.set(ACCESS_TOKEN, result.token);
            commit("SET_TOKEN", result.token);
            commit("SET_HAS_INFO", false);
            resolve();
          })
          .catch(error => {
            reject(error);
          });
      });
    },

    // 获取用户信息
    GetInfo({ commit }) {
      return new Promise((resolve, reject) => {
        getInfo()
          .then(res => {
            const { result } = res;
            commit("SET_ID", result.id);
            commit("SET_GROUPS", result.groups);
            commit("SET_NAME", result.phone_number);
            commit("SET_PHOTO", result.photoURL);
            commit("SET_SUPERUSER", result.is_superuser);
            commit("SET_HAS_INFO", true);
            resolve(res);
          })
          .catch(error => {
            reject(error);
          });
      });
    },

    // 登出
    Logout({ commit }) {
      return new Promise(resolve => {
        logout()
          .then(() => {
            resolve();
          })
          .catch(() => {
            resolve();
          })
          .finally(() => {
            commit("SET_TOKEN", "");
            commit("SET_GROUPS", []);
            commit("SET_NAME", "");
            commit("SET_PHOTO", "");
            commit("SET_SUPERUSER", false);
            commit("SET_HAS_INFO", false);
            Vue.ls.remove(ACCESS_TOKEN);
          });
      });
    }
  }
};

export default user;
