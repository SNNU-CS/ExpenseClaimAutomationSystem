<template>
  <v-card>
    <v-card-title>
      <v-btn color="info" @click="addRole()">新增角色</v-btn>
      <v-spacer></v-spacer>
      <v-spacer></v-spacer>
      <v-spacer></v-spacer>
      <v-text-field v-model="search" append-icon="mdi-magnify" label="搜索" single-line hide-details></v-text-field>
    </v-card-title>
    <v-card-text>
      <v-data-table
        :headers="headers"
        :items="roles"
        sort-by="id"
        :loading="loading"
        :search="search"
      >
        <template v-slot:item.action="{ item }">
          <v-icon small color="warning" @click="editRole(item)">mdi-pencil</v-icon>
          <v-icon color="red" small @click="deleteRole(item)">mdi-delete</v-icon>
        </template>
        <template v-slot:item.users="{ item }">
          <v-chip color="info" v-for="(value, index) in item.users" v-bind:key="index">{{ value }}</v-chip>
        </template>
      </v-data-table>
    </v-card-text>
    <edit-role
      :dialog="dialog"
      :role="role"
      :roleId="roleId"
      :ifAdd="ifAdd"
      @listRole="listRole"
      @close="dialog = false"
    ></edit-role>
  </v-card>
</template>

<script>
import EditRole from "./EditRole";
export default {
  name: "Role",
  components: { "edit-role": EditRole },
  data() {
    return {
      roles: [],
      headers: [
        { text: "ID", sortable: true, value: "id" },
        { text: "角色名", value: "name" },
        { text: "描述", value: "description" },
        { text: "用户", value: "users" },
        { text: "操作", value: "action", sortable: false }
      ],
      search: "",
      loading: true,
      role: {},
      roleId: -1,
      ifAdd: true,
      dialog: false
    };
  },
  created() {
    this.listRole();
  },
  methods: {
    listRole() {
      let self = this;
      self.loading = true;
      this.$api.ListRole().then(function(response) {
        self.loading = false;
        self.roles = response.result;
      });
    },
    editRole(item) {
      this.ifAdd = false;
      this.roleId = item.id;
      this.role = Object.assign({}, item);
      this.dialog = true;
    },
    deleteRole(item) {
      let self = this;
      confirm("确定要删除角色'" + item.name + "'吗?") &&
        this.$api.DeleteRole(item.id).then(function(response) {
          self.$message.success("删除角色'" + item.name + "'成功!");
          self.listRole();
        });
    },
    addRole() {
      this.ifAdd = true;
      this.dialog = true;
    }
  }
};
</script>

<style>
</style>