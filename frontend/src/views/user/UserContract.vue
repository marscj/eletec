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
          <a-card :hoverable="true" :title="'ID: ' + item.contractID">
            <ul style="padding: 0px 20px;">
              <li>
                <p>
                  Option: <em>{{ Options[item.option].label }}</em>
                </p>
              </li>
              <li>
                <p>
                  Issue: <em>{{ item.issue_date }}</em>
                </p>
              </li>
              <li>
                <p>
                  Expiry: <em>{{ item.expiry_date }}</em>
                </p>
              </li>
              <li>
                <p>
                  Validity:
                  <a-checkbox v-model="item.validity" disabled></a-checkbox>
                </p>
              </li>
              <li v-if="item.visits.length">
                <p>Usage Count:</p>
                <ul style="padding: 0px 20px;">
                  <li v-for="(data, index) in item.visits" :key="index">
                    <p>
                      {{ ServiceOptions[data.service].label }} :
                      <em> {{ data.count }}</em>
                    </p>
                  </li>
                </ul>
              </li>
              <li v-else>
                <p>Usage Count: <em>No data</em></p>
              </li>
              <li>
                <p>
                  Address: <em>{{ item.address }}</em>
                </p>
              </li>
              <li>
                <p>
                  Remark:
                  <em class="break-all whitespace-normal">{{ item.remark }}</em>
                </p>
              </li>
            </ul>
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
          <a-form-item label="Option">
            <validation-provider vid="option" v-slot="{ errors }">
              <a-select v-model="form.option">
                <a-select-option
                  v-for="data in Options"
                  :key="data.value"
                  :value="data.value"
                  >{{ data.label }}</a-select-option
                >
              </a-select>
              <span class="errorText">{{ errors[0] }}</span>
            </validation-provider>
          </a-form-item>

          <a-form-item label="Issue">
            <validation-provider vid="issue_date" v-slot="{ errors }">
              <a-date-picker v-model="form.issue_date" />
              <span class="errorText">{{ errors[0] }}</span>
            </validation-provider>
          </a-form-item>

          <a-form-item label="Expiry">
            <validation-provider vid="expiry_date" v-slot="{ errors }">
              <a-date-picker v-model="form.expiry_date" />
              <span class="errorText">{{ errors[0] }}</span>
            </validation-provider>
          </a-form-item>

          <a-form-item label="Address">
            <validation-provider vid="address" v-slot="{ errors }">
              <a-input v-model="form.address"></a-input>
              <span class="errorText">{{ errors[0] }}</span>
            </validation-provider>
          </a-form-item>

          <a-form-item label="Remark">
            <validation-provider vid="remark" v-slot="{ errors }">
              <a-textarea v-model="form.remark"> </a-textarea>
              <span class="errorText">{{ errors[0] }}</span>
            </validation-provider>
          </a-form-item>
        </a-form>
      </validation-observer>
    </a-modal>
  </div>
</template>

<script>
import moment from "moment";
import { Options } from "./const";
import { ServiceOptions } from "../order/const";

import {
  getContracts,
  updateContract,
  createContract,
  deleteContract
} from "@/api/user";

export default {
  data() {
    return {
      Options,
      ServiceOptions,
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
    moment,
    getListData() {
      this.loading = true;
      getContracts({ user_id: this.$route.params.id })
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
          option: 0
        },
        val,
        val
          ? {
              issue_date: moment(val.issue_date, "YYYY-MM-DD"),
              expiry_date: moment(val.expiry_date, "YYYY-MM-DD")
            }
          : {
              issue_date: moment(new Date(), "YYYY-MM-DD"),
              expiry_date: moment(new Date(), "YYYY-MM-DD")
            }
      );
    },
    submit() {
      if (this.form.id === undefined) {
        createContract({
          option: this.form.option,
          issue_date: moment(this.form.issue_date).format("YYYY-MM-DD"),
          expiry_date: moment(this.form.expiry_date).format("YYYY-MM-DD"),
          address: this.form.address,
          quantity: this.form.quantity,
          remark: this.form.remark,
          user_id: this.$route.params.id
        })
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
        updateContract(this.form.id, {
          option: this.form.option,
          issue_date: moment(this.form.issue_date).format("YYYY-MM-DD"),
          expiry_date: moment(this.form.expiry_date).format("YYYY-MM-DD"),
          address: this.form.address,
          quantity: this.form.quantity,
          remark: this.form.remark,
          user_id: this.$route.params.id
        })
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
      deleteContract(val.id)
        .then(res => {
          return this.getListData();
        })
        .finally(() => (this.loading = false));
    }
  }
};
</script>
