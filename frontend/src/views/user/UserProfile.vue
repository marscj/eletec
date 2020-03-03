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
        <a-form-item label="Photo" required>
          <a-upload
            name="Photo"
            :multiple="false"
            :beforeUpload="beforeUpload"
            :customRequest="upload"
            :showUploadList="false"
            class="avatar-uploader"
            listType="picture-card"
          >
            <img
              v-if="form && form.photo && form.photo.thumbnail"
              alt="images"
              :src="form.photo.thumbnail"
            />

            <div v-else>
              <a-icon :type="uploading ? 'loading' : 'plus'" />
              <div class="ant-upload-text">Upload</div>
            </div>
          </a-upload>
        </a-form-item>

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

        <!-- <a-form-item label="Group">
          <a-select mode="multiple" v-model="form.groups_id">
            <a-select-option
              v-for="data in groupOption"
              :key="data.id"
              :value="data.id"
              >{{ data.name }}</a-select-option
            >
          </a-select>
        </a-form-item> -->

        <a-form-item label="Active" help="Whether the account is available">
          <a-checkbox v-model="form.is_active" />
        </a-form-item>

        <a-form-item
          label="Admin"
          help="Used to log in to the back-end website"
        >
          <a-checkbox v-model="form.is_superuser" />
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
// import { getGroups } from "@/api/permission";
export default {
  data() {
    return {
      loading: false,
      uploading: false,
      form: {}
      // groupOption: []
    };
  },
  mounted() {
    this.getUserData();
  },
  methods: {
    getUserData() {
      getUser(this.$route.params.id).then(res => {
        const { result } = res;
        // this.form = Object.assign(result, {
        //   groups_id: result.groups.map(f => f.id)
        // });
        this.form = result;
      });
    },
    // getGroupData() {
    //   this.loading = true;
    //   getGroups()
    //     .then(res => {
    //       const { result } = res;
    //       this.groupOption = result;
    //       return this.getUserData();
    //     })
    //     .finally(() => {
    //       this.loading = false;
    //     });
    // },
    beforeUpload(file) {
      const isIMG = file.type === "image/jpeg" || file.type === "image/png";
      if (!isIMG) {
        this.$message.error("You can only upload JPG or PNG file!");
      }
      const isLt2M = file.size / 1024 / 1024 < 2;
      if (!isLt2M) {
        this.$message.error("Image must smaller than 2MB!");
      }
      return isIMG && isLt2M;
    },
    upload(request) {
      const formData = new FormData();
      formData.append("photo", request.file);
      formData.append("username", this.form.username);
      formData.append("phone_number", this.form.phone_number);
      formData.append("email", this.form.email);
      formData.append("first_name", this.form.first_name);
      formData.append("last_name", this.form.last_name);
      formData.append("role", this.form.role);
      formData.append("is_superuser", this.form.is_superuser);
      formData.append("is_active", this.form.is_active);
      this.uploading = true;
      updateUser(this.$route.params.id, formData)
        .then(res => {
          this.getUserData();
        })
        .finally(() => {
          this.uploading = false;
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
        is_active: this.form.is_active,
        is_superuser: this.form.is_superuser
        // groups_id: this.form.groups_id
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

<style>
.avatar-uploader > .ant-upload {
  width: 128px;
  height: 128px;
}
.ant-upload-select-picture-card i {
  font-size: 32px;
  color: #999;
}

.ant-upload-select-picture-card .ant-upload-text {
  margin-top: 8px;
  color: #666;
}
</style>
