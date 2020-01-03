<template>
  <v-card>
    <v-card-title>
      <v-btn color="info" @click="addUser">新增用户</v-btn>
      <v-spacer></v-spacer>
      <v-spacer></v-spacer>
      <v-spacer></v-spacer>
      <v-text-field v-model="search" append-icon="mdi-magnify" label="搜索" single-line hide-details></v-text-field>
    </v-card-title>
    <v-card-text>
      <v-data-table :headers="headers" :items="users" sort-by="id" :search="search">
        <template v-slot:item.username="{item}">
          <v-avatar v-if="item.avatar" size="30px">
            <v-img :src="item.avatar"></v-img>
          </v-avatar>
          <span>{{item.username}}</span>
        </template>
        <template v-slot:item.action="{ item }">
          <v-icon small @click="editUser(item)">mdi-pencil</v-icon>
          <v-icon small @click="deleteUser(item)">mdi-delete</v-icon>
        </template>
        <template v-slot:item.roles="{item}">
          <v-chip color="info" v-for="(value,index) in item.roles" v-bind:key="index">{{value}}</v-chip>
        </template>
      </v-data-table>
    </v-card-text>
    <edit-user
      :dialog="dialog"
      :user="user"
      :userId="userId"
      :ifAdd="ifAdd"
      @listUser="listUser"
      @close="dialog = false"
    ></edit-user>
  </v-card>
</template>

<script>
import EditUser from "./EditUser";

export default {
  name: "User",
  components: { "edit-user": EditUser },
  data() {
    return {
      headers: [
        { text: "ID", sortable: true, value: "id" },
        { text: "用户名", value: "username" },
        { text: "姓名", value: "full_name" },
        { text: "学院", value: "organization" },
        { text: "角色", value: "roles" },
        { text: "邮箱", value: "email" },
        { text: "性别", value: "sex" },
        { text: "加入日期", value: "date_joined" },
        { text: "上次登录日期", value: "last_login" },
        { text: "操作", value: "action", sortable: false }
      ],
      users: [],
      search: "",
      ifAdd: true,
      userId: -1,
      dialog: false,
      user: {}
    };
  },
  created() {
    this.listUser();
  },
  methods: {
    listUser() {
      let self = this;
      this.$api.ListUser().then(function(response) {
        self.users = response.result;
      });
    },
    editUser(item) {
      this.ifAdd = false;
      this.userId = item.id;
      this.user = Object.assign({}, item);
      this.dialog = true;
    },
    deleteUser(item) {
      let self = this;
      const index = this.users.indexOf(item);
      confirm("确定要删除用户'" + item.username + "'吗?") &&
        this.$api.DeleteUser(item.id).then(function(response) {
          self.$message.success("删除用户'" + item.username + "'成功!");
          self.listUser();
        });
    },
    addUser() {
      this.ifAdd = true;
      this.dialog = true;
    }
  }
};
</script>

<style>
</style>