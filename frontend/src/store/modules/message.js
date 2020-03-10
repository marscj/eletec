import Vue from "vue";
import notification from "ant-design-vue/es/notification";

const message = {
  state: {
    message: []
  },
  mutations: {
    INIT_MESSAGE: (state, message) => {
      if (message) {
        state.message = [...message];
        Vue.ls.set("message", state.message);
      }
    },

    ADD_MESSAGE: (state, message) => {
      if (message) {
        state.message.unshift(message);
        Vue.ls.set("message", state.message);
      }
    },

    READ_MESSAGE: (state, message) => {
      if (message) {
        state.message = state.message.map(f => {
          if (f.messageID == message.messageID) {
            f.read = true;
          }
          return f;
        });
        Vue.ls.set("message", state.message);
      }
    },

    REMOVE_MESSAGE: (state, message) => {
      if (message) {
        state.message = state.message.filter(
          f => f.messageID != message.messageID
        );
        Vue.ls.set("message", state.message);
      }
    }
  },
  actions: {
    pushMessage({ commit }, message) {
      if (message) {
        commit("ADD_MESSAGE", message);
        notification.success({
          message: message.message
        });
      }
    },

    readMessage({ commit }, message) {
      if (message) {
        commit("READ_MESSAGE", message);
      }
    },

    removeMessage({ commit }, message) {
      if (message) {
        commit("REMOVE_MESSAGE", message);
      }
    }
  }
};

export default message;
