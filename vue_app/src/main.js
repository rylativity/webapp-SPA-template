import Vue from 'vue';
import App from './App.vue';
import router from './router';
import vuetify from './plugins/vuetify';
import axios from "axios";
import VueLogger from 'vuejs-logger';
import Keycloak from 'keycloak-js';

Vue.config.productionTip = false;

Vue.use(VueLogger);

let keycloakInitOptions = {
  url: 'https://localhost/auth', realm: 'master', clientId: 'vue-app', onLoad: 'login-required'
}

let keycloak = Keycloak(keycloakInitOptions);
keycloak.createLogoutUrl = function(options) {
  return keycloak.endpoints.logout()
      + '?id_token_hint=' + keycloak.idToken
      + '&post_logout_redirect_uri=' + encodeURIComponent(window.location.href);
}

axios.defaults.headers["Content-type"] = "application/json";
axios.interceptors.request.use(function (config) {
  config.headers.Authorization = `Bearer ${keycloak.token}`
  return config;
});
Vue.prototype.$http = axios;

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
  }, 30000)
}).catch(() => {
  Vue.$log.error('Authentication Failed');
})


