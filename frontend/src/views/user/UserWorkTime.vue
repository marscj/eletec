<template>
  <div>
    <validation-observer ref="observer">
      <validation-provider name="non_field_errors" v-slot="{ errors }">
        <span class="errorText">{{ errors[0] }}</span>
      </validation-provider>

      <a-form
        :form="form"
        :submit="submit"
        :label-col="{ span: 5 }"
        :wrapper-col="{ span: 12 }"
      >
        <a-form-item label="Phone Number" required>
          <validation-provider
            vid="phone_number"
            name="phone number"
            v-slot="{ errors }"
          >
            <a-input v-model="form.phone_number" disabled> </a-input>
            <span class="errorText">{{ errors[0] }}</span>
          </validation-provider>
        </a-form-item>

        <a-button type="primary" html-type="submit" @click="submit">
          Submit
        </a-button>
      </a-form>
    </validation-observer>
  </div>
</template>

<script>
import { getAddress } from "@/api/user";
export default {
  data() {
    return {
      form: {}
    };
  },
  mounted() {
    this.getData();
  },
  methods: {
    getData() {
      getAddress({
        user_id: this.$store.getters.user.id
      }).then(res => {
        const { result } = res;
        this.form = result;
      });
    },
    submit() {}
  }
};
</script>
