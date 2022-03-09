<script setup>
import BaseInput from "@/components/Form/BaseInput";
import BaseButton from "@/components/UI/BaseButton";
</script>

<template>
  <h1 class="mt-4 text-primary text-center fw-bold">Create an account!</h1>
  <div class="row">
    <div class="col-8 mx-auto">
      <p class="text-center ">Create and account to enjoy all of the features of HeadsUp!</p>
    </div>
  </div>
  <form action="">
    <!-- Name -->
    <div class="mb-3">
      <BaseInput
          class="form-control"
          name="name"
          label="Name"
      />
    </div>
    <!-- Phone Number -->
    <div class="mb-3">
      <BaseInput
          class="form-control"
          name="phone-number"
          label="Phone Number"
          type="tel"
      />
    </div>
    <!-- Password -->
    <div class="mb-3">
      <BaseInput
          class="form-control"
          name="password"
          label="password"
          type="password"
      />
    </div>
    <div class="text-center">
      <BaseButton
          class="btn-primary mt-4"
          label="Create Account"
      />
      <p class="pt-3">Already have an account? <router-link to="/log-in">Log in</router-link></p>
    </div>

  </form>
</template>

<style scoped>

</style>
