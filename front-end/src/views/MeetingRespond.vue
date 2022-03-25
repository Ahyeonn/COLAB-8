<script>
import BaseButton from "@/components/UI/BaseButton";
import { mapState } from 'vuex';

export default {
  name: "MeetingRespond.vue",
  data(){
    return {
      submitted: false,
      routeId: this.$route.params.id
    }
  },
  components: {BaseButton},
  computed: {
    ...mapState(['activeMeeting']),
  },
  methods: {
    onClick(value) {
      this.$store.dispatch('sendRespondStatus', [value, this.routeId])
    },
    onSubmit() {
      this.submitted = true
    }
  },
  created() {
    this.$store.dispatch('getMeetingRespound', this.routeId);
  },
}
</script>

<template>
  <template v-if="!submitted">
    <h3 class="my-4 text-md-center">Please let us know if you are still attending!</h3>
    <h4 class="text-center">{{ activeMeeting.event_name }} with {{ activeMeeting.host_name }}</h4>
    <form @submit.prevent="onSubmit" class="d-flex mt-5 justify-content-around">
      <BaseButton @click="() => onClick('true')"  class="btn-success text-white" label="I'm coming" />
      <BaseButton @click="() => onClick('false')" class="btn-danger text-white" label="I can't make it" />
    </form>
  </template>
  <template v-else>
    <h4 class="mt-4">Thank you for your response! You may close this page</h4>
  </template>

</template>

<style scoped>

</style>
