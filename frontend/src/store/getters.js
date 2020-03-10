const getters = {
  device: state => state.app.device,
  theme: state => state.app.theme,
  color: state => state.app.color,

  user: state => state.user,
  id: state => state.user.id,
  token: state => state.user.token,
  avatar: state => state.user.photo,
  nickname: state => state.user.displayName,
  groups: state => state.user.groups,
  has_info: state => state.user.has_info,

  message: state => state.message.message,

  addRouters: state => state.permission.addRouters,
  multiTab: state => state.app.multiTab,
  lang: state => state.i18n.lang
};

export default getters;
