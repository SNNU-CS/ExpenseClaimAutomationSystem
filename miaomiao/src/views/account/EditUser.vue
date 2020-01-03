<template>
  <v-dialog v-model="myDialog" scrollable persistent max-width="50%" transition="dialog-transition">
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
</template>

<script>
export default {
  props: {
    dialog: {
      type: Boolean,
      required: true
    },
    user: {
      type: Object,
      required: false,
      default: function() {
        return this.defaultUser;
      }
    },
    ifAdd: {
      type: Boolean,
      default: true
    },
    userId: {
      type: Number,
      required: false
    }
  },
  data() {
    return {
      editedUser: {},
      defaultUser: {
        username: "",
        first_name: "",
        last_name: "",
        sex: "",
        email: ""
      },
      myDialog: this.dialog,
      form: ""
    };
  },
  created() {
    this.editedUser = Object.assign({}, this.defaultUser);
  },
  computed: {
    formTitle() {
      return !this.ifAdd ? "编辑用户" : "新增用户";
    }
  },
  watch: {
    dialog(val) {
      this.myDialog = val;
    },
    user(val) {
      this.editedUser = this.user;
    }
  },
  methods: {
    save() {
      let self = this;
      let params = {
        username: this.editedUser.username
      };
      if (this.$refs.form.validate()) {
        if (!this.ifAdd) {
          this.$api.EditUser(this.userId, params).then(function(response) {
            self.$message.success(
              "编辑用户'" + response.result.username + "'成功!"
            );
            self.$emit("listUser");
          });
        } else {
          this.$api.AddUser(params).then(function(response) {
            self.$message.success(
              "新增用户'" + response.result.username + "'成功!"
            );
            self.$emit("listUser");
          });
        }
        this.close();
      }
    },
    close() {
      this.editedUser = Object.assign({}, this.defaultUser);
      this.myDialog = false;
      this.$emit("close");
    }
  }
};
</script>

<style>
</style>