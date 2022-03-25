<script>

import BaseButton from "@/components/UI/BaseButton";
export default {
  name: "MeetingDetails",
  components: {BaseButton},
  computed: {
    getEvent() {
      return this.$store.state.dashboard.eventDetails
    },
  },
  methods: {
    reloadPage() {
      window.location.reload();
    }
  },
  created() {
    this.$store.dispatch('fetchEventDetails', this.$route.params.id);
  },
}
</script>

<template>
  <h3 class="my-4">Event Details</h3>
  <div class="card">
    <div class="card-body">
      <h5 class="card-title">{{getEvent['event result']}}</h5>
      <p>{{getEvent['event result'].created_on}}</p>
      <!-- contact list -->
      <ul class="list-unstyled contacts">
        <li v-for="(rsvp, index) in getEvent.rsvp_list" :key="index" >
          <svg class="rounded-circle p-2 me-3 my-3"
               :class="{ 'bg-danger': rsvp[1] === 'Denied', 'bg-success': rsvp[1] === 'Attending' }"
               xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"
               width="24" height="24">
            <path fill="none" d="M0 0h24v24H0z" />
            <path d="M20 22H4v-2a5 5 0 0 1 5-5h6a5 5 0 0 1 5 5v2zm-8-9a6 6 0 1 1 0-12 6 6 0 0 1 0 12z" />
          </svg>
          <span>{{ rsvp[0] }}</span> <span>{{ rsvp[1] }}</span>
        </li>
      </ul>
      <BaseButton label="refresh"
                  class="btn btn-primary mt-3 py-2 w-75 mx-auto d-block shadow-sm"
                  @click.prevent="reloadPage"
      />
      <router-link to="/dashboard"
                   class="btn btn-back mt-3 py-2 w-75 mx-auto d-block shadow-sm"
      >
        Back to dashboard
      </router-link>
    </div>
  </div>
</template>
