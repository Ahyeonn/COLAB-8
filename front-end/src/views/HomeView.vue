<script setup>
import BaseInput from "@/components/Form/BaseInput";
import BaseButton from "@/components/UI/BaseButton";
</script>

<template>
    <h3 class="mt-3 mb-4"> 👋 Hi there! Let's get started on your heads up!</h3>
    <div class="card">
      <div class="card-body">
        <form>
          <!-- Name -->
          <div class="mb-3">
            <BaseInput
                class="form-control"
                name="name"
                label="Name"
            />
          </div>
          <!-- Meeting name -->
          <div class="mb-3">
            <BaseInput
                class="form-control"
                name="meeting-name"
                label="Meeting name"
            />
          </div>
          <!-- Date -->
          <div class="mb-3">
            <BaseInput
                class="form-control"
                name="meeting-name"
                label="Meeting name"
                type="date"
            />
          </div>
          <!-- Time -->
          <div class="mb-3">
            <BaseInput
                class="form-control"
                name="meeting-name"
                label="Meeting name"
                type="time"
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
</template>

<style scoped lang="scss">
.card {
    border-radius: 36px;
    padding: 15px 10px;
  }
</style>
