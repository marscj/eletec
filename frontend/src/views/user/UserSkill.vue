<template>
  <div class="content">
    <a-list
      ref="table"
      size="default"
      rowKey="id"
      :grid="{ gutter: 24, lg: 2, md: 2, sm: 1, xs: 1 }"
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
            <a-card-meta>
              <div class="meta-content" slot="description">
                {{ item.skill }}
              </div>
            </a-card-meta>
            <template class="ant-card-actions" slot="actions">
              <a @click="openModal(item)">Edit</a>
              <a>Delete</a>
            </template>
          </a-card>
        </template>
      </a-list-item>
    </a-list>

    <a-modal v-model="modal" title="Edit" @ok="submit">
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
import { getSkills, updateSkill, createSkill } from "@/api/user";

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
    this.getSkillData();
  },
  methods: {
    getSkillData() {
      this.loading = true;
      getSkills({ user_id: this.$route.params.id })
        .then(res => {
          res.result.unshift({});
          this.listData = res.result;
          console.log(res, "---");
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
            return this.getSkillData();
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
            return this.getSkillData();
          })
          .catch(error => {
            if (error.response) {
              this.$refs.observer.setErrors(error.response.data.result);
            }
          });
      }
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
