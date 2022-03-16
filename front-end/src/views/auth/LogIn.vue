<script>
import BaseInput from "@/components/Form/BaseInput";
import BaseButton from "@/components/UI/BaseButton";

export default {
  name: "LogIn",
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
  <div class="text-center">
    <h1 class="mt-4 text-primary fw-bold">Log in</h1>
    <p>Welcome Back!</p>
  </div>
  <div class="row">
    <div class="col-md-6 mx-auto">
      <form @submit.prevent="">
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
              label="Log In"
              type="submit"
          />
          <p class="pt-3">Don’t have an account?
            <router-link to="/sign-in">Sign up</router-link>
          </p>
        </div>
      </form>
    </div>
  </div>

</template>

<style scoped>

</style>
