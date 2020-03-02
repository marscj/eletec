<template>
  <div class="content">
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
            <a-button type="primary" icon="plus" @click="openModal()">
              New
            </a-button>
          </div>
        </template>
        <template v-else>
          <a-row type="flex" justify="center" align="middle">
            <a-col :span="2">
              <a-radio v-model="item.defAddr" />
            </a-col>
            <a-col :span="22">
              <a-card :hoverable="true">
                <a-card-meta :description="item.title"> </a-card-meta>
                <template class="ant-card-actions" slot="actions">
                  <a @click="openModal(item)">Edit</a>
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
            </a-col>
          </a-row>
        </template>
      </a-list-item>
    </a-list>

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
          :label-col="{ span: 6 }"
          :wrapper-col="{ span: 12 }"
        >
          <a-form-item label="Model">
            <validation-provider vid="model" v-slot="{ errors }">
              <a-select v-model="form.model">
                <a-select-option key="1" value="Personal"
                  >Personal</a-select-option
                >
                <a-select-option key="2" value="Company"
                  >Company</a-select-option
                >
              </a-select>
              <span class="errorText">{{ errors[0] }}</span>
            </validation-provider>
          </a-form-item>

          <a-form-item label="Form">
            <validation-provider vid="form" v-slot="{ errors }">
              <span class="errorText">{{ errors[0] }}</span>
            </validation-provider>
          </a-form-item>

          <a-form-item label="To">
            <validation-provider vid="to" v-slot="{ errors }">
              <span class="errorText">{{ errors[0] }}</span>
            </validation-provider>
          </a-form-item>
        </a-form>
      </validation-observer>
    </a-modal>
  </div>
</template>

<script>
import {
  getAddress,
  updateAddress,
  createAddress,
  deleteAddress
} from "@/api/user";

export default {
  data() {
    return {
      modal: false,
      listData: [],
      loading: false,
      form: {}
    };
  },
  mounted() {
    this.getListData();
  },
  methods: {
    getListData() {
      this.loading = true;
      getAddress({ user_id: this.$route.params.id })
        .then(res => {
          res.result.unshift({});
          this.listData = res.result;
        })
        .finally(() => {
          this.loading = false;
        });
    },
    openModal(val) {
      this.modal = true;
      this.form = Object.assign(
        {
          model: "Personal"
        },
        val
      );
    },
    submit() {
      if (this.form.id === undefined) {
        createAddress(
          Object.assign({
            user_id: this.$route.params.id
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
        updateAddress(this.form.id, this.form)
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
      deleteAddress(val.id)
        .then(res => {
          return this.getListData();
        })
        .finally(() => (this.loading = false));
    }
  }
};
</script>
