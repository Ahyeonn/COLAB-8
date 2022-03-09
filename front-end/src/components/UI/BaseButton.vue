<template>
  <button class="btn" v-bind="$attrs">
    {{ label }}
  </button>
</template>

<script>
export default {
  name: "BaseButton",
  props: {
    label: {
      type: String,
      required: true,
    },
  },
}
</script>
