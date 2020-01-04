<template>
  <v-dialog v-model="myDialog" scrollable persistent max-width="40%" transition="dialog-transition">
    <v-card>
      <v-card-title>
        <span class="headline">{{formTitle}}</span>
      </v-card-title>

      <v-card-text>
        <v-form ref="form" v-model="form">
          <v-col>
            <v-row cols="12" sm="6" md="4">
              <v-text-field
                placeholder="username"
                :disabled="!ifAdd"
                v-model="editedUser.username"
                label="用户名"
              ></v-text-field>
              <v-text-field
                dense
                v-if="ifAdd"
                placeholder="A-Z 0-9 a-z"
                v-model="editedUser.password"
                label="密码"
                :append-icon="showPwd ? 'mdi-eye' : 'mdi-eye-off'"
                :type="showPwd ? 'text' : 'password'"
                @click:append="showPwd = !showPwd"
              ></v-text-field>
            </v-row>
            <v-row cols="12" sm="6" md="4">
              <v-text-field v-model="editedUser.last_name" label="姓氏" placeholder="张"></v-text-field>
              <v-text-field v-model="editedUser.first_name" label="名字" placeholder="三"></v-text-field>
              <v-radio-group label="性别" v-model="editedUser.sex" row>
                <v-radio
                  v-for="item in sexChoices"
                  :key="item.key"
                  :label="item.value"
                  :value="item.key"
                ></v-radio>
              </v-radio-group>
            </v-row>
            <v-row cols="12" sm="6" md="4">
              <v-text-field v-model="editedUser.email" label="邮箱" placeholder="xxx@xx.com"></v-text-field>
              <v-select
                v-model="editedUser.organization"
                item-text="org_name"
                item-value="id"
                :items="orgsList"
                label="学院"
                @focus="getOrgs()"
              ></v-select>
            </v-row>
            <v-row cols="12" sm="6" md="4">
              <v-autocomplete
                v-model="editedUser.roles"
                :items="rolesList"
                chips
                multiple
                label="角色"
                item-text="name"
                item-value="id"
                @focus="getRoles()"
              ></v-autocomplete>
            </v-row>
            <v-row cols="12" sm="6" md="4">
              <v-checkbox v-model="editedUser.is_active" label="是否禁用"></v-checkbox>
            </v-row>
          </v-col>
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
        sex: "M",
        email: "",
        roles: [],
        organization: null,
        password: ""
      },
      myDialog: this.dialog,
      form: "",
      orgsList: [],
      rolesList: [],
      showPwd: false,
      sexChoices: [{ key: "M", value: "男" }, { key: "F", value: "女" }]
    };
  },
  created() {
    this.editedUser = Object.assign({}, this.defaultUser);
  },
  mounted() {
    this.getOrgs();
    this.getRoles();
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
      if (this.$refs.form.validate()) {
        if (!this.ifAdd) {
          this.$api
            .UpdateUser(this.userId, this.editedUser)
            .then(function(response) {
              self.$message.success(
                "编辑用户'" + response.result.username + "'成功!"
              );
              self.$emit("listUser");
              self.close();
            });
        } else {
          this.$api.CreateUser(this.editedUser).then(function(response) {
            self.$message.success(
              "新增用户'" + response.result.username + "'成功!"
            );
            self.$emit("listUser");
            self.close();
          });
        }
      }
    },
    close() {
      this.editedUser = Object.assign({}, this.defaultUser);
      this.myDialog = false;
      this.$emit("close");
    },
    getOrgs() {
      let self = this;
      this.$api.ListOrg().then(function(response) {
        self.orgsList = response.result;
      });
    },
    getRoles() {
      let self = this;
      this.$api.ListRole().then(function(response) {
        self.rolesList = response.result;
      });
    }
  }
};
</script>

<style>
</style>