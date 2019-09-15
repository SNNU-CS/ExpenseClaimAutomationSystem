<template>
  <v-container>
    <v-dialog v-model="dialog" max-width="290">
      <v-card>
        <v-card-title class="headline">66</v-card-title>
        <v-card-text>密码错了</v-card-text>
        <v-card-actions>
          <v-btn color="green darken-1" text @click="dialog = false">确定</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-form ref="form" lazy-validation>
      <v-text-field v-model="username" :counter="10" :rules="nameRules" label="用户名" required></v-text-field>

      <v-text-field v-model="password" label="密码" required></v-text-field>

      <v-select
        v-model="select"
        :items="items"
        :rules="[v => !!v || 'Item is required']"
        label="身份"
        required
      ></v-select>

      <v-checkbox
        v-model="checkbox"
        :rules="[v => !!v || 'You must agree to continue!']"
        label="Do you agree?"
        required
      ></v-checkbox>

      <v-btn color="success" @click="login">登录</v-btn>
    </v-form>
  </v-container>
</template>

<script>
import api from "../fetch/api";
import router from "../router";
export default {
  name: "Login",
  data: () => ({
    username: "",
    nameRules: [
      v => !!v || "Name is required",
      v => (v && v.length <= 10) || "Name must be less than 10 characters"
    ],
    password: "",
    select: null,
    items: ["老师", "学生"],
    checkbox: false,
    dialog: false
  }),

  methods: {
    login() {
      let self = this;
      let parms = {
        username: this.username,
        password: this.password
      };
      api
        .Login(parms)
        .then(function(response) {
          if (response.status === 200) {
            router.push("main");
          } else {
            self.dialog = true;
          }
        })
        .catch();
    }
  }
};
</script>