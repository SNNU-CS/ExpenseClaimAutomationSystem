<template>
  <v-card>
    <v-card-text>
      <v-container fluid>
        <v-row align="left" headers="headers">
          <v-col class="d-flex" cols="12" sm="6">
            <v-select
              :items="subWorkflows"
              label="子工作流"
              item-text="name"
              item-value="id"
              v-model="subWorkflow"
            ></v-select>
          </v-col>

          <v-col class="d-flex" cols="12" sm="6">
            <v-select
              :items="stateTypeList"
              item-text="text"
              item-value="value"
              label="状态类型"
            ></v-select>
          </v-col>

          <v-col class="d-flex" cols="12" sm="6">
            <v-text-field
              label="状态顺序"
              v-model="order"
              type="number"
            ></v-text-field>
          </v-col>

          <v-col class="d-flex" cols="12" sm="6">
            <v-select
              :items="participantTypeList"
              item-text="text"
              item-value="value"
              label="参与者类型"
            ></v-select>
          </v-col>

          <v-col class="d-flex" cols="12" sm="6">
            <v-select
              :items="participant"
              item-value="value"
              label="参与者"
            ></v-select>
          </v-col>
        </v-row>

        <v-row>
          <v-col cols="12" md="6">
            <v-textarea
              outlined
              name="input"
              label="表单字段"
              value=" "
            ></v-textarea>
          </v-col>
        </v-row>
      </v-container>
    </v-card-text>
    <v-card-actions>
      <div class="mx-auto">
        <v-btn color="success" :disabled="loading" @click="handleBtn"
          >提交</v-btn
        >
        <v-btn color="error" @click="close">取消</v-btn>
        <v-btn color="warning" @click="reset">重置</v-btn>
      </div>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  name: "EditWorkflow",
  data: () => ({
    subWorkflows: [],
    subWorkflow:-1,
    stateTypeList: [
      { text: "普通类型", value: "0" },
      { text: "初始状态", value: "1" },
      { text: "结束状态", value: "2" }
    ],
    order: 0,
    participantTypeList: [
      { text: "无处理人", value: "0" },
      { text: "个人", value: "1" },
      { text: "多人", value: "2" },
      { text: "部门", value: "3" },
      { text: "角色", value: "4" },
      { text: "脚本", value: "5" },
      { text: "参与人", value: "6" }
    ],
    participant: [{ value: "creator" }],
    workflowId:this.$route.params.id
  }),
  mounted() {
    this.listWorkflow();
  },
  methods: {
    listWorkflow() {
      let self = this;
      self.loading = true;
      this.$api.ListWorkflow().then(function(response) {
        self.loading = false;
        self.subWorkflows = response.result;
      });
    },
    handleBtn(){
      let parms={
        order: this.order,
        sub_xx:this.subWorkflow
      };
      let self=this;
      this.$api.CreateState(params).then(function(response){
        self.$message.success('状态提交成功');
        self.$router.push("/workflow/manage/" + item.id);
      })
    },
    close(){
       this.$router.back(-1);
    },
    getInitState() {
      let self = this;
      let workflowId = this.workflow.id;
      this.$api
        .GetInitState(workflowId)
        .then(function(response) {
          self.initState = response.result;
          Object.assign(self.newForm, {});
          for (let i = 0; i < self.initState.fields; i++) {
            let item = self.initState.fields[i];
            self.newForm[item.field_key] = item.default_value;
          }
        })
        .catch(function(error) {
          self.workflow = "";
        });
    },
    reset(){
       this.$refs.newForm.reset();
    },
  }
};
</script>

<style></style>
