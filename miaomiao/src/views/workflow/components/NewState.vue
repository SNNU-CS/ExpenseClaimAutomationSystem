<template>
  <v-card>
    <v-card-text>
      <v-form v-model="form" ref="form">
        <v-container fluid>
          <v-row>
            <v-col class="d-flex" cols="12" sm="6">
              <v-text-field label="状态名称" :rules="rules.required" v-model="name"></v-text-field>
            </v-col>
            <v-col class="d-flex" cols="12" sm="6">
              <v-select
                :items="subWorkflows"
                label="子工作流"
                item-text="name"
                item-value="id"
                :rules="rules.required"
                v-model="subWorkflow"
              ></v-select>
            </v-col>

            <v-col class="d-flex" cols="12" sm="6">
              <v-select
                :items="stateTypeList"
                placeholder=" "
                item-text="text"
                item-value="value"
                label="状态类型"
                v-model="stateType"
              ></v-select>
            </v-col>

            <v-col class="d-flex" cols="12" sm="6">
              <v-text-field label="状态顺序" :rules="rules.required" v-model="order" type="number"></v-text-field>
            </v-col>

            <v-col class="d-flex" cols="12" sm="6">
              <v-select
                :items="participantTypeList"
                item-text="text"
                item-value="value"
                label="参与者类型"
                v-model="participantType"
              ></v-select>
            </v-col>

            <v-col class="d-flex" cols="12" sm="6">
              <v-select
                :items="users"
                :rules="rules.required"
                item-text="username"
                item-value="id"
                label="参与者"
                v-model="participant"
              ></v-select>
            </v-col>
          </v-row>
        </v-container>
      </v-form>
    </v-card-text>
    <v-card-actions>
      <div class="mx-auto">
        <v-btn color="success" :disabled="loading" @click="handleBtn">提交</v-btn>
        <v-btn color="error" @click="close">取消</v-btn>
        <v-btn color="warning" @click="reset">重置</v-btn>
      </div>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  name: "NewState",
  data() {
    return {
      subWorkflows: [],
      subWorkflow: -1,
      stateTypeList: [
        { text: "普通类型", value: 0 },
        { text: "初始状态", value: 1 },
        { text: "结束状态", value: 2 }
      ],
      stateType: 0,
      order: 1,
      participantTypeList: [
        { text: "无处理人", value: 0 },
        { text: "个人", value: 1 },
        { text: "多人", value: 2 },
        { text: "部门", value: 3 },
        { text: "角色", value: 4 },
        { text: "脚本", value: 5 },
        { text: "参与人", value: 6 }
      ],
      users: [],
      participant: "",
      workflowId: this.$route.params.id,
      loading: false,
      participantType: 0,
      form: "",
      rules: {
        required: [(value) => !!value || "这是一个必填项."]
      },
      name: ""
    };
  },
  mounted() {
    this.listWorkflow();
    this.listUser();
  },
  methods: {
    listWorkflow() {
      let self = this;
      this.$api.ListWorkflow().then(function(response) {
        self.subWorkflows = response.result;
      });
    },
    listUser() {
      let self = this;
      this.$api.ListUser().then(function(response) {
        self.users = response.result;
      });
    },
    handleBtn() {
      let params = {
        order: this.order,
        name: this.name,
        workflow: parseInt(this.workflowId),
        participant: this.participant,
        participant_type: this.participantType,
        state_type: this.stateType
      };
      if (this.subWorkflow !== -1) {
        params["sub_workflow"] = parseInt(this.workflowId);
      }
      let self = this;
      console.log(params);
      if (this.$refs.form.validate()) {
        this.$api.CreateState(params).then(function(response) {
          self.$message.success("状态添加成功!");
          self.$router.push("/workflow/manage/" + self.workflowId);
        });
      }
    },
    close() {
      this.$router.back(-1);
    },
    reset() {
      this.$refs.form.reset();
    }
  }
};
</script>

<style></style>
