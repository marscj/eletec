<template>
  <page-view class="bg-white">
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
            <img
              :src="item.tag == 0 ? item.image.advertising : item.image.banner"
              slot="cover"
              alt="images"
            />

            <a-card-meta
              :title="item.tag == 0 ? 'Advertising' : 'Banner ' + item.sorter"
            ></a-card-meta>

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
          <a-form-item
            label="Image"
            :help="
              form.tag == 0
                ? 'picture size is better 1280x720'
                : 'picture size is better  854x480'
            "
          >
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
              <a-select v-model="form.tag" @change="onChange">
                <a-select-option
                  v-for="data in options"
                  :key="data.value"
                  :value="data.value"
                  >{{ data.label }}</a-select-option
                >
              </a-select>
              <span class="errorText">{{ errors[0] }}</span>
            </validation-provider>
          </a-form-item>
          <a-form-item label="Sorter" help="for picture sorting">
            <validation-provider vid="sorter" v-slot="{ errors }">
              <a-input-number
                v-model="form.sorter"
                :disabled="form.tag == 0"
              ></a-input-number>
              <span class="errorText">{{ errors[0] }}</span>
            </validation-provider>
          </a-form-item>
        </a-form>
      </validation-observer>
    </a-modal>
  </page-view>
</template>

<script>
import { PageView } from "@/layouts";
import { getApps, createApp, deleteApp } from "@/api/app";
export default {
  components: {
    PageView
  },
  data() {
    return {
      loading: false,
      uploading: false,
      listData: undefined,
      modal: false,
      form: {},
      fileList: [],
      options: [
        { value: 0, label: "Advertising" },
        { value: 1, label: "Banner" }
      ]
    };
  },
  mounted() {
    this.getListData();
  },
  methods: {
    getListData() {
      this.loading = true;
      getApps()
        .then(res => {
          this.listData = res.result;
        })
        .finally(() => {
          this.loading = false;
        });
    },
    deleteData(val) {
      this.loading = true;
      deleteApp(val.id)
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
      formData.append("sorter", this.form.sorter);

      this.uploading = true;
      createApp(formData)
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
    onChange(val) {
      if (val == 0) {
        this.form.sorter = 0;
      }
    },
    openModal(val) {
      this.modal = true;
      this.fileList = [];
      this.form = {
        tag: 0,
        sorter: 0
      };
    }
  }
};
</script>
