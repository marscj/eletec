<template>
  <div class="flex items-center h-full justify-center">
    <div class="max-w-sm rounded overflow-hidden shadow-lg bg-white p-10">
      <img
        class="w-full"
        src="@/assets/images/register.jpg"
        alt="Sunset in the mountains"
      />
      <div class="px-6 py-4">
        <div class="font-bold text-xl mb-2 text-center py-10">
          <div v-if="!loading">
            <p v-if="validate">
              Email verification successful
            </p>
            <p v-else>
              Email verification faile
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { emailValidate } from "@/api/auth";
export default {
  data() {
    return {
      loading: false,
      validate: undefined
    };
  },
  computed: {
    emailKey: () => {
      return this.$route.query.key;
    }
  },
  mounted() {
    this.validateEmail();
  },
  methods: {
    validateEmail() {
      this.loading = true;
      emailValidate({
        key: this.$route.query.key
      })
        .then(res => {
          this.validate = true;
        })
        .catch(error => {
          this.validate = false;
        })
        .finally(() => {
          this.loading = false;
        });
    }
  }
};
</script>
