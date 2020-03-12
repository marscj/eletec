<template>
  <div>
    <div align="right" class="table-operator">
      <a-button type="primary" icon="upload" @click="openModal()">
        New
      </a-button>
    </div>
    <a-list
      ref="list"
      size="default"
      rowKey="id"
      :grid="{ gutter: 24, lg: 1, md: 1, sm: 1, xs: 1 }"
      :dataSource="listData"
      :loading="loading"
    >
      <a-list-item slot="renderItem" slot-scope="item">
        <template>
          <a-card :hoverable="true">
            <img :src="item.image.full_size" slot="cover" alt="images" />

            <a-card-meta :title="item.tag"></a-card-meta>

            <template class="ant-card-actions" slot="actions">
              <a-popconfirm
                title="Are you sure delete this data?"
                @confirm="deleteData(item)"
                okText="Yes"
                cancelText="No"
              >
                <a href="#">Delete</a>
              </a-popconfirm>
            </template>
          </a-card>
        </template>
      </a-list-item>
    </a-list>
    <a-modal
      v-model="modal"
      :title="this.form.id === undefined ? 'Create' : 'Edit'"
      @ok="upload"
    >
      <validation-observer ref="observer">
        <validation-provider name="non_field_errors" v-slot="{ errors }">
          <span class="errorText">{{ errors[0] }}</span>
        </validation-provider>

        <a-form
          :form="form"
          :submit="upload"
          :label-col="{ span: 4 }"
          :wrapper-col="{ span: 16 }"
        >
          <a-form-item label="Image">
            <validation-provider vid="image" v-slot="{ errors }">
              <a-upload
                :multiple="false"
                :fileList="fileList"
                :beforeUpload="beforeUpload"
                :disabled="fileList.length > 0"
                :remove="handleRemove"
              >
                <a-button v-if="fileList.length == 0">
                  <a-icon type="upload" /> Select File
                </a-button>
              </a-upload>
              <span class="errorText">{{ errors[0] }}</span>
            </validation-provider>
          </a-form-item>
          <a-form-item label="Tag">
            <validation-provider vid="tag" v-slot="{ errors }">
              <a-select v-model="form.tag" v-if="options">
                <a-select-option
                  v-for="data in options"
                  :key="data.value"
                  :value="data.value"
                  >{{ data.label }}</a-select-option
                >
              </a-select>
              <a-textarea v-model="form.tag" />
              <span class="errorText">{{ errors[0] }}</span>
            </validation-provider>
          </a-form-item>
        </a-form>
      </validation-observer>
    </a-modal>
  </div>
</template>

<script>
import { getImages, uploadImage, deleteImage } from "@/api/image";
export default {
  name: "ImageList",
  props: {
    content_type: {
      type: String
    },
    options: {
      type: Array
    },
    object_id: {
      type: Number
    }
  },
  data() {
    return {
      loading: false,
      uploading: false,
      listData: undefined,
      modal: false,
      form: {},
      fileList: []
    };
  },
  mounted() {
    this.getListData();
  },
  methods: {
    getListData() {
      this.loading = true;
      getImages({
        object_id: this.object_id,
        content_type: this.content_type
      })
        .then(res => {
          this.listData = res.result;
        })
        .finally(() => {
          this.loading = false;
        });
    },
    deleteData(val) {
      this.loading = true;
      deleteImage(val.id)
        .then(res => {
          this.getListData();
        })
        .finally(() => {
          this.loading = false;
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
    upload() {
      const formData = new FormData();
      formData.append("image", this.fileList[0]);
      formData.append("tag", this.form.tag);
      formData.append("content_type", this.content_type);
      formData.append("object_id", this.object_id);

      this.uploading = true;
      uploadImage(formData)
        .then(res => {
          this.getListData();
          this.modal = false;
        })
        .finally(() => {
          this.uploading = false;
        })
        .catch(error => {
          if (error.response) {
            this.$refs.observer.setErrors(error.response.data.result);
          }
        });
    },
    openModal(val) {
      this.modal = true;
      this.fileList = [];
      this.form = {};
    }
  }
};
</script>
