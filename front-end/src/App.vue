<script setup>
import TheFooter from "@/components/TheFooter";
import TheHeader from "@/components/TheHeader";
</script>

<template>
  <TheHeader />
  <div class="container">
    <router-view />
  </div>
  <TheFooter />
</template>

<style lang="scss">
#app {
  height : 100vh;
  }

.card {
  padding: 15px 10px;
  background:
  linear-gradient(white, white) padding-box,
  linear-gradient(180deg, $color-secondary 0%, $color-primary 100%) border-box !important;
  }
.btn-back {
  background-color: #f0f0f0;
  }

</style>
