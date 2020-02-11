<template>
  <v-card>
    <v-card-title>
      <v-btn color="info" @click="addWorkflow">新增工作流</v-btn>
      <v-spacer></v-spacer>
      <v-spacer></v-spacer>
      <v-spacer></v-spacer>
      <v-text-field v-model="search" append-icon="mdi-magnify" label="搜索" single-line hide-details></v-text-field>
    </v-card-title>
    <v-card-text>
      <v-data-table :headers="headers" :items="workflows" sort-by="id" :search="search" :loading="loading">
        <template v-slot:item.action="{ item }">
          <v-icon small color="warning" @click="editWorkflow(item)">mdi-pencil</v-icon>
          <v-icon color="red" small @click="deleteWorkflow(item)">mdi-delete</v-icon>
        </template>
         <template v-slot:item.flowchart="{ item }">
             <v-btn color="info" @click="see(item)">查看</v-btn>
        </template>
      </v-data-table>
    </v-card-text>
  </v-card>
</template>

<script>


export default {
  name: "Manage",
  components: {  },
  data() {
    return {
      headers: [
        { text: "ID", sortable: true, value: "id" },
        { text: "名称", value: "name" },
        { text: "描述", value: "description" },
        { text: "创建人", value: "creator" },
        { text: "创建时间", value: "created" },
        { text: "操作", value: "action", sortable: false },
        { text: "查看流程图",value: "flowchart"}
      ],
      workflows: [],
      search: "",
      ifAdd: true,
      workflowId: -1,
      dialog: false,
      workflow: {},
      loading: true
    };
  },
  created() {
    this.listWorkflow();
  },
  methods: {
    listWorkflow() {
      let self = this;
      self.loading = true;
      this.$api.ListWorkflow().then(function(response) {
        self.loading = false;
        self.workflows = response.result;
      });
    },
    editWorkflow(item) {
      this.ifAdd = false;
      this.workflowId = item.id;
      this.workflow = Object.assign({}, item);
      let roles_id = [];
      for (let i = 0; i < this.user.roles.length; i++) {
        roles_id.push(this.user.roles[i].id);
      }
      this.user.roles = roles_id;
      this.user.organization = this.user.organization === null ? null : this.user.organization.id;
      this.dialog = true;
    },
    deleteWorkflow(item) {
      let self = this;
      const index = this.workflows.indexOf(item);
      confirm("确定要删除项目'" + item.name + "'吗?") &&
        this.$api.DeleteWorkflow(item.id).then(function(response) {
          self.$message.success("删除项目'" + item.name + "'成功!");
          self.listWorkflow();
        });
    },
  }
}
</script>

<style></style>
