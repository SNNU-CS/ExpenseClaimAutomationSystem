<template>
  <v-card>
    <v-card-text>
      <v-form v-model="form" ref="form">
        <v-container fluid>
          <v-row>
            <v-col cols="3"
              ><v-text-field :rules="rules.required" v-model="name" label="业务名称"></v-text-field>
            </v-col>
            <v-col cols="3"> <v-text-field v-model="description" label="描述"></v-text-field></v-col>
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
      name: "",
      form: "",
      description: "",
      rules: {
        required: [(value) => !!value || "这是一个必填项."]
      }
    };
  },
  methods: {
    submit() {
      let self = this;
      let params = {
        name: this.name,
        description: this.description
      };
      this.$api.CreateWorkflow(params).then(function(reponse) {
        self.$message.success("新增工作流成功!");
        self.$router.push("/workflow");
      });
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
