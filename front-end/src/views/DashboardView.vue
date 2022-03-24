<script>
import BaseButton from "@/components/UI/BaseButton";
export default {
  name: "DashboardView",
  components: {BaseButton},
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
      <h3>Your Events</h3>
      <BaseButton
        class="btn-danger text-white"
        label="Logout"
        @click="logout"
      />
      <div class="card">
        <div class="card-body">
          <p>Dinner</p>
          <span>1/5 replied</span>
          <button>Details</button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>
