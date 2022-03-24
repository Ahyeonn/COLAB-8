<script>
import BaseInput from "@/components/Form/BaseInput";
import BaseButton from "@/components/UI/BaseButton";
import BaseModal from "@/components/BaseModal";

import useVuelidate from '@vuelidate/core'
import {required, alpha, minLength} from '@vuelidate/validators'

export default {
  name: "SignUp",
  components: {
    BaseInput,
    BaseButton,
    BaseModal
  },
  data() {
    return {
      isVisible: false,
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
    toggleModal() {
      this.isVisible = !this.isVisible;
    },
    closeToast() {
      this.anyErrors = false;
    },
    async signUp() {
      try {
        await this.$store.dispatch('register', this.user)
            .then(() => {
              this.isVisible = true;
            })
      } catch (error) {
        this.error = error;
        this.anyErrors = true;
      }
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

  <!-- display back-end errors -->
  <!-- TODO: create a toast component -->
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
      <base-modal @close="toggleModal" :modalActive="isVisible">
        <h2 class="text-primary text-center">We knew you would!</h2>
        <p>Your HeadsUp! account is successfully set up! You are now able to save contacts, repeat invites and see who
           responded to your HeadsUp!</p>
        <router-link
            class="btn btn-primary text-white mt-3 py-2 w-75 mx-auto d-block shadow-sm"
            to="/login">
          Login
        </router-link>
      </base-modal>

      <form @submit.prevent="signUp">
        <!-- Name -->
        <div class="mb-3">
          <BaseInput
              class="form-control"
              name="name"
              label="Name"
              required
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
              required
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
