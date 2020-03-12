<template>
  <validation-observer ref="observer">
    <a-form :form="form" @submit="handleSubmit">
      <a-row :gutter="16">
        <a-col :span="24">
          <a-form-item>
            <validation-provider
              vid="phone_number"
              name="phone number"
              v-slot="{ errors }"
            >
              <a-input placeholder="Phone Number" v-model="from.phone_number">
                <a-icon
                  slot="prefix"
                  type="mobile"
                  :style="{ color: 'rgba(0,0,0,.25)' }"
                />
                <a-select
                  slot="addonBefore"
                  defaultValue="+971"
                  style="width:80px"
                >
                  <a-select-option value="+971">+971</a-select-option>
                </a-select>
              </a-input>
              <span class="errorText">{{ errors[0] }}</span>
            </validation-provider>
          </a-form-item>
        </a-col>
      </a-row>

      <a-row>
        <a-col :span="24">
          <a-form-item>
            <validation-provider vid="otp" name="captcha" v-slot="{ errors }">
              <!-- <a-input placeholder="Verify Code" v-model="from.otp">
                <a-icon slot="prefix" type="mail" />
              </a-input> -->
              <a-row :gutter="4">
                <a-col :span="20">
                  <a-input v-model="from.otp" placeholder="Captcha" />
                </a-col>
                <a-col :span="4">
                  <a-button
                    class="w-full"
                    :disabled="state.smsSendBtn"
                    @click.stop.prevent="generate"
                    v-text="(!state.smsSendBtn && 'Send') || state.time + ' s'"
                  ></a-button>
                </a-col>
              </a-row>
              <span class="errorText">{{ errors[0] }}</span>
            </validation-provider>
          </a-form-item>
        </a-col>
        <!-- <a-col :span="8">
          <a-button
            style="display: block; width: 100%; height: 40px;"
            :disabled="state.smsSendBtn"
            @click.stop.prevent="generate"
            type="primary"
            ghost
            v-text="(!state.smsSendBtn && 'Send') || state.time + ' s'"
          ></a-button>
        </a-col> -->
      </a-row>
      <a-row type="flex" justify="center" align="middle">
        <a-button
          type="primary"
          ghost
          size="large"
          style="width: 100%;"
          @click="handleSubmit"
          :loading="state.loginBtn"
          :disabled="state.loginBtn"
          >Login</a-button
        >
      </a-row>
    </a-form>
    <validation-provider name="non_field_errors" v-slot="{ errors }">
      <span class="errorText">{{ errors[0] }}</span>
    </validation-provider>
  </validation-observer>
</template>

<script>
import { phoneGenerate } from "@/api/auth";
import { mapActions, mapGetters } from "vuex";
import { timeFix } from "@/utils/util";

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
  computed: {
    phone_number() {
      return "+971" + this.from.phone_number;
    }
  },
  methods: {
    ...mapActions(["Login"]),

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
        phone_number: this.phone_number
      })
        .then(res => {
          setTimeout(hide, 2500);
          this.$notification["success"]({
            message: "Prompt",
            description: "Sent successfully",
            duration: 3
          });
        })
        .catch(error => {
          setTimeout(hide, 1);
          clearInterval(interval);
          this.state.time = 60;
          this.state.smsSendBtn = false;

          if (error.response) {
            this.$refs.observer.setErrors(error.response.data.result);
          }
        })
        .finally(() => {});
    },
    handleSubmit() {
      const { Login } = this;

      this.state.loginBtn = true;

      Login({
        phone_number: this.phone_number,
        otp: this.from.otp
      })
        .then(res => {
          this.loginSuccess();
        })
        .catch(error => {
          if (error.response) {
            this.$refs.observer.setErrors(error.response.data.result);
          }
        })
        .finally(() => {
          this.state.loginBtn = false;
        });
    },
    loginSuccess() {
      this.$router.push({ path: "/" });
      setTimeout(() => {
        this.$notification.success({
          message: "Welcome",
          description: `${timeFix()}`
        });
      }, 1000);
      this.isLoginError = false;
    }
  }
};
</script>
