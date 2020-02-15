<template>
  <v-card>
    <v-card-title>
      <v-btn color="info" @click="addTran">新增流转</v-btn>
      <v-spacer></v-spacer>
      <v-spacer></v-spacer>
      <v-spacer></v-spacer>
      <v-text-field v-model="search" append-icon="mdi-magnify" label="搜索" single-line hide-details></v-text-field>
    </v-card-title>
    <v-card-text>
      <v-data-table :headers="headers" :items="trans" sort-by="id" :search="search" :loading="loading">
        <template v-slot:item.action="{ item }">
          <v-icon color="red" small @click="deleteTran(item)">mdi-delete</v-icon>
        </template>
      </v-data-table>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  name: "TranSet",
  data() {
    return {
      headers: [
        { text: "ID", sortable: true, value: "id" },
        { text: "操作名称", value: "name" },
        { text: "工作流", value: "workflow" },
        { text: "流转类型", value: "transition_type" },
        { text: "源状态", value: "source_state.name" },
        { text: "目的状态", value: "destination_state.name" },
        { text: "创建人", value: "creator" },
        { text: "创建时间", value: "created" },
        { text: "更新时间", value: "modified" },
        { text: "属性类型", value: "attribute_type" },
        { text: "操作", value: "action", sortable: false }
      ],
      trans: [],
      search: "",
      tran: {},
      loading: true,
      workflowId: this.$route.params.id
    };
  },
  mounted() {
    this.listTran();
  },
  methods: {
    listTran() {
      let self = this;
      self.loading = true;
      this.$api.ListTran(this.workflowId).then(function(response) {
        self.loading = false;
        self.trans = response.result;
      });
    },

    deleteTran(item) {
      let self = this;
      const index = this.trans.indexOf(item);
      confirm("确定要删除流转'" + item.name + "'吗?") &&
        this.$api.DeleteTran(item.id).then(function(response) {
          self.$message.success("删除流转'" + item.name + "'成功!");
          self.listTran();
        });
    },
    addTran() {
      this.$router.push("/workflow/" + this.workflowId + "/trans/new");
    }
  }
};
</script>

<style></style>
