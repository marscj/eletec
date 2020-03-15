<template>
  <user-layout>
    <div style="height:100%;">
      <a-row
        type="flex"
        justify="space-around"
        align="middle"
        style="height:100%;"
      >
        <div style="background-color:#eff2f7; width:60%; height: 350px;">
          <a-col :span="24" style="height: 100%;">
            <a-row
              type="flex"
              justify="space-around"
              align="middle"
              style="height: 100%;"
            >
              <a-col :span="12">
                <img
                  src="@/assets/images/register.png"
                  alt="register"
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
                  <div class="items-center">
                    <h3>Verification succeeded</h3>
                  </div>
                </div>
              </a-col>
            </a-row>
          </a-col>
        </div>
      </a-row>
    </div>
  </user-layout>
</template>

<script>
import { UserLayout } from "@/layouts";
export default {
  components: {
    UserLayout
  }
};
</script>
