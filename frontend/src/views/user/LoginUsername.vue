<template>
  <div>
    <a-form>
      <a-form-item>
        <a-input size="large" type="text" placeholder="Username">
          <a-icon
            slot="prefix"
            type="user"
            :style="{ color: 'rgba(0,0,0,.25)' }"
          />
        </a-input>
      </a-form-item>

      <a-form-item>
        <a-input
          size="large"
          type="password"
          autocomplete="false"
          placeholder="Password"
        >
          <a-icon
            slot="prefix"
            type="lock"
            :style="{ color: 'rgba(0,0,0,.25)' }"
          />
        </a-input>
      </a-form-item>
    </a-form>

    <a-row type="flex" justify="space-between" align="middle">
      <a-button type="primary" ghost>Register</a-button>
      <a-button type="primary" ghost>Login</a-button>
    </a-row>
  </div>
</template>

<script>
export default {};
</script>
