import Vue from 'vue'
import Router from 'vue-router'
import Main from './views/Main'
import Login from './views/Login'
import DashBoard from './views/DashBoard'
import User from "./views/account/User.vue"
Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      redirect: '/login'
      // 以后前端加了登录校验,记得把这里改成main
    },
    {
      path: '/main',
      component: Main,
      children: [
        {
          path: 'dashboard',
          component: DashBoard
        },
        {
          path: 'user',
          component: User
        }
      ]
    },
    {
      path: '/login',
      component: Login
    }
  ]
})
