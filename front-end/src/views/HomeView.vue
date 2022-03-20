<script>
import BaseInput from "@/components/Form/BaseInput";
import BaseButton from "@/components/UI/BaseButton";

import useVuelidate from '@vuelidate/core'
import { required, alpha,minLength, alphaNum } from '@vuelidate/validators'

export default {
  name: "HomeView",
  components: {
    BaseInput,
    BaseButton
  },
  setup: () => ({ v$: useVuelidate() }),
  data() {
    return {
      meeting: {
        hostName: '',
        name: '',
        date: '',
        time: '',
      }
    }
  },
  validations () {
    return {
      meeting: {
        hostName: {
          required,
          alpha,
          minLength: minLength(3),
          $autoDirty: true,
        },
        name: {
          required,
          alphaNum,
          minLength: minLength(5),
          $autoDirty: true,
        },
        date: {
          required,
          $autoDirty: true,
        },
        time: {
          required,
          $autoDirty: true,
        }
      }
    }
  },
  methods: {
    async onSubmit() {
      await this.$store.dispatch('createMeeting', this.meeting)
      await this.$router.push({ path : '/contact-info' });
    }
  }
}
</script>

<template>
  <h3 class="my-4 text-center"> 👋 Hi there! Let's get started on your heads up!</h3>
  <div class="row">
    <div class="col-md-6 mx-auto">
      <div class="card shadow">
        <div class="card-body">
          <form @submit.prevent="onSubmit">
            <!-- Name -->
            <div class="mb-3">
              <BaseInput
                  class="form-control"
                  name="hostName"
                  label="Host name"
                  required
                  :modelValue="meeting.hostName"
                  @input="(event) => meeting.hostName = event.target.value"
                  :invalid="v$.meeting.hostName.$error"
              />
              <!-- Display errors -->
              <template v-if="v$.meeting.hostName.$error">
                <template
                    v-for="(error, index) of v$.meeting.hostName.$errors"
                    :key="index"
                >
                  <p>{{ error.$message }}</p>
                </template>
              </template>
            </div>
            <!-- Meeting name -->
            <div class="mb-3">
              <BaseInput
                  class="form-control"
                  name="meeting-name"
                  label="Meeting name"
                  required
                  :modelValue="meeting.name"
                  @input="(event) => meeting.name = event.target.value"
                  :invalid="v$.meeting.name.$error"
              />
              <!-- Display errors -->
              <template v-if="v$.meeting.name.$error">
                <template
                    v-for="(error, index) of v$.meeting.name.$errors"
                    :key="index"
                >
                  <p>{{ error.$message }}</p>
                </template>
              </template>
            </div>
            <!-- Date -->
            <div class="mb-3">
              <BaseInput
                  class="form-control"
                  name="meeting-date"
                  label="Date"
                  type="date"
                  required
                  :modelValue="meeting.date"
                  @input="(event) => meeting.date = event.target.value"
                  :invalid="v$.meeting.date.$error"
              />
              <!-- Display errors -->
              <template v-if="v$.meeting.date.$error">
                <template
                    v-for="(error, index) of v$.meeting.date.$errors"
                    :key="index"
                >
                  <p>{{ error.$message }}</p>
                </template>
              </template>
            </div>
            <!-- Time -->
            <div class="mb-3">
              <BaseInput
                  class="form-control"
                  name="meeting-time"
                  label="Time"
                  type="time"
                  required
                  min="07:00" max="22:00"
                  :modelValue="meeting.time"
                  @input="(event) => meeting.time = event.target.value"
                  :invalid="v$.meeting.time.$error"
              />
              <!-- Display errors -->
              <template v-if="v$.meeting.time.$error">
                <template
                    v-for="(error, index) of v$.meeting.time.$errors"
                    :key="index"
                >
                  <p>{{ error.$message }}</p>
                </template>
              </template>
            </div>

            <div class="text-center py-3">
              <BaseButton
                  type="submit"
                  class="btn-primary mt-4 py-2 w-75 text-white shadow-sm"
                  label="Continue"
              />
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
</style>
