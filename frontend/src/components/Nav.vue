<template>
  <div class="row">
    <nav class="navbar navbar-expand navbar-light bg-light fixed-top d-none d-sm-block">
      <div class="container-fluid">
        <router-link to="/" class="navbar-brand" aria-current="page">Welcome</router-link>
        <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <router-link to="/" class="nav-link">Home</router-link>
          </li>
          <template v-for="item in menu.items" :key="item.ID">
            <template v-if="item.child_items !== undefined">
              <li class="nav-item dropdown">
                <Menu :title="item.title" :menuItems="item.child_items" />
              </li>
            </template>
            <template v-else-if="item.object === 'page' || item.object === 'post'">
              <li class="nav-item">
                <router-link :to="makePath(item)" class="nav-link">{{ item.title }}</router-link>
              </li>
            </template>
          </template>
          <li class="nav-item">
            <router-link to="/blog" class="nav-link">Blog</router-link>
          </li>
          <li class="nav-item">
            <router-link v-show="loggedin" to="/domains" class="nav-link">Domains</router-link>
          </li>
          <li class="nav-item">
            <router-link v-show="loggedin && subscriptionType === 'starter' && !customer_id" to="/subscribe"
              class="nav-link">Subscribe</router-link>
          </li>
          <li class="nav-item">
            <router-link v-show="!loggedin" to="/login" class="nav-link">Log in</router-link>
          </li>
          <li class="nav-item">
            <router-link v-show="!loggedin" to="/register" class="nav-link">Sign Up</router-link>
          </li>
          <li class="nav-item dropdown">
            <a v-show="loggedin" class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button"
              data-bs-toggle="dropdown" aria-expanded="false">
              Menu
            </a>
            <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="navbarDropdown">
              <li>
                <router-link to="/account" class="nav-link">Account</router-link>
                <hr class="dropdown-divider" />
              </li>
              <li>
                <a href="#" @click="logout" class="dropdown-item">Log out</a>
              </li>
            </ul>
          </li>
        </ul>
      </div>
    </nav>
    <nav class="navbar navbar-expand navbar-light bg-light fixed-top d-block d-sm-none">
      <div class="container-fluid">
        <router-link to="/" class="navbar-brand" aria-current="page">Welcome</router-link>
        <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <router-link to="/" class="nav-link">Home</router-link>
          </li>
          <template v-for="item in menu.items" :key="item.ID">
            <template v-if="item.child_items !== undefined">
              <li class="nav-item dropdown">
                <Menu :title="item.title" :menuItems="item.child_items" />
              </li>
            </template>
            <template v-else-if="item.object === 'page' || item.object === 'post'">
              <li class="nav-item">
                <router-link :to="makePath(item)" class="nav-link">{{ item.title }}</router-link>
              </li>
            </template>
          </template>
          <li class="nav-item">
            <router-link to="/blog" class="nav-link">Blog</router-link>
          </li>

          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown"
              aria-expanded="false">
              Menu
            </a>
            <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="navbarDropdown">
              <li class="nav-item">
                <router-link v-show="loggedin" to="/domains" class="nav-link">Domains</router-link>
              </li>
              <li class="nav-item">
                <router-link v-show="loggedin && subscriptionType === 'starter' && !customer_id" to="/subscribe"
                  class="nav-link">Subscribe</router-link>
              </li>
              <li class="nav-item">
                <router-link v-show="!loggedin" to="/login" class="nav-link">Log in</router-link>
              </li>
              <li class="nav-item">
                <router-link v-show="!loggedin" to="/register" class="nav-link">Sign Up</router-link>
              </li>
              <li>
                <router-link v-show="loggedin" to="/account" class="nav-link">Account</router-link>
                <hr class="dropdown-divider" />
              </li>
              <li>
                <a href="#" @click="logout" class="dropdown-item">Log out</a>
              </li>
            </ul>
          </li>
        </ul>
      </div>
    </nav>
  </div>
</template>

<script>
import Menu from "@/components/Menu.vue";

export default {
  name: "Nav",
  components: {
    Menu,
  },
  computed: {
    loggedin() {
      return this.$store.state.auth.access && this.$store.state.auth.access !== "";
    },
    menu() {
      return this.$store.state.primaryMenu;
    },
    subscriptionType() {
      return this.$store.state.auth.user.subscription.subscription_type
    },
    previousSubscriptionType() {
      return this.$store.state.auth.user.subscription.previous_subscription_type
    },
    customerId() {
      return this.$store.state.auth.user.subscription.customer_id
    },
  },
  mounted() {
    this.$store.dispatch("getPrimaryMenu");
  },
  methods: {
    logout(e) {
      e.preventDefault();
      this.$store.dispatch("logout");
      this.$router.push("login");
    },
    makePath(item) {
      return `/${item.object}/${item.slug}`;
    },
  },
};
</script>

<style scoped>
.navbar {
  position: fixed;
  top: 0;
  width: 100%;
}
</style>
