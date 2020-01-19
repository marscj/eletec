<template>
  <div>
    <a-form>
      <a-form-item>
        <a-input size="large" type="text" placeholder="Phone Number">
          <a-icon
            slot="prefix"
            type="mobile"
            :style="{ color: 'rgba(0,0,0,.25)' }"
          />
        </a-input>
      </a-form-item>
      <a-row :gutter="16">
        <a-col class="gutter-row" :span="16">
          <a-form-item>
            <a-input size="large" type="text" placeholder="Verify Code">
              <a-icon
                slot="prefix"
                type="mail"
                :style="{ color: 'rgba(0,0,0,.25)' }"
              />
            </a-input>
          </a-form-item>
        </a-col>
        <a-col class="gutter-row" :span="8">
          <a-button
            style="display: block; width: 100%; height: 40px;"
            :disabled="state.smsSendBtn"
            @click.stop.prevent="getCaptcha"
            type="primary"
            ghost
            v-text="(!state.smsSendBtn && 'Send') || state.time + ' s'"
          ></a-button>
        </a-col>
      </a-row>
    </a-form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      state: {
        time: 60,
        loginBtn: false,
        loginType: 0,
        smsSendBtn: false
      }
    };
  },
  methods: {
    getCaptcha(e) {
      e.preventDefault();

      this.state.smsSendBtn = true;

      const interval = window.setInterval(() => {
        if (this.state.time-- <= 0) {
          this.state.time = 60;
          this.state.smsSendBtn = false;
          window.clearInterval(interval);
        }
      }, 1000);
    }
  }
};
</script>
