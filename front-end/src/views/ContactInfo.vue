<script setup>
import BaseInput from "@/components/Form/BaseInput";
import BaseButton from "@/components/UI/BaseButton";
</script>

<template>
  <h2 class="my-4 text-md-center">📞 Almost there! Just enter everyone’s contact details! </h2>
  <div class="row">
    <div class="col-md-6 mx-auto">
      <div class="card shadow">
        <div class="card-body">
          <form>
            <!-- Host phone-number -->
            <div class="mb-3">
              <BaseInput
                  class="form-control"
                  name="host-phone-number"
                  label="Your number"
                  type="tel"
                  disabled
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
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>
