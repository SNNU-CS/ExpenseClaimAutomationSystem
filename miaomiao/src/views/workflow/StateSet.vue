<template>
  <v-card>
      <v-card-title>
          <v-btn color="info" @click="addState">新增状态</v-btn>
          <v-spacer></v-spacer>
          <v-spacer></v-spacer>
          <v-spacer></v-spacer>
          <v-text-field v-model="search" append-icon="mdi-magnify" label="搜索" single-line hide-details></v-text-field>
      </v-card-title>
      <v-card-text>
          <v-data-table :headers="headers" :items="states" sort-by="id" :search="search" :loading="loading">
          
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
        { text: "名称", value: "name" },
        { text: "状态顺序", value: "order" },
        { text: "状态类型", value: "state_type" },
        { text: "工作流", value: "workflow" },
        { text: "子工作流", value: "sub_workflow"},
        { text: "分配方式", value: "distribute_type" },
        { text: "创建人", value: "creator" },
        { text: "创建时间", value: "created" },
        { text: "更新时间", value: "modified" },
        { text: "参与者类型", value: "participant_type" },
        { text: "参与者", value: "participant" },
        { text: "表单字段", value: "state_field_str" },
        ],
      states:[],
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
      this.$api.ListState().then(function(response){
        self.loading = false;
        self.states = response.result;
      });
    }
  },
  addState() {
    this.$router.push("workflow/newstate");
  },

}
</script>

<style>

</style>