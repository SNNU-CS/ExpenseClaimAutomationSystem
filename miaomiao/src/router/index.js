import Vue from "vue";
import Router from "vue-router";
import Main from "@/views/Main";
import Login from "@/views/Login";
import DashBoard from "@/views/DashBoard";

import account from "./account";
import error from "./error";
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
        ...account
      ]
    },
    {
      path: "/login",
      component: Login
    },
    ...error
  ]
});
