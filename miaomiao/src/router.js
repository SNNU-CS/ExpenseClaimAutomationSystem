import Vue from "vue";
import Router from "vue-router";
import Main from "./views/Main";
import Login from "./views/Login";
import DashBoard from "./views/DashBoard";
import User from "./views/account/User.vue";
import Role from "./views/account/Role.vue";
import Error404 from "./views/error/404.vue";
Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    {
      path: "/",
      component: Main,
      redirect: "/dashboard",
      children: [
        {
          path: "dashboard",
          component: DashBoard
        },
        {
          path: "account/user",
          component: User
        },
        {
          path: "account/role",
          component: Role
        }
      ]
    },
    {
      path: "/login",
      component: Login
    },
    {
      path: "/error/404",
      component: Error404
    },
    {
      path: "*",
      redirect: "/error/404"
    }
  ]
});
