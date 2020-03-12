<template>
  <a-spin :spinning="loading">
    <validation-observer ref="observer">
      <validation-provider name="non_field_errors" v-slot="{ errors }">
        <span class="errorText">{{ errors[0] }}</span>
      </validation-provider>
      <a-form :form="form" :submit="submit">
        <a-row :gutter="16">
          <a-col :span="8">
            <a-form-item label="Service">
              <a-select v-model="form.service" disabled>
                <a-select-option
                  v-for="data in ServiceOptions"
                  :key="data.value"
                  :value="data.value"
                  >{{ data.label }}</a-select-option
                >
              </a-select>
            </a-form-item>
          </a-col>

          <a-col :span="8">
            <a-form-item label="Main Info">
              <a-select
                v-model="form.main_info"
                v-if="form.service != null"
                disabled
              >
                <a-select-option
                  v-for="(data, index) in MainInfoOptions[form.service]"
                  :key="index"
                  :value="index"
                  >{{ data }}</a-select-option
                >
              </a-select>
            </a-form-item>
          </a-col>

          <a-col :span="8">
            <a-form-item label="Sub Info">
              <a-select
                v-model="form.sub_info"
                v-if="form.service != null && form.main_info != null"
                disabled
              >
                <a-select-option
                  v-for="(data, index) in SubInfoOptions[form.service][
                    form.main_info
                  ]"
                  :key="index"
                  :value="index"
                  >{{ data }}</a-select-option
                >
              </a-select>
            </a-form-item>
          </a-col>

          <a-col :span="8">
            <a-form-item label="From Date">
              <a-input v-model="form.from_date" disabled></a-input>
            </a-form-item>
          </a-col>

          <a-col :span="8">
            <a-form-item label="To Date">
              <a-input v-model="form.to_date" disabled></a-input>
            </a-form-item>
          </a-col>

          <a-col :span="8">
            <a-form-item label="Create Date">
              <a-input v-model="form.create_at" disabled></a-input>
            </a-form-item>
          </a-col>

          <div v-if="form.user">
            <a-col :span="8">
              <a-form-item label="User">
                <a-input v-model="form.user.name" disabled> </a-input>
              </a-form-item>
            </a-col>

            <a-col :span="8">
              <a-form-item label="Phone">
                <a-input v-model="form.user.phone_number" disabled> </a-input>
              </a-form-item>
            </a-col>

            <a-col :span="8">
              <a-form-item label="Email">
                <a-input v-model="form.user.email" disabled> </a-input>
              </a-form-item>
            </a-col>
          </div>

          <a-col :span="8">
            <a-form-item label="Service Code">
              <validation-provider name="code" v-slot="{ errors }">
                <a-input v-model="form.code"></a-input>
                <span class="errorText">{{ errors[0] }}</span>
              </validation-provider>
            </a-form-item>
          </a-col>

          <a-col :span="8">
            <a-form-item label="Contract">
              <validation-provider name="status" v-slot="{ errors }">
                <a-select v-model="form.contract_id" allowClear>
                  <a-select-option
                    v-for="data in contracts"
                    :key="data.id"
                    :value="data.id"
                  >
                    <a-popover>
                      <template slot="content">
                        <ul class="px-4">
                          <li>Option: {{ Options[data.option].label }}</li>
                          <li>Issue: {{ data.issue_date }}</li>
                          <li>Expiry: {{ data.expiry_date }}</li>
                          <li v-if="data.visits.length">
                            <span>Usage Count:</span>
                            <ul class="px-4">
                              <li
                                v-for="(item, index) in data.visits"
                                :key="index"
                              >
                                <span>
                                  {{ ServiceOptions[item.service].label }} :
                                  {{ item.count }}
                                </span>
                              </li>
                            </ul>
                          </li>
                          <li v-else>
                            Usage Count: No data
                          </li>
                          <li>Address: {{ data.address }}</li>
                          <li>Remark: {{ data.remark }}</li>
                        </ul>
                      </template>
                      {{ data.contractID }}
                    </a-popover>
                  </a-select-option>
                </a-select>
                <span class="errorText">{{ errors[0] }}</span>
              </validation-provider>
            </a-form-item>
          </a-col>

          <a-col :span="8">
            <a-form-item label="Status">
              <validation-provider name="status" v-slot="{ errors }">
                <a-select v-model="form.status">
                  <a-select-option
                    v-for="data in StatusOptions"
                    :key="data.value"
                    :value="data.value"
                    >{{ data.label }}</a-select-option
                  >
                </a-select>
                <span class="errorText">{{ errors[0] }}</span>
              </validation-provider>
            </a-form-item>
          </a-col>

          <a-col :span="24">
            <a-form-item label="Address">
              <validation-provider name="address" v-slot="{ errors }">
                <a-input v-model="form.address"></a-input>
                <span class="errorText">{{ errors[0] }}</span>
              </validation-provider>
            </a-form-item>
          </a-col>
        </a-row>

        <div align="right">
          <a-button type="primary" html-type="submit" @click="submit">
            Submit
          </a-button>
        </div>
      </a-form>

      <div v-if="form.lat && form.lng" class="pt-10">
        <div class="title">Map</div>
        <gmap-map
          class="map"
          :center="{ lat: form.lat, lng: form.lng }"
          :zoom="16"
          map-type-id="satellite"
        >
          <gmap-marker
            :key="index"
            v-for="(m, index) in markers"
            :position="m.position"
            :clickable="true"
            :draggable="true"
            @click="center = m.position"
          />
        </gmap-map>
      </div>
    </validation-observer>
  </a-spin>
