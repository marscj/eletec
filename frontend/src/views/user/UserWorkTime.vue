<template>
  <div class="content">
    <a-list
      ref="table"
      size="default"
      rowKey="id"
      :grid="{ gutter: 24, lg: 1, md: 2, sm: 1, xs: 1 }"
      :dataSource="listData"
      :loading="loading"
    >
      <a-list-item slot="renderItem" slot-scope="item">
        <template v-if="!item || item.id === undefined">
          <a-button class="new-btn" type="dashed" @click="openModal()">
            <a-icon type="plus" />
            New
          </a-button>
        </template>
        <template v-else>
          <a-card :hoverable="true">
            <a-card-meta :description="item.skill"> </a-card-meta>
            {{ item.remark }}

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
                <a-select-option key="1" value="Monday">Monday</a-select-option>
                <a-select-option key="2" value="Tuesday"
                  >Tuesday</a-select-option
                >
                <a-select-option key="3" value="Wednesday"
                  >Wednesday</a-select-option
                >
                <a-select-option key="4" value="Thursday"
                  >Thursday</a-select-option
                >
                <a-select-option key="5" value="Friday">Friday</a-select-option>
                <a-select-option key="6" value="Saturday"
                  >Saturday</a-select-option
                >
                <a-select-option key="7" value="Sunday">Sunday</a-select-option>
              </a-select>
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
import {
  getWorkTimes,
  updateWorkTime,
  createWorkTime,
  deleteWorkTime
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
      getWorkTimes({ user_id: this.$route.params.id })
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
          useful: true,
          week: "Monday"
        },
        val
      );
    },
    submit() {
      if (this.form.id === undefined) {
        createWorkTime(
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
        updateWorkTime(this.form.id, this.form)
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

<style lang="less" scoped>
@import "~@/components/index.less";

.card-list {
  /deep/ .ant-card-body:hover {
    .ant-card-meta-title > a {
      color: @primary-color;
    }
  }

  /deep/ .ant-card-meta-title {
    margin-bottom: 12px;

    & > a {
      display: inline-block;
      max-width: 100%;
      color: rgba(0, 0, 0, 0.85);
    }
  }

  /deep/ .meta-content {
    position: relative;
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    height: 64px;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;

    margin-bottom: 1em;
  }
}

.card-avatar {
  width: 48px;
  height: 48px;
  border-radius: 48px;
}

.ant-card-actions {
  background: #f7f9fa;

  li {
    float: left;
    text-align: center;
    margin: 12px 0;
    color: rgba(0, 0, 0, 0.45);
    width: 50%;

    &:not(:last-child) {
      border-right: 1px solid #e8e8e8;
    }

    a {
      color: rgba(0, 0, 0, 0.45);
      line-height: 22px;
      display: inline-block;
      width: 100%;
      &:hover {
        color: @primary-color;
      }
    }
  }
}

.new-btn {
  background-color: #fff;
  border-radius: 2px;
  width: 100%;
  height: 110px;
}
</style>
