import Vue from 'vue';
import App from './App.vue';
import router from './router';
import vuetify from './plugins/vuetify';
import axios from "axios";
import VueLogger from 'vuejs-logger';
import Keycloak from 'keycloak-js';

Vue.config.productionTip = false;
axios.defaults.headers["Content-type"] = "application/json";
Vue.prototype.$http = axios;
Vue.use(VueLogger);

let keycloakInitOptions = {
  url: 'https://localhost/auth', realm: 'myrealm', clientId: 'vue-app', onLoad: 'login-required'
}

let keycloak = Keycloak(keycloakInitOptions);

keycloak.init({ onLoad: keycloakInitOptions.onLoad }).then((auth) => {
  if (!auth) {
    window.location.reload();
  } else {
    Vue.$log.info("Authenticated");

    new Vue({
      router,
      vuetify,
      render: h => h(App, {props: {keycloak: keycloak}})
    }).$mount('#app')
  }

  //Token Refresh
  setInterval(() => {
    keycloak.updateToken(70).then((refreshed) => {
      if (refreshed) {
        Vue.$log.info('Token refreshed' + refreshed);
      } else {
        Vue.$log.warn('Token not refreshed, valid for ' + 
          Math.round(keycloak.tokenParsed.exp + keycloak.timeSkew - new Date().getTime() / 1000) + ' seconds')
      }
    }).catch(() => {
      Vue.$log.error('Failed to refresh token');
    });
  }, 6000)
}).catch(() => {
  Vue.$log.error('Authentication Failed');
})


