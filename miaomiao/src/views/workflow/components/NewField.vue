<template>
  <v-card>
    <v-card-text>
      <v-form v-model="form" ref="form">
        <v-container fluid>
          <v-row>
            <v-col cols="3"
              ><v-text-field :rules="rules.required" v-model="input.name" label="字段名称"></v-text-field>
            </v-col>
            <v-col cols="3"><v-text-field v-model="input.default" label="默认值"></v-text-field> </v-col>
            <v-col cols="3"> <v-text-field v-model="input.description" label="描述"></v-text-field></v-col>
            <v-col cols="3">
              <v-text-field :rules="rules.required" label="顺序" type="number" v-model="input.order"></v-text-field
            ></v-col>
            <v-col cols="3">
              <v-text-field :rules="rules.required" label="字段标识" v-model="input.key"></v-text-field
            ></v-col>
            <v-col cols="3">
              <v-select
                item-text="text"
                item-value="value"
                :items="typeList"
                v-model="input.type"
                :rules="rules.required"
                label="字段类型"
              ></v-select
            ></v-col>
            <v-col cols="3">
              <v-switch label="必填项" v-model="input.required"></v-switch>
            </v-col>
            <v-col cols="12">
              <v-textarea
                label="radio、checkbox、select的选项"
                placeholder="格式为json如:[{'text':'','value':''}]"
                outlined
                v-model="input.fieldChoice"
              ></v-textarea>
            </v-col>
          </v-row>
        </v-container>
      </v-form>
    </v-card-text>
    <v-card-actions>
      <div class="mx-auto">
        <v-btn color="success" :disabled="loading" @click="submit">提交</v-btn>
        <v-btn color="error" @click="close">取消</v-btn>
        <v-btn color="warning" @click="reset">重置</v-btn>
      </div>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  data() {
    return {
      form: "",
      input: {
        description: "",
        name: "",
        type: "",
        key: "",
        order: 1,
        fieldChoice: ""
      },
      rules: {
        required: [(value) => !!value || "这是一个必填项."]
      },
      workflowId: this.$route.params.id,
      typeList: [
        { text: "字符串", value: 0 },
        { text: "整形", value: 1 },
        { text: "布尔", value: 2 },
        { text: "日期", value: 3 },
        { text: "日期时间", value: 4 },
        { text: "单选框", value: 5 },
        { text: "多选框", value: 6 },
        { text: "下拉列表", value: 7 },
        { text: "多选下拉列表", value: 8 },
        { text: "文本域", value: 9 },
        { text: "附件", value: 10 },
        { text: "用户", value: 11 },
        { text: "多选用户", value: 12 }
      ],
      loading: false
    };
  },
  mounted() {},
  methods: {
    submit() {
      let self = this;
      let params = {
        workflow: this.workflowId,
        description: this.input.description,
        field_key: this.input.key,
        field_name: this.input.name,
        field_choice: this.input.fieldChoice,
        order: this.input.order,
        field_type: this.input.type,
        required: this.input.required
      };
      if (this.$refs.form.validate()) {
        this.loading = true;
        this.$api
          .CreateCustomField(params)
          .then(function(reponse) {
            self.$message.success("新增自定义字段成功!");
            self.loading = false;
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
