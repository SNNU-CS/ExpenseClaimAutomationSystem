<template>
  <v-app-bar app dark color="primary">
    <!-- <v-app-bar-nav-icon></v-app-bar-nav-icon> -->

    <v-spacer></v-spacer>
    <v-btn text href="mailto:zhaoqi99@outlook.com">联系作者</v-btn>
    <v-btn icon href="https://github.com/snnucs/ExpenseClaimAutomationSystem">
      <v-icon class="fa-2x">mdi-github-circle</v-icon>
    </v-btn>
    <v-btn icon text>
      <v-badge color="red" overlap>
        <template v-slot:badge>
          <span v-if="notificationsCount">{{notificationsCount}}</span>
        </template>
        <v-icon>mdi-bell</v-icon>
      </v-badge>
    </v-btn>
    <v-menu offset-y origin="center center" :nudge-bottom="10" transition="scale-transition">
      <template v-slot:activator="{ on }">
        <v-btn icon v-on="on">
          <v-avatar size="40px">
            <v-img :src="avatar"></v-img>
          </v-avatar>
        </v-btn>
      </template>
      <v-list flat>
        <v-list-item-group>
          <v-list-item v-for="(item, index) in items" @click="item.click" :key="index">
            <v-list-item-icon>
              <v-icon v-text="item.icon"></v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title v-text="item.title"></v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-menu>
  </v-app-bar>
</template>
<script>
export default {
  name: "Toolbar",
  data() {
    return {
      avatar: "https://cdn.vuetifyjs.com/images/john.jpg",
      notificationsCount: 1, // change to 0 in the future
      items: [
        {
          icon: "mdi-account-circle",
          title: "个人信息",
          click: this.handleProfile
        },
        {
          icon: "mdi-settings",
          title: "设置",
          click: this.handleSetting
        },
        {
          icon: "mdi-logout",
          title: "退出",
          click: this.handleLogut
        }
      ]
    };
  },
  methods: {
    handleLogut() {
      this.$message.info("用户"+localStorage.username + "退出登录!");
      this.$router.push("/login");
    },
    handleSetting() {},
    handleProfile() {}
  }
};
</script>

<style></style>