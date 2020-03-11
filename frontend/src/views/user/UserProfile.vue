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
            :fileList="fileList"
            :beforeUpload="beforeUpload"
            :disabled="fileList.length > 0"
            :remove="handleRemove"
            listType="text"
          >
            <img
              v-if="form && form.photo && form.photo.image.thumbnail"
              alt="images"
              :src="form.photo.image.thumbnail"
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
            <a-select-option
              v-for="data in RoleOptions"
              :key="data.value"
              :value="data.value"
              >{{ data.label }}</a-select-option
            >
          </a-select>
        </a-form-item>

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
import { uploadImage, updateImage } from "@/api/image";
import { RoleOptions } from "./const";

export default {
  data() {
    return {
      RoleOptions,
      loading: false,
      uploading: false,
      form: {},
      fileList: []
    };
  },
  mounted() {
    this.getUserData();
  },
  computed: {
    photo() {
      return this.fileList[0];
    }
  },
  methods: {
    getUserData() {
      getUser(this.$route.params.id).then(res => {
        const { result } = res;
        this.form = result;
      });
    },
    beforeUpload(file) {
      const isIMG = file.type === "image/jpeg" || file.type === "image/png";
      if (!isIMG) {
        this.$message.error("You can only upload JPG or PNG file!");
      }

      const isLt2M = file.size / 1024 / 1024 < 2;
      if (!isLt2M) {
        this.$message.error("Image must smaller than 2MB!");
      }

      if (isIMG && isLt2M) {
        this.fileList = [...this.fileList, file];
      }
      return false;
    },
    handleRemove(file) {
      const index = this.fileList.indexOf(file);
      const newFileList = this.fileList.slice();
      newFileList.splice(index, 1);
      this.fileList = newFileList;
    },
    submit() {
      this.loading = true;
      const formData = new FormData();

      if (this.photo) {
        formData.append("photo", this.photo);
        console.log(this.photo);
      }

      formData.append("username", this.form.username);
      formData.append("phone_number", this.form.phone_number);
      formData.append("email", this.form.email);
      formData.append("first_name", this.form.first_name);
      formData.append("last_name", this.form.last_name);
      formData.append("role", this.form.role);
      formData.append("is_active", this.form.is_active);
      formData.append("is_superuser", this.form.is_superuser);

      updateUser(this.$route.params.id, formData)
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
