import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import Home from "../views/Home.vue";

const routes: Array<RouteRecordRaw> = [
  {
    path: "/home",
    name: "Home",
    component: Home,
  },
  {
    path: "/explore",
    name: "Explore",
    component: Home,
  },
  {
    path: "/lists",
    name: "Lists",
    component: Home,
  },
  {
    path: "/bookmarks",
    name: "Bookmarks",
    component: Home,
  },
  {
    path: "/profile",
    name: "Profile",
    component: Home,
  },
  {
    path: "/notifications",
    name: "Notifications",
    component: Home,
  },
  {
    path: "/messages",
    name: "Messages",
    component: Home,
  },
  {
    path: "/signup",
    name: "SignUp",
    component: () => import("../views/SignUp.vue"),
  },
  {
    path: "/login",
    name: "Login",
    component: () => import("../views/Login.vue"),
  },
  {
    path: "/",
    name: "Welcome",
    component: () => import("../views/Welcome.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
