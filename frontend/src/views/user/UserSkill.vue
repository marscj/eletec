<template>
  <div class="content">
    <div class="table-operator">
      <a-button type="primary" icon="plus" @click="openModal()">New</a-button>
    </div>

    <s-table
      ref="table"
      size="default"
      :rowKey="record => record.id"
      :columns="columns"
      :data="loadData"
      :pageURI="true"
      showPagination="auto"
      bordered
    >
      <template slot="action" slot-scope="data">
        <template>
          <a @click="openModal(data)">Edit</a>
        </template>
      </template>
    </s-table>

    <a-modal v-model="modal" title="Edit">
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

          <a-form-item label="Useful">
            <validation-provider vid="useful" v-slot="{ errors }">
              <a-checkbox v-model="form.useful"></a-checkbox>
              <span class="errorText">{{ errors[0] }}</span>
            </validation-provider>
          </a-form-item>

          <a-button type="primary" html-type="submit" @click="submit">
            Submit
          </a-button>
        </a-form>
      </validation-observer>
    </a-modal>
  </div>
</template>

<script>
import { getSkills, updateSkill } from "@/api/user";
import { STable, Ellipsis } from "@/components";
export default {
  components: {
    STable
  },
  data() {
    return {
      modal: false,
      columns: [
        {
          title: "Skill",
          dataIndex: "skill"
        },
        {
          title: "Useful",
          dataIndex: "useful"
        },

        {
          title: "Remark",
          dataIndex: "remark"
        },
        {
          title: "ACTION",
          width: "80px",
          scopedSlots: { customRender: "action" }
        }
      ],
      loadData: parameter => {
        return getSkills(
          Object.assign(parameter, {
            user_id: this.$store.getters.user.id
          })
        ).then(res => {
          return res.result;
        });
      },
      form: {}
    };
  },
  methods: {
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
      updateSkill(this.form.id, this.form);
    }
  }
};
</script>
