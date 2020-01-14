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
              <v-text-field placeholder="admin" v-model="editedRole.name" label="角色名"></v-text-field>
              <v-text-field placeholder="管理员" v-model="editedRole.description" label="描述"></v-text-field>
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
    role: {
      type: Object,
      required: false,
      default: function() {
        return this.defaultRole;
      }
    },
    ifAdd: {
      type: Boolean,
      default: true
    },
    roleId: {
      type: Number,
      required: false
    }
  },
  data() {
    return {
      editedRole: {},
      defaultRole: {
        name: "",
        description: ""
      },
      myDialog: this.dialog,
      form: ""
    };
  },
  computed: {
    formTitle() {
      return !this.ifAdd ? "编辑角色" : "新增角色";
    }
  },
  watch: {
    dialog(val) {
      this.myDialog = val;
    },
    role(val) {
      this.editedRole = val;
    }
  },
  methods: {
    save() {
      let self = this;
      if (this.$refs.form.validate()) {
        if (!this.ifAdd) {
          this.$api
            .UpdateRole(this.roleId, this.editedRole)
            .then(function(response) {
              self.$message.success(
                "编辑角色'" + response.result.name + "'成功!"
              );
            });
          self.$emit("listRole");
          self.close();
        } else {
          this.$api.CreateRole(this.editedRole).then(function(response) {
            self.$message.success(
              "新增角色'" + response.result.name + "'成功!"
            );
            self.$emit("listRole");
            self.close();
          });
        }
      }
    },
    close() {
      this.editedRole = Object.assign({}, this.defaultRole);
      this.myDialog = false;
      this.$emit("close");
    }
  }
};
</script>

<style>
</style>