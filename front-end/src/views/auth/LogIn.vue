<script>
import BaseInput from "@/components/Form/BaseInput";
import BaseButton from "@/components/UI/BaseButton";

import useVuelidate from '@vuelidate/core'
import {required, minLength} from '@vuelidate/validators'

export default {
  name: "LogIn",
  components: {
    BaseInput,
    BaseButton
  },
  data() {
    return {
      error: '',
      anyErrors: false,
    }
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
    closeToast() {
      this.anyErrors = false;
    },
    async login() {
      try {
        await this.$store.dispatch('login', this.user)
            .then(() => {
              this.$router.push({ path : '/dashboard' });
            })
      }
      catch (error) {
        this.error = error;
        this.anyErrors = true;
      }
    }
  }
}
</script>

<template>
  <div class="text-center">
    <h1 class="mt-4 text-primary fw-bold">Log in</h1>
    <p>Welcome Back! <br />
       We’re so happy to see you!</p>
  </div>
  <!-- display back-end errors -->
  <div v-show="anyErrors" class="toast show mb-3" role="alert" aria-live="assertive" aria-atomic="true">
    <div class="toast-header">
      <strong class="me-auto">Oh no!</strong>
      <small>now</small>
      <button
          type="button"
          class="btn-close"
          data-bs-dismiss="toast"
          aria-label="Close"
          @click="closeToast"
      ></button>
    </div>
    <div class="toast-body">
      {{error}}
    </div>
  </div>
  <div class="row">
    <div class="col-md-6 mx-auto">
      <form @submit.prevent="login">
        <!-- Phone Number -->
        <div class="mb-3">
          <BaseInput
              class="form-control"
              name="phone-number"
              label="Phone Number"
              type="tel"
              required
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
              required
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
              class="btn-primary mt-4 py-2 w-75 text-white shadow-sm"
              label="Log In"
              type="submit"
          />
          <p class="pt-3">Don’t have an account?
            <router-link to="/sign-up">Sign up</router-link>
          </p>
        </div>
      </form>
    </div>
  </div>

</template>

<style scoped>

</style>
