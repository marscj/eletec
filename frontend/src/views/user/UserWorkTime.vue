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
          <a-card :hoverable="true" :title="WeekOptions[item.week].label">
            {{ item.form | moment("HH:mm") }} - {{ item.to | moment("HH:mm") }}
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
          <a-form-item label="Days of week">
            <validation-provider vid="week" v-slot="{ errors }">
              <a-select v-model="form.week">
                <a-select-option
                  v-for="data in WeekOptions"
                  :key="data.value"
                  :value="data.value"
                  >{{ data.label }}</a-select-option
                >
              </a-select>
              <span class="errorText">{{ errors[0] }}</span>
            </validation-provider>
          </a-form-item>

          <a-form-item label="Form">
            <validation-provider vid="form" v-slot="{ errors }">
              <a-time-picker v-model="form.form" format="HH:mm" />
              <span class="errorText">{{ errors[0] }}</span>
            </validation-provider>
          </a-form-item>

          <a-form-item label="To">
            <validation-provider vid="to" v-slot="{ errors }">
              <a-time-picker v-model="form.to" format="HH:mm" />
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
import {
  getWorkTimes,
  updateWorkTime,
  createWorkTime,
  deleteWorkTime
} from "@/api/user";
import { WeekOptions } from "./const";

export default {
  data() {
    return {
      WeekOptions,
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
      getWorkTimes({ user_id: this.$route.params.id })
        .then(res => {
          res.result.unshift({});
          this.listData = res.result.map(f => {
            f.form = moment(f.form, "HH:mm");
            f.to = moment(f.to, "HH:mm");
            return f;
          });
        })
        .finally(() => {
          this.loading = false;
        });
    },
    openModal(val) {
      this.modal = true;
      this.form = Object.assign(
        {
          week: 0
        },
        val,
        val
          ? {
              form: moment(val.form, "HH:mm"),
              to: moment(val.to, "HH:mm")
            }
          : {
              form: moment("08:00", "HH:mm"),
              to: moment("18:00", "HH:mm")
            }
      );
    },
    submit() {
      if (this.form.id === undefined) {
        createWorkTime({
          week: this.form.week,
          form: moment(this.form.form).format("HH:mm:ss"),
          to: moment(this.form.to).format("HH:mm:ss"),
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
        updateWorkTime(this.form.id, {
          week: this.form.week,
          form: moment(this.form.form).format("HH:mm:ss"),
          to: moment(this.form.to).format("HH:mm:ss"),
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
      deleteWorkTime(val.id)
        .then(res => {
          return this.getListData();
        })
        .finally(() => (this.loading = false));
    }
  }
};
</script>
