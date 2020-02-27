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
        <validation-provider
          vid="phone_number"
          name="phone number"
          v-slot="{ errors }"
        >
          <a-form-item label="Phone Number" required>
            <a-input v-model="form.phone_number" disabled> </a-input>
          </a-form-item>
          <span class="errorText">{{ errors[0] }}</span>
        </validation-provider>

        <validation-provider
          vid="first_name"
          name="first name"
          v-slot="{ errors }"
        >
          <a-form-item label="First Name">
            <a-input v-model="form.first_name"> </a-input>
          </a-form-item>
          <span class="errorText">{{ errors[0] }}</span>
        </validation-provider>

        <validation-provider
          vid="last_name"
          name="last name"
          v-slot="{ errors }"
        >
          <a-form-item label="Last Name">
            <a-input v-model="form.last_name"> </a-input>
          </a-form-item>
          <span class="errorText">{{ errors[0] }}</span>
        </validation-provider>

        <validation-provider vid="email" v-slot="{ errors }">
          <a-form-item label="Email">
            <a-input v-model="form.email"> </a-input>
          </a-form-item>
          <span class="errorText">{{ errors[0] }}</span>
        </validation-provider>

        <a-form-item label="Role">
          <a-select v-model="form.role">
            <a-select-option key="1" value="Customer">Customer</a-select-option>
            <a-select-option key="2" value="Staff">Staff</a-select-option>
            <a-select-option key="3" value="Freelancer"
              >Freelancer</a-select-option
            >
          </a-select>
        </a-form-item>

        <a-form-item label="Group">
          <a-select mode="multiple">
            <a-select-option key="1" value="1">1</a-select-option>
          </a-select>
        </a-form-item>

        <a-form-item label="Active">
          <a-checkbox v-model="form.is_active" />
        </a-form-item>

        <a-button type="primary" html-type="submit" @click="submit">
          Submit
        </a-button>
      </a-form>
    </validation-observer>
  </div>
</template>

<script>
import { getUser, updateUser } from "@/api/user";
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
      getUser(this.$route.params.id).then(res => {
        const { result } = res;
        this.form = result;
      });
    },
    submit() {
      console.log("submit");
    }
  }
};
</script>
