<script>
import BaseButton from "@/components/UI/BaseButton";


export default {
  name: "DashboardView",
  components: {BaseButton},
  created() {
    // this.$store.dispatch('getEvents');

  },
  computed: {
    getEvents() {
      const events = this.$store.state.dashboard.events
      return events.map(event =>{
        return event
      });
    }
  },
  methods: {
    async logout() {
      await this.$store.commit('LOG_IN', 'false');
      await this.$router.push({ path : '/log-in' });
    }
  }
}
</script>

<template>
  <h3 class="my-4 text-center">Dashboard</h3>
  <div class="row">
    <div class="col-md-6">
      <BaseButton
          class="btn-danger text-white"
          label="Logout"
          @click="logout"
      />
      <h3>Your Events</h3>
      {{getEvents}}
      <div class="row">
        <div class="col">
          <template v-for="event in getEvents" :key="event.id">
            <p>{{event.event_name}}</p>
            <div class="card">
              <div class="card-body">
                <BaseButton
                    class="btn-primary d-block mt-2"
                    label="Details"
                />
              </div>
            </div>
          </template>

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
