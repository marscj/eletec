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
          <a-form-item label="Model">
            <validation-provider vid="model" v-slot="{ errors }">
              <a-select v-model="form.model" defaultValue="Personal">
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

          <a-form-item label="City">
            <validation-provider vid="city" v-slot="{ errors }">
              <a-input v-model="form.city"> </a-input>
              <span class="errorText">{{ errors[0] }}</span>
            </validation-provider>
          </a-form-item>

          <a-form-item label="Community">
            <validation-provider vid="community" v-slot="{ errors }">
              <a-input v-model="form.community"> </a-input>
              <span class="errorText">{{ errors[0] }}</span>
            </validation-provider>
          </a-form-item>

          <a-form-item label="Street">
            <validation-provider vid="street" v-slot="{ errors }">
              <a-input v-model="form.street"> </a-input>
              <span class="errorText">{{ errors[0] }}</span>
            </validation-provider>
          </a-form-item>

          <a-form-item label="Building">
            <validation-provider vid="building" v-slot="{ errors }">
              <a-input v-model="form.building"> </a-input>
              <span class="errorText">{{ errors[0] }}</span>
            </validation-provider>
          </a-form-item>

          <a-form-item label="Style">
            <validation-provider vid="style" v-slot="{ errors }">
              <a-select v-model="form.style" defaultValue="Apartment">
                <a-select-option key="1" value="Apartment"
                  >Apartment</a-select-option
                >
                <a-select-option key="2" value="Villa">Villa</a-select-option>
              </a-select>
              <span class="errorText">{{ errors[0] }}</span>
            </validation-provider>
          </a-form-item>

          <a-form-item label="OfficeNo">
            <validation-provider
              vid="office_no"
              name="OfficeNo"
              v-slot="{ errors }"
            >
              <a-input v-model="form.office_no"> </a-input>
              <span class="errorText">{{ errors[0] }}</span>
            </validation-provider>
          </a-form-item>

          <a-form-item label="Address" help="from the map">
            <validation-provider
              vid="address"
              name="address"
              v-slot="{ errors }"
            >
              <a-input v-model="form.address"> </a-input>
              <span class="errorText">{{ errors[0] }}</span>
            </validation-provider>
          </a-form-item>

          <a-form-item label="Latitude" help="from the map">
            <validation-provider vid="lat" name="latitude" v-slot="{ errors }">
              <a-input v-model="form.lat"> </a-input>
              <span class="errorText">{{ errors[0] }}</span>
            </validation-provider>
          </a-form-item>

          <a-form-item label="Longitude" help="from the map">
            <validation-provider vid="lgt" name="longitude" v-slot="{ errors }">
              <a-input v-model="form.lgt"> </a-input>
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
import { getAddress, updateAddress } from "@/api/user";
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
          title: "Model",
          dataIndex: "model"
        },
        {
          title: "City",
          dataIndex: "city"
        },

        {
          title: "Community",
          dataIndex: "community"
        },
        {
          title: "Street",
          dataIndex: "street"
        },
        {
          title: "Building",
          dataIndex: "building"
        },
        {
          title: "Style",
          dataIndex: "style"
        },
        {
          title: "OfficeNo",
          dataIndex: "office_no"
        },
        {
          title: "VillaNo",
          dataIndex: "villa_no"
        },
        {
          title: "Address",
          dataIndex: "address"
        },
        {
          title: "ACTION",
          width: "80px",
          scopedSlots: { customRender: "action" }
        }
      ],
      loadData: parameter => {
        return getAddress(
          Object.assign(parameter, {
            user_id: this.$store.getters.user.id
          })
        ).then(res => {
          console.log(res, "---");
          return res.result;
        });
      },
      form: {}
    };
  },
  methods: {
    openModal(val) {
      this.modal = true;
      this.form = Object.assign({}, val);
    },
    submit() {
      updateAddress(this.form.id, this.form);
    }
  }
};
</script>
