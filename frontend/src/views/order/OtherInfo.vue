<template>
  <div>
    <div v-if="form.other_info || form.image" class="pt-10">
      <description-list title="Other Info">
        <a-card>
          <img
            v-for="data in form.images"
            :key="data.id"
            :src="data.image.medium"
            alt="image"
            slot="cover"
            class="pb-2"
          />

          <a-card-meta :description="form.other_info"> </a-card-meta>
        </a-card>
      </description-list>
    </div>
  </div>
</template>

<script>
export default {};
</script>
