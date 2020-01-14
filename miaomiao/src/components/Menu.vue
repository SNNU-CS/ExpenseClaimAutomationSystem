<template>
  <v-navigation-drawer
    id="app-drawer"
    v-model="inputValue"
    app
    color="grey darken-2"
    dark
    floating
    mobile-break-point="991"
    persistent
    width="260"
  >
    <template v-slot:img="attrs">
      <v-img v-bind="attrs" gradient="to top, rgba(0, 0, 0, .7), rgba(0, 0, 0, .7)" />
    </template>

    <v-list-item two-line>
      <v-list-item-avatar color="white">
        <v-img src="https://cdn.vuetifyjs.com/images/logos/v.png" height="34" contain />
      </v-list-item-avatar>

      <v-list-item-title class="title">财务报销系统</v-list-item-title>
    </v-list-item>

    <v-divider class="mx-3 mb-3" />

    <v-list nav>
      <!-- Bug in Vuetify for first child of v-list not receiving proper border-radius -->
      <div />

      <v-list-item
        v-for="(link, i) in links"
        :key="i"
        :to="link.to"
        active-class="primary white--text"
      >
        <v-list-item-action>
          <v-icon>{{ link.icon }}</v-icon>
        </v-list-item-action>

        <v-list-item-title v-text="link.text" />
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
export default {
  props: {
    opened: {
      type: Boolean,
      default: false
    }
  },
  data: () => ({
    links: [
      {
        to: "/login",
        icon: "mdi-view-dashboard",
        text: "测试登录"
      },
      {
        to: "/dashboard",
        icon: "mdi-view-dashboard",
        text: "仪表盘"
      },
      {
        to: "/account/user",
        icon: "mdi-account",
        text: "用户管理"
      },
      {
        to: "/account/role",
        icon: "mdi-account-multiple",
        text: "角色管理"
      },
      {
        to: "/main/table-list",
        icon: "mdi-clipboard-outline",
        text: "Table List"
      },
      {
        to: "/main//typography",
        icon: "mdi-format-font",
        text: "Typography"
      },
      {
        to: "/main/icons",
        icon: "mdi-chart-bubble",
        text: "Icons"
      },
      {
        to: "/main/maps",
        icon: "mdi-map-marker",
        text: "Maps"
      },
      {
        to: "/main/notifications",
        icon: "mdi-bell",
        text: "Notifications"
      }
    ],
    inputValue: "/"
  }),

  computed: {},

  methods: {}
};
</script>
