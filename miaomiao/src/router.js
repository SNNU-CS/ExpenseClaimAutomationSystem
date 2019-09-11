import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home'
import Main from './components/Main'
import Login from './components/Login'
import DashBoard from './components/DashBoard'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      redirect: '/main'
    },
    {
      path: '/main',
      component: Main,
      children: [
        {
          path: 'test',
          component: Home
        },
        {
          path: 'dashboard',
          component: DashBoard
        }
      ]
    },
    {
      path: '/login',
      component: Login
    }
  ]
})
