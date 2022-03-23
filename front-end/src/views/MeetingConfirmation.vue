<script>
import BaseButton from "@/components/UI/BaseButton";
import {mapGetters} from 'vuex'

export default {
  name: "MeetingConfirmation",
  components: {BaseButton},
  computed: {
    ...mapGetters(['getContacts', 'getMeeting'])
  },
}
</script>

<template>
  <div class="row">
    <div class="col-md-6 mx-auto">
      <h3 class="my-4"> 🔍 Take a look and confirm your details blow!</h3>
      <section id="message-preview">
        <p class="fw-bold"><span class="step rounded-circle bg-primary text-white">1</span> Message Preview</p>
        <div class="card mb-4">
          <p class="text-center text-muted">HeadsUp!</p>
          <p class="heads-up-message text-white rounded-3 p-3">
            Hey it's {{ getMeeting[0].hostName }}, just sending a HeadsUp! about our {{ getMeeting[0].name }} at {{ getMeeting[0].date }} - {{getMeeting[0].time}}. Let me know if you're coming!
          </p>
          <p class="text-muted text-center">Your friend</p>
          <p class="friend-message rounded-3 p-3">
            Yes, I'll be there!
          </p>
        </div>
      </section>
      <section id="recipients">
        <p class="fw-bold mb-3"><span class="step rounded-circle bg-primary text-white">2</span> Recipients</p>
        <!-- contact list -->
        <ul class="list-unstyled contacts">
          <li v-for="(contacts, index) in getContacts" :key="index">
            <svg class="rounded-circle p-2 me-3 my-3" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"
                 width="24" height="24">
              <path fill="none" d="M0 0h24v24H0z" />
              <path d="M20 22H4v-2a5 5 0 0 1 5-5h6a5 5 0 0 1 5 5v2zm-8-9a6 6 0 1 1 0-12 6 6 0 0 1 0 12z" />
            </svg>
            <span>{{ contacts }}</span>
          </li>
        </ul>
        <div class="text-center">
          <BaseButton class="btn-primary mt-4 py-2 w-75 text-white shadow-sm" label="Send HeadsUp!"/>
          <router-link
              class="btn btn-back mt-3 py-2 w-75 mx-auto d-block shadow-sm"
              to="/contact-info"
          >Go back
          </router-link>
        </div>

      </section>
    </div>
  </div>
</template>

<style scoped lang="scss">
.heads-up-message {
  background: #37D15D;
  margin-left: 30%;
}
.friend-message {
  background: #E9E9EB;
  margin-right: 40%;
  }

.step {
  padding: 5px 10px;
}
</style>
