<template>
  <v-card>
    <v-card-text>
      <v-container fluid>
        <v-row>
          <v-col class="d-flex" cols="12" sm="6">
            <v-select
                 :items="users"
                :rules="rules.required"
                item-text="username"
                item-value="id"
                label="创建人"
                v-model="people"
            ></v-select>
          </v-col>

          <v-col cols="12" sm="6" md="3">
          <v-text-field
            label="操作名称"
            placeholder=""
          ></v-text-field>
          </v-col>
    
          <v-col class="d-flex" cols="12" sm="6">
              <v-select
                :items="Workflows"
                label="工作流"
                item-text="name"
                item-value="id"
                :rules="rules.required"
                v-model="Workflow"
              ></v-select>
          </v-col>

          <v-col class="d-flex" cols="12" sm="6">
              <v-select
                :items="tranTypeList"
                placeholder="常规流转"
                item-text="text"
                item-value="value"
                label="流转类型"
                v-model="tranType"
              ></v-select>
          </v-col>

          <v-col class="d-flex" cols="12" sm="6">
              <v-text-field label="定时器" :rules="rules.required" v-model="order" type="number"></v-text-field>
          </v-col>


           <v-col class="d-flex" cols="12" sm="6">
            <v-select
              :items="SourceStates"
              item-text="name"
              item-value="value"
              label="源状态"
              :rules="rules.required"
              v-model="SourceState"            
            ></v-select>
          </v-col>

           <v-col class="d-flex" cols="12" sm="6">
            <v-select
              :items="SourceStates"
              item-value="value"
              item-text="name"
              label="目的状态"
            ></v-select>
          </v-col>




          <v-col class="d-flex" cols="12" sm="6">
              <v-select
                :items="attrTypeList"
                placeholder="同意"
                item-text="text"
                item-value="value"
                label="属性类型"
                v-model="attrType"
              ></v-select>
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
  name: "NewTran",
  data() {
    return {
      users: [],
      Workflows: [],
      Workflow: -1,
      SourceStates: [],
      SourceState: -1,
      name: "",
      tranTypeList: [
        { text: "常规流转", value: 0 },
        { text: "定时器流转", value: 1 },
      ],
      tranType: 0,
      order: 0,
      attrTypeList: [
        { text: "同意", value: 0 },
        { text: "拒绝", value: 1 },
        { text: "其他", value: 2 },
      ],
      attrType: 0,
      people: "",
      workflowId: this.$route.params.id,
      loading: false,
      form: "",
      rules: {
        required: [(value) => !!value || "这是一个必填项."]
      },
     
    };
  },
  mounted() {
    this.listStates();
    this.listUser();
    this.listWorkflow();
  },
  methods: {
    listWorkflow() {
      let self = this;
      this.$api.ListWorkflow().then(function(response) {
        self.Workflows = response.result;
      });
    },
    listStates() {
      let self = this;
      this.$api.ListWorkflowState().then(function(response) {
        self.SourceStates = response.result;
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
        transition_type: this.tranType,
        attribute_type: this.attrType,
      };


      let self = this;
      console.log(params);
      if (this.$refs.form.validate()) {
        this.$api.CreateTran(params).then(function(response) {
          self.$message.success("流转添加成功!");
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
