<template>
  <v-dialog v-model="dialog" persistent max-width="30%" transition="dialog-transition">
    <v-card>
      <v-card-title>
        <span>修改密码</span>
      </v-card-title>
      <v-form ref="form" v-model="form">
        <v-col>
          <v-text-field
            placeholder="新密码（5-12大小写字母、数字）"
            v-model="newPwd"
            label="新密码"
            :rules="rules.newPwd"
            :type="showPwd ? 'text' : 'password'"
            :append-icon="showPwd ? 'mdi-eye' : 'mdi-eye-off'"
            @click:append="showPwd = !showPwd"
          ></v-text-field>
        </v-col>
        <v-col>
          <v-text-field
            placeholder="确认密码（5-12大小写字母、数字）"
            v-model="newPwd2"
            label="确认密码"
            :rules="[(v) => !!v || '请输入确认密码', check]"
            :type="showPwd ? 'text' : 'password'"
            :append-icon="showPwd ? 'mdi-eye' : 'mdi-eye-off'"
            @click:append="showPwd = !showPwd"
          ></v-text-field>
        </v-col>
      </v-form>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="blue darken-1" text @click="confirm">保存</v-btn>
        <v-btn color="blue darken-1" text @click="close">取消</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  methods: {
    close() {
      this.$router.back(-1);
    },
    confirm() {
      if (this.$refs.form.validate()) {
        let params = {
          password: this.newPwd,
          password2: this.newPwd2
        };
        let self = this;
        this.$api.GetSelf().then(function(response) {
          let userId = response.result.id;
          self.$api.SetPassword(userId, params).then(function(response) {
            self.$message.success("密码修改成功,下次登录生效!");
          });
        });
      }
    },
    check() {
      return this.newPwd == this.newPwd2 ? true : "两次输入的密码不一致";
    }
  },
  data() {
    return {
      newPwd: "",
      newPwd2: "",
      dialog: true,
      showPwd: false,
      form: "",
      rules: {
        newPwd: [(v) => !!v || "请输入新密码"]
      }
    };
  }
};
</script>
