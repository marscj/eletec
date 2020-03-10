import Vue from "vue";
import Vuex from "vuex";

import app from "./modules/app";
import user from "./modules/user";
import permission from "./modules/permission";
import message from "./modules/message";
import getters from "./getters";

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    app,
    user,
    permission,
    message
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
    },
    SOCKET_ONCLOSE(state, event) {
      state.socket.isConnected = false;
    },
    SOCKET_ONERROR(state, event) {
      console.error(state, event);
    },
    SOCKET_ONMESSAGE(state, message) {
      state.socket.message = message;
      this.dispatch("pushMessage", message);
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
      Vue.prototype.$connect();
    },
    closeMessage() {
      Vue.prototype.$disconnect();
    }
  },
  getters
});
