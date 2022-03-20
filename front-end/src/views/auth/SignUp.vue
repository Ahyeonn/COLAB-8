<script>
import BaseInput from "@/components/Form/BaseInput";
import BaseButton from "@/components/UI/BaseButton";

import useVuelidate from '@vuelidate/core'
import {required, alpha, minLength} from '@vuelidate/validators'

export default {
  name: "SignUp",
  components: {
    BaseInput,
    BaseButton
  },
  setup: () => ({v$: useVuelidate()}),
  computed: {
    user() {
      return this.$store.state.auth.user
    }
  },
  validations() {
    return {
      user: {
        name: {
          required,
          alpha,
          minLength: minLength(3),
          $autoDirty: true,
        },
        phoneNumber: {
          required,
          minLength: minLength(10),
          $autoDirty: true,
        },
        password: {
          required,
          minLength: minLength(8),
          $autoDirty: true,
        }
      }
    }
  },
  methods: {
    updateUser({key, value}) {
      this.$store.commit('UPDATE_USER', {[key]: value})
    },
    signUp() {
      this.$store.dispatch('register', this.user)
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
      <form @submit.prevent="signUp">
        <!-- Name -->
        <div class="mb-3">
          <BaseInput
              class="form-control"
              name="name"
              label="Name"
              :modelValue="user.name"
              @input="(event) => updateUser({key: 'name', value: event.target.value})"
              :invalid="v$.user.name.$error"
          />
          <!-- Display errors -->
          <template v-if="v$.user.name.$error">
            <template
                v-for="(error, index) of v$.user.name.$errors"
                :key="index"
            >
              <p>{{ error.$message }}</p>
            </template>
          </template>
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
              :invalid="v$.user.phoneNumber.$error"
          />
          <!-- Display errors -->
          <template v-if="v$.user.phoneNumber.$error">
            <template
                v-for="(error, index) of v$.user.phoneNumber.$errors"
                :key="index"
            >
              <p>{{ error.$message }}</p>
            </template>
          </template>
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
              :invalid="v$.user.password.$error"
          />
          <!-- Display errors -->
          <template v-if="v$.user.password.$error">
            <template
                v-for="(error, index) of v$.user.password.$errors"
                :key="index"
            >
              <p>{{ error.$message }}</p>
            </template>
          </template>
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
