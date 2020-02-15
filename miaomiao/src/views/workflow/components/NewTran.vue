<template>
  <v-card>
    <v-card-text>
      <v-form v-model="form" ref="form">
        <v-container fluid>
          <v-row>
            <v-col cols="12" sm="6">
              <v-text-field label="操作名称" v-model="name" :rules="rules.required" placeholder=""></v-text-field>
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

            <v-col v-if="tranType === 1" class="d-flex" cols="12" sm="6">
              <v-text-field label="定时器" :rules="rules.required" v-model="order" type="number"></v-text-field>
            </v-col>

            <v-col class="d-flex" cols="12" sm="6">
              <v-select
                :items="SourceStates"
                item-text="name"
                item-value="id"
                label="源状态"
                :rules="rules.required"
                v-model="SourceState"
              ></v-select>
            </v-col>

            <v-col class="d-flex" cols="12" sm="6">
              <v-select
                :items="SourceStates"
                item-value="id"
                item-text="name"
                label="目的状态"
                v-model="destinationState"
                :rules="rules.required"
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
  name: "NewTran",
  data() {
    return {
      SourceStates: [],
      SourceState: -1,
      name: "",
      tranTypeList: [
        { text: "常规流转", value: 0 },
        { text: "定时器流转", value: 1 }
      ],
      tranType: 0,
      order: 0,
      attrTypeList: [
        { text: "同意", value: 0 },
        { text: "拒绝", value: 1 },
        { text: "其他", value: 2 }
      ],
      attrType: 0,
      workflowId: this.$route.params.id,
      loading: false,
      form: "",
      rules: {
        required: [(value) => !!value || "这是一个必填项."]
      },
      destinationState: ""
    };
  },
  mounted() {
    this.listStates();
  },
  methods: {
    listStates() {
      let self = this;
      this.$api.ListWorkflowState(this.workflowId).then(function(response) {
        self.SourceStates = response.result;
      });
    },
    handleBtn() {
      let params = {
        order: this.order,
        name: this.name,
        workflow: parseInt(this.workflowId),
        transition_type: this.tranType,
        attribute_type: this.attrType,
        source_state: this.SourceState,
        destination_state: parseInt(this.destinationState)
      };

      let self = this;
      console.log(params);
      if (this.$refs.form.validate()) {
        self.loading = true;
        this.$api
          .CreateTran(params)
          .then(function(response) {
            self.loading = false;
            self.$message.success("流转添加成功!");
            self.$router.push("/workflow/manage/" + self.workflowId);
          })
          .catch(function(error) {
            self.loading = false;
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
