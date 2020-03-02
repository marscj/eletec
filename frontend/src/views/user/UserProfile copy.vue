<template>
  <a-spin :spinning="loading">
    <validation-observer ref="observer">
      <validation-provider name="non_field_errors" v-slot="{ errors }">
        <span class="errorText">{{ errors[0] }}</span>
      </validation-provider>

      <a-form
        :form="form"
        :submit="submit"
        :label-col="{ span: 6 }"
        :wrapper-col="{ span: 12 }"
      >
        <a-form-item label="Username" required>
          <a-input v-model="form.username" disabled> </a-input>
        </a-form-item>

        <a-form-item label="Phone Number" required>
          <validation-provider
            vid="phone_number"
            name="phone number"
            v-slot="{ errors }"
          >
            <a-input v-model="form.phone_number"> </a-input>
            <span class="errorText">{{ errors[0] }}</span>
          </validation-provider>
        </a-form-item>

        <a-form-item label="Email">
          <validation-provider vid="email" v-slot="{ errors }">
            <a-input v-model="form.email"> </a-input>
            <span class="errorText">{{ errors[0] }}</span>
          </validation-provider>
        </a-form-item>

        <a-form-item label="First Name">
          <validation-provider
            vid="first_name"
            name="first name"
            v-slot="{ errors }"
          >
            <a-input v-model="form.first_name"> </a-input>
            <span class="errorText">{{ errors[0] }}</span>
          </validation-provider>
        </a-form-item>

        <a-form-item label="Last Name">
          <validation-provider
            vid="last_name"
            name="last name"
            v-slot="{ errors }"
          >
            <a-input v-model="form.last_name"> </a-input>
            <span class="errorText">{{ errors[0] }}</span>
          </validation-provider>
        </a-form-item>

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
          <a-select mode="multiple" v-model="form.groups_id">
            <a-select-option
              v-for="data in groupOption"
              :key="data.id"
              :value="data.id"
              >{{ data.name }}</a-select-option
            >
          </a-select>
        </a-form-item>

        <a-form-item label="Active">
          <a-checkbox v-model="form.is_active" />
        </a-form-item>

        <a-button
          type="primary"
          html-type="submit"
          @click="submit"
          :loading="updateing"
        >
          Submit
        </a-button>
      </a-form>
    </validation-observer>
  </a-spin>
</template>

<script>
import { getUser, updateUser } from "@/api/user";
import { getGroups } from "@/api/permission";
export default {
  data() {
    return {
      loading: false,
      form: {},
      groupOption: []
    };
  },
  mounted() {
    this.getGroupData();
  },
  methods: {
    getUserData() {
      getUser(this.$route.params.id).then(res => {
        const { result } = res;
        this.form = Object.assign(result, {
          groups_id: result.groups.map(f => f.id)
        });
      });
    },
    getGroupData() {
      this.loading = true;
      getGroups()
        .then(res => {
          const { result } = res;
          this.groupOption = result;
          return this.getUserData();
        })
        .finally(() => {
          this.loading = false;
        });
    },
    submit() {
      this.loading = true;
      updateUser(this.$route.params.id, {
        username: this.form.username,
        phone_number: this.form.phone_number,
        email: this.form.email,
        first_name: this.form.first_name,
        last_name: this.form.last_name,
        role: this.form.role,
        groups_id: this.form.groups_id
      })
        .catch(error => {
          if (error.response) {
            this.$refs.observer.setErrors(error.response.data.result);
          }
        })
        .finally(() => {
          this.loading = false;
        });
    }
  }
};
</script>
