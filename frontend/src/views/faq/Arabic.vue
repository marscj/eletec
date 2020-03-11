<template>
  <div>
    <div align="right" class="table-operator">
      <a-button type="primary" icon="plus" @click="openModal()">
        New
      </a-button>
    </div>
    <a-spin :spinning="loading">
      <div v-if="listData.length">
        <a-collapse :bordered="false">
          <template v-slot:expandIcon="props">
            <a-icon type="caret-right" :rotate="props.isActive ? 90 : 0" />
          </template>
          <a-collapse-panel
            v-for="data in listData"
            :key="data.id"
            style="background: #f7f7f7; border-radius: 4px; margin-bottom: 14px; border: 0; overflow: hidden"
          >
            <template slot="header">
              <span>{{ data.title }}</span>
            </template>
            <p class="whitespace-pre-line">{{ data.content }}</p>
            <a @click="openModal(data)">Edit</a>
            <a-popconfirm
              title="Are you sure delete this data?"
              @confirm="deleteData(data)"
              okText="Yes"
              cancelText="No"
              class="pl-4"
            >
              <a href="#">Delete</a>
            </a-popconfirm>
          </a-collapse-panel>
        </a-collapse>
      </div>
      <a-empty v-else />
    </a-spin>
    <a-modal
      v-model="modal"
      :title="this.form.id === undefined ? 'Create' : 'Edit'"
      @ok="submit"
    >
      <validation-observer ref="observer">
        <validation-provider name="non_field_errors" v-slot="{ errors }">
          <span class="errorText">{{ errors[0] }}</span>
        </validation-provider>

        <a-form
          :form="form"
          :submit="submit"
          :label-col="{ span: 4 }"
          :wrapper-col="{ span: 16 }"
        >
          <a-form-item label="Title">
            <validation-provider vid="title" v-slot="{ errors }">
              <a-input v-model="form.title"></a-input>
              <span class="errorText">{{ errors[0] }}</span>
            </validation-provider>
          </a-form-item>

          <a-form-item label="Content">
            <validation-provider vid="content" v-slot="{ errors }">
              <a-textarea v-model="form.content" :rows="6"> </a-textarea>
              <span class="errorText">{{ errors[0] }}</span>
            </validation-provider>
          </a-form-item>
        </a-form>
      </validation-observer>
    </a-modal>
  </div>
</template>

<script>
import { getFaqs, updateFaq, createFaq, deleteFaq } from "@/api/faq";
export default {
  data() {
    return {
      loading: false,
      uploading: false,
      listData: [],
      modal: false,
      form: {}
    };
  },
  mounted() {
    this.getListData();
  },
  methods: {
    getListData() {
      this.loading = true;
      getFaqs({ language: "ar" })
        .then(res => {
          this.listData = res.result;
        })
        .finally(() => {
          this.loading = false;
        });
    },
    submit() {
      if (this.form.id === undefined) {
        createFaq(
          Object.assign(this.form, {
            language: "ar"
          })
        )
          .then(res => {
            this.modal = false;

            return this.getListData();
          })
          .catch(error => {
            if (error.response) {
              this.$refs.observer.setErrors(error.response.data.result);
            }
          });
      } else {
        updateFaq(this.form.id, this.form)
          .then(res => {
            this.modal = false;
            return this.getListData();
          })
          .catch(error => {
            if (error.response) {
              this.$refs.observer.setErrors(error.response.data.result);
            }
          });
      }
    },
    deleteData(val) {
      this.loading = true;
      deleteFaq(val.id)
        .then(res => {
          this.getListData();
        })
        .finally(() => {
          this.loading = false;
        });
    },
    openModal(val) {
      this.modal = true;
      this.form = Object.assign({}, val);
    }
  }
};
</script>
