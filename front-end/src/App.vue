<script setup>
  import TheFooter from "@/components/TheFooter";
  import TheHeader from "@/components/TheHeader";
</script>

<template>
  <TheHeader />
  <div class="container">
    <router-view/>
  </div>
  <TheFooter />
</template>

<style lang="scss">
  #app {
      height: 100%;
    }
</style>
