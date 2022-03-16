<script>
import BaseInput from "@/components/Form/BaseInput";
import BaseButton from "@/components/UI/BaseButton";

export default {
  name: "SignIn",
  components: {
    BaseInput,
    BaseButton
  },
  computed: {
    user() {
      return this.$store.state.auth.user
    }
  },
  methods: {
    updateUser({key, value}) {
      this.$store.commit('UPDATE_USER', {[key]: value})
    }
  }
}
</script>

<template>
  <div class="row">
    <div class="col-9 mb-4 col-md-6 mx-auto text-center">
      <h1 class="mt-4 text-primary text-center fw-bold">Create an account!</h1>
      <p class="text-md-start">Create and account to enjoy all of the features of HeadsUp!</p>
    </div>
  </div>
  <div class="row">
    <div class="col-md-6 mx-auto">
      <form @submit.prevent="">
        <!-- Name -->
        <div class="mb-3">
          <BaseInput
              class="form-control"
              name="name"
              label="Name"
              :modelValue="user.name"
              @input="(event) => updateUser({key: 'name', value: event.target.value})"
          />
        </div>
        <!-- Phone Number -->
        <div class="mb-3">
          <BaseInput
              class="form-control"
              name="phone-number"
              label="Phone Number"
              type="tel"
              :modelValue="user.phoneNumber"
              @input="(event) => updateUser({key: 'phoneNumber', value: event.target.value})"
          />
        </div>
        <!-- Password -->
        <div class="mb-3">
          <BaseInput
              class="form-control"
              name="password"
              label="password"
              type="password"
              :modelValue="user.password"
              @input="(event) => updateUser({key: 'password', value: event.target.value})"
          />
        </div>
        <div class="text-center">
          <BaseButton
              class="btn-primary mt-4"
              label="Create Account"
              type="submit"
          />
          <p class="pt-3">Already have an account?
            <router-link to="/log-in">Log in</router-link>
          </p>
        </div>

      </form>
    </div>
  </div>

</template>

<style scoped>

</style>
