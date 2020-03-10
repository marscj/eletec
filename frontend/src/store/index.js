import Vue from "vue";
import Vuex from "vuex";

import app from "./modules/app";
import user from "./modules/user";
import permission from "./modules/permission";
import getters from "./getters";

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    app,
    user,
    permission
  },
  state: {
    socket: {
      isConnected: false,
      message: "",
      reconnectError: false
    }
  },
  mutations: {
    SOCKET_ONOPEN(state, event) {
      Vue.prototype.$socket = event.currentTarget;
      state.socket.isConnected = true;
      console.info("SOCKET_ONOPEN");
    },
    SOCKET_ONCLOSE(state, event) {
      state.socket.isConnected = false;
      console.info("SOCKET_ONOPEN");
    },
    SOCKET_ONERROR(state, event) {
      console.error(state, event);
    },
    SOCKET_ONMESSAGE(state, message) {
      state.socket.message = message;
    },
    SOCKET_RECONNECT(state, count) {
      console.info(state, count);
    },
    SOCKET_RECONNECT_ERROR(state) {
      state.socket.reconnectError = true;
    }
  },
  actions: {
    openMessage() {
      console.log("openMessage");
      Vue.prototype.$connect();
    },
    closeMessage() {
      console.log("closeMessage");
      Vue.prototype.$disconnect();
    }
  },
  getters
});
