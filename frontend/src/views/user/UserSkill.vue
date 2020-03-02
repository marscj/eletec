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
          <a-form-item label="Skill">
            <validation-provider vid="skill" v-slot="{ errors }">
              <a-select v-model="form.skill">
                <a-select-option key="1" value="A/C">A/C</a-select-option>
                <a-select-option key="2" value="Electrical"
                  >Electrical</a-select-option
                >
                <a-select-option key="3" value="Plumbing"
                  >Plumbing</a-select-option
                >
                <a-select-option key="4" value="Cleaning"
                  >Cleaning</a-select-option
                >
                <a-select-option key="5" value="Duct Cleaning"
                  >Duct Cleaning</a-select-option
                >
                <a-select-option key="6" value="Other">Other</a-select-option>
              </a-select>
              <span class="errorText">{{ errors[0] }}</span>
            </validation-provider>
          </a-form-item>

          <a-form-item v-if="form.skill === 'Other'" label="Remark">
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
import { getSkills, updateSkill, createSkill, deleteSkill } from "@/api/user";

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
      getSkills({ user_id: this.$route.params.id })
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
          skill: "A/C"
        },
        val
      );
    },
    submit() {
      if (this.form.id === undefined) {
        createSkill(
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
        updateSkill(this.form.id, this.form)
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
      deleteSkill(val.id)
        .then(res => {
          return this.getListData();
        })
        .finally(() => (this.loading = false));
    }
  }
};
</script>
