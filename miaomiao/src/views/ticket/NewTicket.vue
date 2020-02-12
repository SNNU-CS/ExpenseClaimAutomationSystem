<template>
  <v-col>
    <v-card>
      <!-- <v-card-title primary-title>
        title
      </v-card-title> -->
      <v-spacer></v-spacer>
      <v-card-text>
        <v-col cols="6">
          <v-select
            v-model="workflow"
            :items="workflows"
            label="业务名称"
            item-text="name"
            item-value="id"
            outlined
            return-object
            @input="handleWorkflow"
          ></v-select>
        </v-col>
      </v-card-text>
    </v-card>
    <v-card class="mt-4" v-if="workflow">
      <v-card-title primary-title> {{ cardTitle }} </v-card-title>
      <span class="ml-4"> {{ workflow.description }}</span>
      <v-card-text>
        <v-form ref="form">
          <v-text-field :rules="rules.required" label="标题" placeholder="姓氏" v-model="title"></v-text-field></v-form
      ></v-card-text>
      <v-card-actions>
        <div class="mx-auto">
          <v-btn color="success" @click="handleBtn">提交</v-btn>
          <v-btn color="error" @click="close">取消</v-btn>
          <v-btn color="warning" @click="reset">重置</v-btn>
        </div>
      </v-card-actions>
    </v-card>
  </v-col>
</template>

<script>
export default {
  data() {
    return {
      workflow: "",
      workflows: [],
      initState: {},
      title: "",
      rules: {
        required: [(value) => !!value || "这是一个必填项."]
      }
    };
  },
  computed: {
    cardTitle() {
      return "新建 - " + this.workflow.name;
    }
  },
  mounted() {
    this.getWorkflows();
  },
  methods: {
    getWorkflows() {
      let self = this;
      this.$api.ListWorkflow().then(function(response) {
        self.workflows = response.result;
      });
    },
    setTitle() {
      let self = this;
      this.$api.GetSelf().then(function(response) {
        if (response.result.full_name !== "") {
          self.title = response.result.full_name + "的" + self.workflow.name;
        } else {
          self.title = self.workflow.name;
        }
      });
    },
    handleWorkflow() {
      this.getInitState();
      this.setTitle();
    },
    getInitState() {
      let self = this;
      let workflowId = this.workflow.id;
      this.$api
        .GetInitState(workflowId)
        .then(function(response) {
          self.initState = response.result;
        })
        .catch(function(error) {
          self.workflow = "";
        });
    },
    handleBtn() {
      let self = this;
      let params = {
        workflow: self.workflow.id,
        title: self.title,
        ticket_data: {}
      };
      self.$api.CreateTicket(params).then(function(response) {
        self.$message.success("流程提交成功!");
        self.$router.push("/ticket/my");
      });
    },
    reset() {
      this.$refs.form.reset();
    },
    close() {
      this.$router.back(-1);
    }
  }
};
</script>

<style></style>
