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
              <a-radio v-model="item.defAddr" disabled />
            </a-col>
            <a-col :span="22">
              <a-card :hoverable="true">
                <a-card-meta :title="item.title"> </a-card-meta>
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
                <a-select-option
                  v-for="data in ModelOptions"
                  :key="data.value"
                  :value="data.value"
                  >{{ data.label }}</a-select-option
                >
              </a-select>
              <span class="errorText">{{ errors[0] }}</span>
            </validation-provider>
          </a-form-item>

          <a-form-item label="Style">
            <validation-provider vid="style" v-slot="{ errors }">
              <a-select v-model="form.style">
                <a-select-option
                  v-for="data in StyleOptions"
                  :key="data.value"
                  :value="data.value"
                  >{{ data.label }}</a-select-option
                >
              </a-select>
              <span class="errorText">{{ errors[0] }}</span>
            </validation-provider>
          </a-form-item>

          <a-form-item label="City">
            <validation-provider vid="city" v-slot="{ errors }">
              <a-input v-model="form.city"></a-input>
              <span class="errorText">{{ errors[0] }}</span>
            </validation-provider>
          </a-form-item>

          <a-form-item label="Community">
            <validation-provider vid="community" v-slot="{ errors }">
              <a-input v-model="form.community"></a-input>
              <span class="errorText">{{ errors[0] }}</span>
            </validation-provider>
          </a-form-item>

          <a-form-item label="Street">
            <validation-provider vid="street" v-slot="{ errors }">
              <a-input v-model="form.street"></a-input>
              <span class="errorText">{{ errors[0] }}</span>
            </validation-provider>
          </a-form-item>

          <a-form-item label="Building">
            <validation-provider vid="building" v-slot="{ errors }">
              <a-input v-model="form.building"></a-input>
              <span class="errorText">{{ errors[0] }}</span>
            </validation-provider>
          </a-form-item>

          <a-form-item
            :label="
              form.style === 0
                ? form.model === 0
                  ? 'RoomNo'
                  : 'OfficeNo'
                : 'VillaNo'
            "
          >
            <validation-provider vid="roomNo" v-slot="{ errors }">
              <a-input v-model="form.roomNo"></a-input>
              <span class="errorText">{{ errors[0] }}</span>
            </validation-provider>
          </a-form-item>

          <a-form-item
            label="Address"
          >
            <validation-provider vid="address" v-slot="{ errors }">
              <a-input v-model="form.address"></a-input>
              <span class="errorText">{{ errors[0] }}</span>
            </validation-provider>
          </a-form-item>

          <!-- <a-form-item label="Default Address">
            <a-checkbox v-model="form.defAddr" />
          </a-form-item> -->
        </a-form>
      </validation-observer>
    </a-modal>
  </div>
</template>

<script>
import { ModelOptions, StyleOptions } from "./const";

import {
  getAddress,
  updateAddress,
  createAddress,
  deleteAddress
} from "@/api/user";

export default {
  data() {
    return {
      ModelOptions,
      StyleOptions,
      modal: false,
      listData: undefined,
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
          model: 0,
          style: 0
        },
        val
      );
    },
    submit() {
      if (this.form.id === undefined) {
        createAddress(
          Object.assign(this.form, {
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
