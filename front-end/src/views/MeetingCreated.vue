<template>
  <div class="row">
    <div class="col-md-6 mx-auto">
      <h3 class="my-4">🎉 Woohoo! Your HeadsUp! is all set up!</h3>
      <p>
        Your HeadsUp! is successfully set up! We will send a confirmation text to your group the day before the event. Come back and check your account to see who responded!
      </p>
      <router-link to="/" class="btn btn-primary mt-4 py-2 w-75 text-white mx-auto d-block shadow-sm" >
        Send another HeadsUp!
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: "MeetingCreated",
}
</script>

<style scoped>

</style>
