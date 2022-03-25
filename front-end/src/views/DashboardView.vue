<script>
import BaseButton from "@/components/UI/BaseButton";

export default {
  name: "DashboardView",
  components: {BaseButton},
  computed: {
    getEvents() {
      return this.$store.state.dashboard.events
    },
    getAuthenticatedUser() {
      return this.$store.state.auth.authenticatedUser
    }
  },
  methods: {
    async logout() {
      await this.$store.commit('LOG_IN', 'false');
      await localStorage.setItem('user_id', null);
      await localStorage.setItem('user_name', null);
      await this.$router.push({path: '/log-in'});
    },
    detail(id) {
      this.$router.push({path: `/dashboard/events/${id}`});
    }
  }
}
</script>

<template>
  <h3 class="my-4 text-center">
    👋 Welcome back
    <span class=" text-capitalize">{{ getAuthenticatedUser.name }}!</span>
  </h3>
      <h3 class="my-3">Your Events</h3>
  <div class="row">
    <div class="col-md-6 mx-auto" v-if="!getEvents">
      <p>Oh, you dont have any events yet!</p>
    </div>
    <div class="col" v-for="event in getEvents" :key="event.id" v-else>
      <div class="card text-center">
        <div class="card-body">
          <p>{{ event.event_name }}</p>
          <BaseButton
              class="btn-primary shadow-sm d-block mt-2 d-block mx-auto"
              label="Details"
              @click.prevent="detail(event.event_id)"
          />
        </div>
      </div>
    </div>
  </div>
  <BaseButton
      class="btn-danger d-block text-white shadow-sm mt-5"
      label="Logout"
      @click="logout"
  />
</template>

<style scoped lang="scss">
.card {
  max-width : 300px;
  }
</style>
