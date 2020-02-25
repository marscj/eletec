function plugin (Vue) {
  if (plugin.installed) {
    return
  }

  !Vue.prototype.$auth && Object.defineProperties(Vue.prototype, {
    $auth: {
      get () {
        const _this = this
        return (permissions) => {
          const [model, action] = permissions.split('.')
          const groups = _this.$store.getters.groups
          const user = _this.$store.getters.user

          if (user.is_superuser) {
            return true
          }

          let list = groups.reduce((f1, f2) => f1.concat(f2.permissions), []).find(f => {
            return f.content_type.model === model && f.codename === action;
          });

          return Boolean(list)
        }
      }
    }
  })
}

export default plugin