</template>

<script>
import { getOrder, updateOrder } from "@/api/order";
import { getContracts } from "@/api/user";
import { Options } from "../user/const";
import moment from "moment";

import {
  StatusOptions,
  ServiceOptions,
  MainInfoOptions,
  SubInfoOptions
} from "./const";

export default {
  data() {
    return {
      Options,
      StatusOptions,
      ServiceOptions,
      MainInfoOptions,
      SubInfoOptions,
      form: {},
      contracts: [],
      markers: [],
      loading: false
    };
  },
  mounted() {
    this.getOrderData();
  },
  watch: {
    form(val) {
      if (val) {
        this.markers.push({
          id: this.lastId,
          position: {
            lat: val.lat,
            lng: val.lng
          },
          opacity: 1,
          draggable: true,
          enabled: true,
          clicked: 0,
          rightClicked: 0,
          dragended: 0,
          ifw: false
        });
        this.$emit("data", val);
      }
    },
    "$route.params"(val) {
      this.getOrderData();
    }
  },
  methods: {
    moment,
    getOrderData() {
      this.loading = true;
      getOrder(this.$route.params.id)
        .then(res => {
          const { result } = res;
          this.form = result;
          return getContracts({ user_id: this.form.user.id }).then(res => {
            this.contracts = res.result;
          });
        })
        .finally(() => {
          this.loading = false;
        });
    },
    submit() {
      this.loading = true;
      updateOrder(this.$route.params.id, {
        status: this.form.status,
        address: this.form.address,
        user_id: this.form.user_id,
        contract_id: this.form.contract_id ? this.form.contract_id : null
      })
        .then(res => {
          const { result } = res;
          this.form = result;

          return getContracts({ user_id: this.form.user.id }).then(res => {
            this.contracts = res.result;
          });
        })
        .catch(error => {
          if (error.response) {
            this.$refs.observer.setErrors(error.response.data.result);
          }
        })
        .finally(() => {
          this.loading = false;
        });
    }
  }
};
</script>

<style lang="less" scoped>
.title {
  color: rgba(0, 0, 0, 0.85);
  font-size: 16px;
  font-weight: 500;
  margin-bottom: 16px;
}

.map {
  width: 100%;
  height: 600px;
  display: block;
}
</style>
