import { createApp } from "vue";
import App from "./App.vue";
import "./registerServiceWorker";
import router from "./router";
import store from "./store";

import "bootstrap-icons/font/bootstrap-icons.scss";
import "windi.css";
import "./assets/scss/index.scss";

createApp(App).use(store).use(router).mount("#app");
