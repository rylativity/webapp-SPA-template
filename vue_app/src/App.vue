<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
      <div class="d-flex align-center">
        <v-img
          alt="Vuetify Logo"
          class="shrink mr-2"
          contain
          src="https://cdn.vuetifyjs.com/images/logos/vuetify-logo-dark.png"
          transition="scale-transition"
          width="40"
        />

      <v-toolbar-title>My Vue Homepage</v-toolbar-title>
      </div>

      <v-app-bar-nav-icon @click="drawer = true"></v-app-bar-nav-icon>

      <v-spacer></v-spacer>

      <v-btn
        href="https://github.com/vuetifyjs/vuetify/releases/latest"
        target="_blank"
        text
      >
        <span class="mr-2">Latest Release</span>
        <v-icon>mdi-open-in-new</v-icon>
      </v-btn>
    </v-app-bar>
    <v-navigation-drawer
      v-model="drawer"
      absolute
      temporary
    >
      <v-list
        nav
        dense
      >
        <v-list-item-group
          v-model="group"
          active-class="deep-purple--text text--accent-4"
        >

          <v-list-item @click="setSource('flaskapi')">
            <v-list-item-icon>
              <v-icon>mdi-view-dashboard</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Flask Api</v-list-item-title>
          </v-list-item>

           <v-list-item @click="setSource('keycloak')">
            <v-list-item-icon>
              <v-icon>mdi-view-dashboard</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Keycloak</v-list-item-title>
          </v-list-item>

          <a target="_blank" href="https://google.com">
          <v-list-item>
            <v-list-item-icon>
              <v-icon>mdi-fan</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Google New Tab</v-list-item-title>
            <v-icon>mdi-open-in-new</v-icon>
          </v-list-item>
          </a>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
    <v-main>
      <!-- <router-view/> -->
      <!-- <v-container>
        <v-card v-for="(url, name) in sources" :key="name">
          <portal :src="url"></portal>
        </v-card>
      </v-container> -->
      <iframe :src="sourceUrl" height="100%" width="100%"></iframe>

    </v-main>
  </v-app>
</template>

<script>

export default {
  name: 'App',

  data: () => ({
    drawer: false,
    group: null,
    source: 'flaskapi',
    sources: {
      flaskapi: 'https://localhost/hello',
    }
  }),
  computed: {
    sourceUrl () {
      return this.sources[this.source]
    }
  },
  methods: {
    setSource (s) {
      this.source = null
      this.source = s
      this.drawer = false
    }
  }
}
</script>
<style scoped>
  a {
    text-decoration: none !important;
}
</style>
