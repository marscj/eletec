<template>
  <div>
    <div align="right" class="table-operator">
      <a-button type="primary" icon="plus" @click="openModal()">
        New
      </a-button>
    </div>

    <s-table
      ref="table"
      :rowKey="record => record.id"
      :columns="columns"
      :data="loadData"
    >
      <template slot="action" slot-scope="data">
        <a href="#" @click="openModal(data)">Edit</a>
        <a-divider type="vertical"></a-divider>
        <a-popconfirm
          title="Are you sure delete this data?"
          @confirm="deleteData(data)"
          okText="Yes"
          cancelText="No"
        >
          <a href="#">Delete</a>
        </a-popconfirm>
      </template>
    </s-table>

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
          <a-form-item label="Action Date">
            <validation-provider
              vid="date"
              name="action date"
              v-slot="{ errors }"
            >
              <a-date-picker
                v-model="date"
                format="YYYY-MM-DD HH:mm"
                :showTime="{ defaultValue: moment('00:00:00', 'HH:mm') }"
                class="w-full"
              />
              <span class="errorText">{{ errors[0] }}</span>
            </validation-provider>
          </a-form-item>

          <a-form-item label="Card">
            <validation-provider vid="card" v-slot="{ errors }">
              <a-input v-model="form.card" class="w-full" />
              <span class="errorText">{{ errors[0] }}</span>
            </validation-provider>
          </a-form-item>

          <a-form-item label="Unit">
            <validation-provider vid="unit" v-slot="{ errors }">
              <a-input-number v-model="form.unit" class="w-full" />
              <span class="errorText">{{ errors[0] }}</span>
            </validation-provider>
          </a-form-item>

          <a-form-item
            label="Staff ID"
            help="Staff ID is user ID, user list check ID"
          >
            <validation-provider
              vid="staff_id"
              name="staff id"
              v-slot="{ errors }"
            >
              <a-input-number v-model="form.staff_id" class="w-full" />
              <span class="errorText">{{ errors[0] }}</span>
            </validation-provider>
          </a-form-item>

          <a-form-item label="Remark">
            <validation-provider vid="remark" v-slot="{ errors }">
              <a-textarea v-model="form.remark" />
              <span class="errorText">{{ errors[0] }}</span>
            </validation-provider>
          </a-form-item>
        </a-form>
      </validation-observer>
    </a-modal>
  </div>
</template>

<script>
import { STable } from "@/components";
import { getJobs, updateJob, createJob, deleteJob } from "@/api/job";
import moment from "moment";

export default {
  components: {
    STable
  },
  data() {
    return {
      queryParam: {},
      columns: [
        {
          title: "JOBID",
          dataIndex: "jobID",
          align: "center"
        },
        {
          title: "ACTION DATE",
          dataIndex: "date",
          align: "center"
        },
        {
          title: "CARD",
          dataIndex: "card",
          align: "center"
        },
        {
          title: "STAFF",
          dataIndex: "staff.name",
          align: "center"
        },
        {
          title: "ACTION",
          width: "140px",
          scopedSlots: { customRender: "action" },
          align: "center"
        }
      ],
      loadData: parameter => {
        return getJobs(
          Object.assign(parameter, this.queryParam, {
            order_id: this.$route.params.id
          })
        ).then(res => {
          return res.result;
        });
      },
      modal: false,
      form: {},
      date: moment(new Date())
    };
  },
  methods: {
    moment,
    openModal(val) {
      this.modal = true;
      this.form = Object.assign({}, val);
      this.date = moment(new Date());
    },
    submit() {
      if (this.form.id === undefined) {
        createJob(
          Object.assign(this.form, {
            date: this.date.format("YYYY-MM-DD HH:mm:ss"),
            order_id: this.$route.params.id
          })
        )
          .then(res => {
            this.modal = false;
            this.$refs.table.refresh();
          })
          .catch(error => {
            if (error.response) {
              this.$refs.observer.setErrors(error.response.data.result);
            }
          });
      } else {
        updateJob(
          this.form.id,
          Object.assign(this.form, {
            date: this.date.format("YYYY-MM-DD HH:mm:ss")
          })
        )
          .then(res => {
            this.modal = false;
            this.$refs.table.refresh();
          })
          .catch(error => {
            if (error.response) {
              this.$refs.observer.setErrors(error.response.data.result);
            }
          });
      }
    },
    deleteData(val) {
      deleteJob(val.id).then(res => {
        this.$refs.table.refresh();
      });
    }
  }
};
</script>
