<script setup>
import BaseInput from "@/components/Form/BaseInput";
import BaseButton from "@/components/UI/BaseButton";
</script>

<template>
  <h2 class="my-4">📞 Almost there! Just enter everyone’s contact details! </h2>
  <form>
    <!-- Phone Number -->
    <div class="mb-3">
      <BaseInput
          class="form-control"
          name="phone-number"
          label="Phone Number"
          type="phone"
      />
    </div>
    <!-- Contact Number #1 -->
    <div class="mb-3">
      <BaseInput
          class="form-control"
          name="contact-number-1"
          label="Contact Number #1"
          type="tel"
      />
    </div>
    <!-- Contact Number #2 -->
    <div class="mb-3">
      <BaseInput
          class="form-control"
          name="contact-number-2"
          label="Contact Number #2"
          type="tel"
      />
    </div>

    <!-- Contact Number #3 -->
    <div class="mb-3">
      <BaseInput
          class="form-control"
          name="contact-number-3"
          label="Contact Number #3"
          type="tel"
      />
    </div>

      <BaseButton
          class="btn-secondary mt-4 d-block mx-auto"
          label="Add another contact +"
      />
      <BaseButton
          class="btn-primary mt-4 d-block mx-auto"
          label="Send HeadsUp!"
      />
  </form>
</template>

<style scoped>

</style>
