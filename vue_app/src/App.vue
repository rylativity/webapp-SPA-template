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

      <v-btn @click="keycloak.logout()">
        <span class="mr-2">Logout</span>
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
        <v-list-item-group>
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
      <v-container>
        <v-card>
          <v-btn @click="getProtectedResource()">
            <span class="mr-2">Make Protected API Call</span>
          </v-btn>
          <v-card-title>Protect API Call Result</v-card-title>
          <v-card-text>{{ protectedApiData }}</v-card-text>
        </v-card>
      </v-container>
      <v-container>
        <v-card>
          <v-card-title>Access Token</v-card-title>
          <v-card-text>{{ keycloak.token }}</v-card-text>
        </v-card>
        <v-card>
          <v-card-title>Id Token</v-card-title>
          <v-card-text>{{ keycloak.idToken }}</v-card-text>
        </v-card>
      </v-container>
      <br>
      <v-container>
        <h2>Proxy Headers</h2>
        <v-card v-for="(headerVal, headerName) in headers" :key="headerName">
          <v-card-title>{{ headerName }}</v-card-title>
          <v-card-text>{{ headerVal }}</v-card-text>
        </v-card>
      </v-container>
      <!-- <iframe :src="sourceUrl" height="100%" width="100%"></iframe> -->

    </v-main>
  </v-app>
</template>

<script>

export default {
  name: 'App',
  props:['keycloak'],
  data: () => ({
    drawer: false,
    sources: {
      flaskapi: 'https://localhost/api/hello',
    },
    headers: {},
    protectedApiData:{"Result":"Not Clicked"}
  }),
  methods: {
    getProtectedResource() {
      let endpoint = `/api/protected`;
      this.$http.get(endpoint, {headers:{
        Authorization: `Bearer ${this.keycloak.token}`
      }}).then((response) => {
        this.protectedApiData = response.data
      }).catch(() => {
        this.protectedApiData = {"Result":"Failed to Fetch Protected Resource"}
      })
    }
  },
  created() {
    let endpoint = `/api/headers`;
    this.$http.get(endpoint).then((response) => {
      this.headers = response.data
    })
  }
}
</script>
<style scoped>
  a {
    text-decoration: none !important;
}
</style>
