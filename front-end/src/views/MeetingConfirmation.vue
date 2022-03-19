<script>
import BaseButton from "@/components/UI/BaseButton";
export default {
  name: "MeetingConfirmation",
  components: {BaseButton}
}
</script>

<template>
  <div class="row">
    <div class="col-md-6 mx-auto">
      <h3 class="my-4 text-center"> 🔍 Take a look and confirm your details blow!</h3>
      <section id="message-preview">
        <p class="fw-bold"><span class="step">1</span> Message Preview</p>
        <img class="img-fluid text-center" src="@/assets/SMS-preview.jpg" alt="">
      </section>
      <section id="recipients">
        <p class="fw-bold"><span>2</span> Recipients</p>
        <div class="text-center">
          <BaseButton class="btn-primary mt-4 py-2 w-75 text-white shadow-sm" label="Send HeadsUp!"/>
          <BaseButton class="btn-back mt-4 py-2 w-75 shadow-sm" label="Edit details"/>
        </div>

      </section>
    </div>
  </div>
</template>

<style scoped>

</style>
