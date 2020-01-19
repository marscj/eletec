<template>
  <div class="flex items-center justify-center">
    <div class="sm:w-1/2 md:w-1/2 lg:w-3/4 xl:w-3/5 sm:m-0 m-4">
      <div class="shadow-xl">
        <div
          class="flex flex-row items-center"
          style="background-color:#eff2f7; height:400px;"
        >
          <div class="w-1/2 p-16">
            <img
              src="@/assets/images/login.png"
              alt="login"
              class="object-fill mx-auto"
            />
          </div>

          <div class="w-1/2 bg-white h-full py-10">
            <div class="px-8">
              <h4 class="text-xl text-center">Login</h4>
              <!-- <p>Welcome back, please login to your account.</p> -->
            </div>
            <div class="px-8">
              <a-tabs
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
              </a-tabs>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import LoginUsername from "./LoginUsername.vue";
import LoginPhone from "./LoginPhone";

export default {
  components: {
    LoginUsername,
    LoginPhone
  }
};
</script>
