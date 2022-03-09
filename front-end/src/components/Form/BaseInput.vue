<template>
  <label class="form-label" :for="identity">{{ label }}</label>
  <input
      :id="identity"
      :name="name"
      :maxlength="maxlength"
      :placeholder="placeholder"
      v-bind="$attrs"
      :value="modelValue"
      @input="$emit('update:modelValue', $event.target.value)"
  />
</template>

<script>
export default {
  name: 'BaseInput',
  props: {
    label: {
      type: String,
      required: true,
    },
    name: {
      type: String,
      required: true,
    },
    id: {
      type: String,
      required: false,
    },
    placeholder: {
      type: String,
      required: false,
    },
    maxlength: {
      type: String,
      required: false,
    },
    modelValue: {
      type: String,
      default: '',
    },
  },
  data() {
    return {
      // if the id attribute omitted use the same value as the name.
      identity: this.id ? this.id : this.name,
    };
  },
  methods: {
    emit(value) {
      this.$emit('update:modelValue', value);
    },
  },
};
</script>
