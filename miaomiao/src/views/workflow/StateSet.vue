<template>
  <v-card>
    <v-card-title>
      <!-- <v-btn color="info" @click="addState">新增状态</v-btn> -->
      <v-spacer></v-spacer>
      <v-spacer></v-spacer>
      <v-spacer></v-spacer>
      <v-text-field v-model="search" append-icon="mdi-magnify" label="搜索" single-line hide-details></v-text-field>
    </v-card-title>
    <v-card-text>
      <v-data-table :headers="headers" :items="states" sort-by="id" :search="search" :loading="loading">
        <template v-slot:item.action="{ item }">
          <v-icon small color="warning" @click="editState(item)">mdi-pencil</v-icon>
          <v-icon color="red" small @click="deleteState(item)">mdi-delete</v-icon>
        </template>
      </v-data-table>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  name: "StateSet",
  components: {},
  data() {
    return {
      headers: [
        { text: "ID", sortable: true, value: "id" },
        { text: "工作流", value: "workflow" },
        { text: "子工作流", value: "sub_workflow" },
        { text: "名称", value: "name" },
        { text: "状态类型", value: "state_type" },
        { text: "状态顺序", value: "order" },
        { text: "分配方式", value: "distribute_type" },
        { text: "参与者类型", value: "participant_type" },
        { text: "创建人", value: "creator" },
        { text: "参与者", value: "participant" },
        { text: "创建时间", value: "created" },
        { text: "更新时间", value: "modified" },
        { text: "表单字段", value: "state_field_str" },
        { text: "操作", value: "action", sortable: false }
      ],
      states: [],
      search: "",
      state: {},
      loading: true
    };
  },
  mounted() {
    this.listState();
  },
  methods: {
    listState() {
      let self = this;
      self.loading = true;
      this.$api.ListState().then(function(response) {
        self.loading = false;
        self.states = response.result;
      });
    },
    editState(item) {
      // this.$router.push("/workflow/")
    },
    deleteState(item) {
      let self = this;
      const index = this.states.indexOf(item);
      confirm("确定要删除状态'" + item.name + "'吗?") &&
        this.$api.DeleteState(item.id).then(function(response) {
          self.$message.success("删除状态'" + item.name + "'成功!");
          self.listState();
        });
    }
    // addState() {
    //   this.$router.push("workflow/newstate");
    // }
  }
};
</script>

<style></style>
