<script>
import BaseButton from "@/components/UI/BaseButton";


export default {
  name: "DashboardView",
  components: {BaseButton},
  computed: {
    getEvents() {
      return this.$store.state.dashboard.events
    }
  },
  methods: {
    async logout() {
      await this.$store.commit('LOG_IN', 'false');
      await this.$router.push({path: '/log-in'});
    }
  }
}
</script>

<template>
  <h3 class="my-4 text-center">Dashboard</h3>
      <BaseButton
          class="btn-danger text-white"
          label="Logout"
          @click="logout"
      />
      <h3 class="my-3">Your Events</h3>
  <div class="row">
    <div class="col-md-6 mx-auto" v-if="!getEvents">
      <p>Oh, you dont have any events yet!</p>
    </div>
    <div class="col" v-for="event in getEvents" :key="event.id" v-else>
      <div class="card text-center">
        <div class="card-body">
          <p>{{ event.event_name }}</p>
          <span>{{ event.num_of_recipients }} members</span>
          <BaseButton
              class="btn-primary d-block mt-2"
              label="Details"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
.card {
  max-width : 300px;
  }
</style>
