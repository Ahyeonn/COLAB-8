<script setup>
  import TheFooter from "@/components/TheFooter";
  import TheHeader from "@/components/TheHeader";
</script>

<template>
  <TheHeader />
  <router-view/>
  <TheFooter />
</template>

<style lang="scss">
  #app {
      height: 100%;
    }
</style>
