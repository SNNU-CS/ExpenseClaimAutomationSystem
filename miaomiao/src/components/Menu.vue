<template>
  <v-navigation-drawer v-model="inputValue" app :expand-on-hover="expandOnHover" floating>
    <v-toolbar color="primary" dark>
      <img src="https://cdn.vuetifyjs.com/images/logos/v.png" height="36" />
      <v-toolbar-title class="ml-0 pl-3">
        <span>财务报销系统</span>
      </v-toolbar-title>
    </v-toolbar>

    <v-divider class="mx-3 mb-3" />

    <v-list nav>
      <v-subheader v-if="header">{{ header }}</v-subheader>
      <v-list-item>
        <v-list-item-content>
          <v-img contain src="@/assets/logo.svg" height="80"></v-img>
        </v-list-item-content>
      </v-list-item>
      <v-divider></v-divider>
      <template v-for="(link, i) in links">
        <v-list-item v-if="!link.children" :key="link.to" :to="link.to">
          <v-list-item-action>
            <v-icon>{{ link.icon }}</v-icon>
          </v-list-item-action>
          <v-list-item-title v-text="link.text"></v-list-item-title>
        </v-list-item>
        <v-list-group v-else-if="link.children" :prepend-icon="link.icon" no-action :key="i">
          <template v-slot:activator>
            <v-list-item-title>{{ link.text }}</v-list-item-title>
          </template>
          <v-list-item v-for="child in link.children" :key="child.to" :to="child.to">
            <v-list-item-title v-text="child.text" />
            <v-list-item-action>
              <v-icon v-text="child.icon"></v-icon>
            </v-list-item-action>
          </v-list-item>
        </v-list-group>
      </template>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
export default {
  props: {
    opened: {
      type: Boolean,
      default: false
    },
    drawer: {
      type: Boolean,
      default: false
    }
  },
  data() {
    return {
      expandOnHover: this.drawer,
      header: "ECAS",
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
          icon: "mdi-settings",
          text: "系统管理",
          children: [
            {
              to: "/account/user",
              icon: "mdi-account",
              text: "用户管理"
            },
            {
              to: "/account/role",
              icon: "mdi-account-multiple",
              text: "角色管理"
            }
          ]
        },
        {
          icon: "mdi-settings",
          text: "工作流管理",
          children: [
            {
              to: "/workflow/manage",
              icon: "mdi-network",
              text: "工作流配置"
            },
            {
              to: "/workflow/config",
              icon: "mdi-account-multiple",
              text: "状态配置"
            },
            {
              to: "/workflow/config",
              icon: "mdi-account-multiple",
              text: "流转配置"
            },
            {
              to: "/workflow/config",
              icon: "mdi-account-multiple",
              text: "自定义字段配置"
            }
          ]
        }
      ],
      inputValue: "/"
    };
  },
  computed: {},
  methods: {},
  watch: {
    drawer(val) {
      this.expandOnHover = val;
    }
  }
};
</script>
