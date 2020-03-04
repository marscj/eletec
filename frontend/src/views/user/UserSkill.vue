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
          <a-card :hoverable="true" :title="SkillOptions[item.skill].label">
            <p v-if="item.skill === 5">{{ item.remark }}</p>
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
                <a-select-option
                  v-for="data in SkillOptions"
                  :key="data.value"
                  :value="data.value"
                  >{{ data.label }}</a-select-option
                >
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

const SkillOptions = [
  { value: 0, label: "Air Conditioner" },
  { value: 1, label: "Electrical" },
  { value: 2, label: "Plumbing" },
  { value: 3, label: "House Cleaning" },
  { value: 4, label: "Duct Cleaning" },
  { value: 5, label: "Other" }
];

export default {
  data() {
    return {
      SkillOptions,
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
          skill: 0
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
