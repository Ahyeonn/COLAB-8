<template>
  <label class="form-label" :class="labelStatus" :for="identity">
    {{ label }}
  </label>
  <input
      :id="identity"
      :name="name"
      :class="fieldStatus"
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
    currentValue: {
      default: '',
    },
    invalid: {
      type: Boolean,
      required: false,
    },
  },
  data() {
    return {
      // if the id attribute omitted use the same value as the name.
      identity: this.id ? this.id : this.name,
    };
  },
  mounted() {
    this.emit(this.currentValue);
  },
  computed: {
    labelStatus() {
      if (!this.invalid && this.modelValue !== '') {
        return 'text-success';
      }
      if (this.invalid) {
        return 'text-danger';
      }
      return '';
    },
    fieldStatus() {
      if (!this.invalid && this.modelValue !== '') {
        return 'is-valid';
      }
      if (this.invalid) {
        return 'is-invalid';
      }
      return '';
    },
  },
  methods: {
    emit(value) {
      this.$emit('update:modelValue', value);
    },
  },
};
</script>
