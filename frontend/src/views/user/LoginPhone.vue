<template>
  <div>
    <a-form>
      <a-row :gutter="16">
        <a-col :span="6">
          <a-input size="large" type="text" placeholder="+971" disabled />
        </a-col>
        <a-col :span="18">
          <a-form-item>
            <a-input
              size="large"
              type="text"
              placeholder="Phone Number"
              v-model="from.phone_number"
            >
              <a-icon
                slot="prefix"
                type="mobile"
                :style="{ color: 'rgba(0,0,0,.25)' }"
              />
            </a-input>
          </a-form-item>
        </a-col>
      </a-row>

      <a-row :gutter="16">
        <a-col :span="16">
          <a-form-item>
            <a-input
              size="large"
              type="text"
              placeholder="Verify Code"
              v-model="from.otp"
            >
              <a-icon
                slot="prefix"
                type="mail"
                :style="{ color: 'rgba(0,0,0,.25)' }"
              />
            </a-input>
          </a-form-item>
        </a-col>
        <a-col :span="8">
          <a-button
            style="display: block; width: 100%; height: 40px;"
            :disabled="state.smsSendBtn"
            @click.stop.prevent="generate"
            type="primary"
            ghost
            v-text="(!state.smsSendBtn && 'Send') || state.time + ' s'"
          ></a-button>
        </a-col>
      </a-row>
      <a-row type="flex" justify="center" align="middle">
        <a-button type="primary" ghost size="large" style="width: 100%;"
          >Login</a-button
        >
      </a-row>
    </a-form>
  </div>
</template>

<script>
import { phoneGenerate } from "@/api/auth";

export default {
  data() {
    return {
      state: {
        time: 60,
        loginBtn: false,
        loginType: 0,
        smsSendBtn: false
      },
      from: {}
    };
  },
  methods: {
    generate(e) {
      e.preventDefault();

      this.state.smsSendBtn = true;

      const interval = window.setInterval(() => {
        if (this.state.time-- <= 0) {
          this.state.time = 60;
          this.state.smsSendBtn = false;
          window.clearInterval(interval);
        }
      }, 1000);

      const hide = this.$message.loading("Sending", 0);
      phoneGenerate({
        phone_number: "+971" + this.from.phone_number
      }).then(res => {});
    }
  }
};
</script>
