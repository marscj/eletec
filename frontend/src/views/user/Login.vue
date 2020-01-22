<template>
  <div style="height:100%;">
    <a-row
      type="flex"
      justify="space-around"
      align="middle"
      style="height:100%;"
    >
      <div style="background-color:#eff2f7; width:50%; height: 350px;">
        <a-col :span="24" style="height: 100%;">
          <a-row
            type="flex"
            justify="space-around"
            align="middle"
            style="height: 100%;"
          >
            <a-col :span="12">
              <img
                src="@/assets/images/login.png"
                alt="login"
                style="display: block; margin: auto;"
              />
            </a-col>
            <a-col :span="12" style="height: 100%;">
              <div
                style="background-color: white; padding: 25px 20px; height: 100%;"
              >
                <div>
                  <h2 style="text-align: center;">Login</h2>
                </div>
                <div>
                  <login-phone style="padding: 20px 20px;" />
                  <!-- <a-tabs
                    :tabBarStyle="{
                      textAlign: 'center',
                      borderBottom: 'unset'
                    }"
                  >
                    <a-tab-pane tab="USERNAME" key="1">
                      <login-username />
                    </a-tab-pane>
                    <a-tab-pane tab="PHONE" key="2">
                      <login-phone />
                    </a-tab-pane>
                  </a-tabs> -->
                  <a-row type="flex" justify="center" align="middle">
                    <!-- <a-button type="primary" ghost>Register</a-button> -->
                    <a-button
                      type="primary"
                      ghost
                      size="large"
                      style="width: 100%; margin: 0px 20px;"
                      >Login</a-button
                    >
                  </a-row>
                </div>
              </div>
            </a-col>
          </a-row>
        </a-col>
      </div>
    </a-row>
  </div>
</template>

<script>
// import LoginUsername from "./LoginUsername.vue";
import LoginPhone from "./LoginPhone";

export default {
  components: {
    // LoginUsername
    LoginPhone
  }
};
</script>
