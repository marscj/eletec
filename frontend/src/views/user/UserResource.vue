<template>
  <div>
    <a-list
      ref="list"
      size="default"
      rowKey="id"
      :grid="{ gutter: 24, lg: 1, md: 1, sm: 1, xs: 1 }"
      :dataSource="listData"
      :loading="loading"
    >
      <a-list-item slot="renderItem" slot-scope="item">
        <template v-if="!item || item.id === undefined">
          <div align="right" class="table-operator">
            <a-upload
              name="Id"
              :multiple="false"
              :beforeUpload="beforeUpload"
              :customRequest="upload"
              :showUploadList="false"
              style="padding: 10px 10px;"
            >
              <a-button type="primary" icon="plus" :loading="uploading">
                New
              </a-button>
            </a-upload>
          </div>
        </template>
        <template v-else>
          <a-card :hoverable="true">
            <img :src="item.image.large" slot="cover" alt="images" />

            <a-card-meta :title="FlagOptions[item.flag]"></a-card-meta>

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
  </div>
</template>

<script>
import { FlagOptions } from "./const";
import { getImages, uploadImage, deleteImage } from "@/api/image";
export default {
  data() {
    return {
      FlagOptions,
      loading: false,
      uploading: false,
      listData: []
    };
  },
  mounted() {
    this.getListData();
  },
  methods: {
    getListData() {
      this.loading = true;
      getImages({ object_id: this.$route.params.id, content: 0 })
        .then(res => {
          res.result.unshift({});
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
      return isIMG && isLt2M;
    },
    upload(request) {
      const formData = new FormData();
      formData.append("image", request.file);
      formData.append("content", 0);
      formData.append("flag", 3);
      formData.append("object_id", this.$route.params.id);
      this.uploading = true;
      uploadImage(formData)
        .then(res => {
          this.getListData();
        })
        .finally(() => {
          this.uploading = false;
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
