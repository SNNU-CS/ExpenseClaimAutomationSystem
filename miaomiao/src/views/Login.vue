<template>
  <v-app id="inspire">
    <v-content>
      <v-container class="fill-height" fluid>
        <v-row align="center" justify="center">
          <v-col cols="12" sm="8" md="4">
            <v-card class="elevation-12">
              <v-toolbar color="primary" dark flat>
                <v-toolbar-title>系统登录</v-toolbar-title>
                <v-spacer />
              </v-toolbar>
              <v-card-text>
                <v-form ref="form">
                  <v-text-field
                    label="用户名"
                    v-model="username"
                    :rules="nameRules"
                    prepend-icon="mdi-account"
                    type="text"
                  />

                  <v-text-field
                    v-model="password"
                    label="密码"
                    :rules="passwordRules"
                    prepend-icon="mdi-lock"
                    type="password"
                  />
                </v-form>
              </v-card-text>
              <v-card-actions>
                <v-spacer />
                <v-btn @click="login()" color="primary">登录</v-btn>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import api from "../api/auth";
import router from "../router";
export default {
  name: "Login",
  data: () => ({
    username: "",
    password: "",
    nameRules: [
      v => !!v || "用户名是必填项",
      v => (v && v.length <= 10) || "用户名长度不能超过10字符"
    ],
    passwordRules: [v => !!v || "密码是必填项"]
  }),
  methods: {
    login() {
      let self = this;
      let parms = {
        username: this.username,
        password: this.password
      };
      if (this.$refs.form.validate()) {
        api.Login(parms).then(function(response) {
          if (response.status === 200) {
            let result = response.result;
            localStorage.Token = result.token;
            localStorage.username = result.username;
            let name = result.user.last_name + result.user.first_name;
            self.$message.success(
              "登录成功!欢迎回来," +
                result.user.organization +
                "的" +
                name +
                "!"
            );
            router.push("main");
          } else if (response.status === 1003) {
            self.$message.error("当前用户不存在!");
          } else if (response.status === 1004) {
            self.$message.error("用户名/密码错误,请重新输入!");
          }
        });
      }
    }
  }
};
</script>