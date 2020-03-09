import Vue from "vue";
import Vuex from "vuex";

import app from "./modules/app";
import user from "./modules/user";

// default router permission control
import permission from "./modules/permission";

// dynamic router permission control (Experimental)
// import permission from './modules/async-router'
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
      console.info("SOCKET_ONCLOSE");
    },
    SOCKET_ONERROR(state, event) {
      console.error(state, event);
      console.info("SOCKET_ONERROR");
    },
    // default handler called for all methods
    SOCKET_ONMESSAGE(state, message) {
      state.socket.message = message;
      console.info(message, "=----");
    },
    // mutations for reconnect methods
    SOCKET_RECONNECT(state, count) {
      console.info(state, count);
    },
    SOCKET_RECONNECT_ERROR(state) {
      state.socket.reconnectError = true;
      console.info("SOCKET_RECONNECT_ERROR");
    }
  },
  actions: {},
  getters
});
