<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light" :class="{ 'round-nav': isVisible }">
    <div class="container-fluid">
      <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarToggler"
          aria-controls="navbarToggler"
          aria-expanded="false"
          aria-label="Toggle navigation"
          @click="toggleNavbar"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <a class="navbar-brand" href="#">Navbar</a>
      <div class="break flex-grow-1"></div>
      <img class="img-fluid rounded-circle" src="@/assets/user.jpg" alt="User profile image">
      <div class="collapse navbar-collapse" :class="{ show: isVisible }" id="navbarToggler">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <router-link class="nav-link" to="/">Home</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/how-it-works">How it works</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/log-in">Log in</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/sign-in">Sign in</router-link>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "TheHeader",
  data() {
    return {
      isVisible: false
    }
  },
  methods: {
    toggleNavbar() {
      this.isVisible = !this.isVisible;
    }
  }
}
</script>

<style scoped lang="scss">
@import "src/scss/utilities/variables";

nav {
  color : $white;
  }

.round-nav, .show {
  border-bottom-left-radius  : 30px;
  border-bottom-right-radius : 30px;
  }

.show {
  background : white;
  margin     : 5px -12px -10px !important;
  padding    : 0 20px;
  box-shadow : 0 3px 10px rgba(0, 0, 0, .3);
  }

.nav-item:not(:last-child) {
  border-bottom : 1px solid $color-secondary;
  }

img {
  aspect-ratio : 1/1;
  width        : 42px;
  height       : 42px;
  }
</style>
