<template>
  <v-container>
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
    checkbox: false
  }),

  methods: {
    login() {
      let parms = {
        username: this.username,
        password: this.password
      };
      api
        .Login(parms)
        .then(function(response) {
          if (response.status === 200) {
          } else {
          }
        })
        .catch();
    }
  }
};
</script>