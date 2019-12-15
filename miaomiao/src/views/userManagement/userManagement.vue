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
    <v-dialog v-model="dialog" scrollable persistent max-width="50%" transition="dialog-transition">
      <v-card>
        <v-card-title>
          <span class="headline">{{formTitle}}</span>
        </v-card-title>

        <v-card-text>
          <v-form ref="form" v-model="form">
            <v-row>
              <v-col cols="12" sm="6" md="4">
                <v-text-field v-model="editedUser.username" label="用户名"></v-text-field>
              </v-col>
            </v-row>
          </v-form>
        </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="save">保存</v-btn>
          <v-btn color="blue darken-1" text @click="close">取消</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-card>
</template>

<script>
export default {
  name: "UserManagement",
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
      editedUser: null,
      defaultUser: {
        username: "",
        first_name: "",
        last_name: "",
        sex: "",
        email: ""
      },
      dialog: false,
      ifEdit: false,
      form: ""
    };
  },
  created() {
    this.editedUser = Object.assign({}, this.defaultUser);
    this.listUser();
  },
  computed: {
    formTitle() {
      return this.ifEdit ? "编辑用户" : "新增用户";
    }
  },
  methods: {
    listUser() {
      let self = this;
      this.$api.ListUser().then(function(response) {
        if (response.status === 200) {
          self.users = response.result;
        }
      });
    },
    editUser(item) {
      this.ifEdit = true;
      this.editedUser = Object.assign({}, item);
      this.dialog = true;
    },
    close() {
      this.editedUser = Object.assign({}, this.defaultUser);
      this.dialog = false;
    },
    save() {
      let self = this;
      let params = {
        username: this.editedUser.username
      };
      if (this.$refs.form.validate()) {
        if (this.ifEdit) {
          this.$api
            .EditUser(this.editedUser.id, params)
            .then(function(response) {
              if (response.status === 200) {
                self.$message.success(
                  "编辑用户'" + response.result.username + "'成功!"
                );
              }
              self.listUser();
            });
        } else {
          this.$api.AddUser(params).then(function(response) {
            if (response.status === 200) {
              self.$message.success(
                "新增用户'" + response.result.username + "'成功!"
              );
            }
            self.listUser();
          });
        }
        this.close();
      }
    },
    deleteUser(item) {
      let self = this;
      const index = this.users.indexOf(item);
      confirm("确定要删除用户'" + item.username + "'吗?") &&
        this.$api.DeleteUser(item.id).then(function(response) {
          if (response.status === 200) {
            self.$message.success("删除用户'" + item.username + "'成功!");
          }
          self.listUser();
        });
    },
    addUser() {
      this.ifEdit = false;
      this.dialog = true;
    }
  }
};
</script>

<style>
</style>