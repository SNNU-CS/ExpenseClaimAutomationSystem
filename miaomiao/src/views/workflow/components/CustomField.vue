<template>
  <v-card>
    <v-card-title>
      <v-btn color="info" @click="addDIY">新增自定义项</v-btn>
      <v-spacer></v-spacer>
      <v-spacer></v-spacer>
      <v-spacer></v-spacer>
      <v-text-field v-model="search" append-icon="mdi-magnify" label="搜索" single-line hide-details></v-text-field>
    </v-card-title>
    <v-card-text>
      <v-data-table :headers="headers" :items="diys" sort-by="id" :search="search" :loading="loading">
        <template v-slot:item.action="{ item }">
          <v-icon color="red" small @click="deleteDIY(item)">mdi-delete</v-icon>
        </template>
        <template v-slot:item.required="{ item }">
          <v-icon color="success" v-if="item.required">mdi-check-circle-outline</v-icon>
          <v-icon color="red" v-else>mdi-cancel</v-icon>
        </template>
      </v-data-table>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  name: "DIYSet",
  data() {
    return {
      headers: [
        { text: "ID", sortable: true, value: "id" },
        { text: "工作流", value: "workflow" },
        { text: "类型", value: "field_type" },
        { text: "字段标识", value: "field_key" },
        { text: "字段名称", value: "field_name" },
        { text: "排序", value: "order" },
        { text: "是否是必填项", value: "required" },
        { text: "创建人", value: "creator" },
        { text: "创建时间", value: "created" },
        { text: "更新时间", value: "modified" },
        { text: "操作", value: "action", sortable: false }
      ],
      diys: [],
      search: "",
      diy: {},
      loading: true,
      workflowId: this.$route.params.id
    };
  },
  mounted() {
    this.listDIY();
  },
  methods: {
    listDIY() {
      let self = this;
      self.loading = true;
      this.$api.ListWorkflowFields(this.workflowId).then(function(response) {
        self.loading = false;
        self.diys = response.result;
      });
    },
    deleteDIY(item) {
      let self = this;
      const index = this.diys.indexOf(item);
      confirm("确定要删除自定义项'" + item.field_name + "'吗?") &&
        this.$api.DeleteDIY(item.id).then(function(response) {
          self.$message.success("删除自定义项'" + item.field_name + "'成功!");
          self.listDIY();
        });
    },
    addDIY() {
      this.$router.push("/workflow/" + this.workflowId + "/fields/new");
    }
  }
};
</script>

<style></style>
