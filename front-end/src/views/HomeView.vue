<script>
import BaseInput from "@/components/Form/BaseInput";
import BaseButton from "@/components/UI/BaseButton";

// import { mapActions } from 'vuex'

export default {
  name: "HomeView",
  components: {
    BaseInput,
    BaseButton
  },
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
  methods: {
    onSubmit() {
      this.$store.dispatch('createMeeting', this.meeting)
      this.$router.push({ path : '/contact-info' });
    }
  }
}
</script>

<template>
  <h3 class="my-4"> 👋 Hi there! Let's get started on your heads up!</h3>
  <div class="row">
    <div class="col-md-6 mx-auto">
      <div class="card">
        <div class="card-body">
          <form @submit.prevent="onSubmit">
            <!-- Name -->
            <div class="mb-3">
              <BaseInput
                  class="form-control"
                  name="hostName"
                  label="Name"
                  :modelValue="meeting.hostName"
                  @input:modelValue="(event) => meeting.hostName = event.target.value"
              />
            </div>
            <!-- Meeting name -->
            <div class="mb-3">
              <BaseInput
                  class="form-control"
                  name="meeting-name"
                  label="Meeting name"
                  :modelValue="meeting.name"
                  @input:modelValue="(event) => meeting.name = event.target.value"
              />
            </div>
            <!-- Date -->
            <div class="mb-3">
              <BaseInput
                  class="form-control"
                  name="meeting-date"
                  label="Date"
                  type="date"
                  :modelValue="meeting.date"
                  @input:modelValue="(event) => meeting.date = event.target.value"
              />
            </div>
            <!-- Time -->
            <div class="mb-3">
              <BaseInput
                  class="form-control"
                  name="meeting-time"
                  label="Time"
                  type="time"
                  min="07:00" max="22:00"
                  :modelValue="meeting.time"
                  @input:modelValue="(event) => meeting.time = event.target.value"
              />
            </div>
            <div class="text-center py-3">
              <BaseButton
                  type="submit"
                  class="btn-primary text-center"
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
.card {
  border-radius: 36px;
  padding: 15px 10px;
  }
</style>
