<script setup>
import BaseInput from "@/components/Form/BaseInput";
import BaseButton from "@/components/UI/BaseButton";
</script>

<template>
  <h1 class="mt-4 text-primary text-center fw-bold">Log in</h1>
  <p class="text-center">Welcome Back!</p>
  <form>
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
          label="Log In"
      />
      <p class="pt-3">Don’t have an account? <router-link to="/sign-in">Sign up</router-link></p>
    </div>
  </form>

</template>

<style scoped>

</style>
