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
        <v-form ref="newForm" :model="newForm">
          <v-container fluid>
            <v-row>
              <v-col cols="3">
                <v-text-field :rules="rules.required" label="标题" placeholder="标题" v-model="title"></v-text-field>
              </v-col>
              <template v-for="item in initState.fields">
                <v-col :key="item.field_key" :cols="get_cols(item.field_type)">
                  <v-text-field
                    v-if="[0, 1, 3, 4].indexOf(item.field_type) != -1"
                    :label="item.field_name"
                    v-model="newForm[item.field_key]"
                    :type="get_type(item.field_type)"
                    :placeholder="item.description"
                    :rules="item.required === true ? rules.required : []"
                  ></v-text-field>
                  <v-switch
                    v-if="item.field_type === 2"
                    :label="item.field_name"
                    v-model="newForm[item.field_key]"
                    :rules="item.required === true ? rules.required : []"
                  ></v-switch>
                  <v-radio-group
                    v-if="item.field_type === 5"
                    row
                    :label="item.field_name"
                    v-model="newForm[item.field_key]"
                    outline
                    :rules="item.required === true ? rules.required : []"
                  >
                    <v-radio
                      v-for="choice in item.field_choice"
                      :key="choice"
                      :label="choice.text"
                      :value="choice.value"
                    ></v-radio>
                  </v-radio-group>
                  <template v-if="item.field_type === 6">
                    <v-checkbox
                      v-model="newForm[item.field_key]"
                      v-for="check in item.field_choice"
                      :key="check.value"
                      :label="check.text"
                      :value="check.value"
                      :rules="item.required === true ? rules.required : []"
                    ></v-checkbox>
                  </template>
                  <v-select
                    v-model="newForm[item.field_key]"
                    :items="item.field_choice"
                    item-text="text"
                    item-value="value"
                    v-if="[7, 8].indexOf(item.field_type) != -1"
                    :multiple="item.field_type === 8"
                    :label="item.field_name"
                    :placeholder="item.description"
                    :rules="item.required === true ? rules.required : []"
                  ></v-select>
                  <v-select
                    v-model="newForm[item.field_key]"
                    :items="users"
                    item-text="username"
                    item-value="id"
                    key="id"
                    v-if="[11, 12].indexOf(item.field_type) != -1"
                    :multiple="item.field_type === 12"
                    :label="item.field_name"
                    :placeholder="item.description"
                    :rules="item.required === true ? rules.required : []"
                  ></v-select>
                  <v-textarea
                    outlined
                    v-model="newForm[item.field_key]"
                    v-if="item.field_type === 9"
                    :label="item.field_name"
                    :placeholder="item.description"
                    :rules="item.required === true ? rules.required : []"
                  ></v-textarea>
                  <v-file-input
                    v-if="item.field_type === 10"
                    :placeholder="item.description"
                    v-model="newForm[item.field_key]"
                    chips
                    multiple
                    show-size
                    counter
                    :rules="item.required === true ? rules.required : []"
                    :label="item.field_name"
                  >
                    <template v-slot:append>
                      <v-btn text @click="upload(item)" :loading="loading" :disabled="loading" color="primary"
                        >上传<v-icon right dark>mdi-cloud-upload</v-icon>
                      </v-btn>
                    </template>
                  </v-file-input>
                </v-col>
              </template>
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
  </v-col>
</template>

<script>
export default {
  // self.FIELD_TYPE_STR = 0  # 字符串类型
  // self.FIELD_TYPE_INT = 1  # 整形类型
  // self.FIELD_TYPE_BOOL = 2  # 布尔类型
  // self.FIELD_TYPE_DATE = 3  # 日期类型
  // self.FIELD_TYPE_DATETIME = 4  # 日期时间类型
  // self.FIELD_TYPE_RADIO = 5  # 单选框
  // self.FIELD_TYPE_CHECKBOX = 6  # 多选框
  // self.FIELD_TYPE_SELECT = 7  # 下拉列表
  // self.FIELD_TYPE_MULTI_SELECT = 8  # 多选下拉列表
  // self.FIELD_TYPE_TEXT = 9  # 文本域
  // self.FIELD_TYPE_ATTACHMENT = 10  # 附件，多个附件使用逗号隔开。调用方自己实现上传功能
  // self.FIELD_TYPE_USERNAME = 11  # 用户名
  // self.FIELD_TYPE_MULTI_USERNAME = 12  # 多选用户名,多人情况逗号隔开

  data() {
    return {
      workflow: "",
      workflows: [],
      initState: {},
      title: "",
      rules: {
        required: [(value) => !!value || "这是一个必填项."]
      },
      users: [],
      newForm: {},
      loading: false,
      files: {}
    };
  },
  computed: {
    cardTitle() {
      return "新建 - " + this.workflow.name;
    }
  },
  mounted() {
    this.getWorkflows();
    this.getUsers();
  },
  methods: {
    get_type(field_type) {
      switch (field_type) {
        case 0:
          return "text";
        case 1:
          return "number";
        case 3:
          return "time";
        case 4:
          return "datetime-local";
      }
    },
    upload(item) {
      this.files[item.field_key] = [];
      this.loading = true;
      let self = this;
      for (let file of this.newForm[item.field_key]) {
        let formData = new FormData();
        formData.append("file", file);
        self.$api
          .UploadTicketFile(formData)
          .then(function(response) {
            self.loading = false;
            self.$message.success("上传文件成功!");
            self.files[item.field_key].push(response.result.id);
          })
          .catch(function(e) {
            self.loading = false;
          });
      }
    },
    get_cols(field_type) {
      switch (field_type) {
        case 2:
          return 1;
        case 9:
          return 12;
        case 10:
          return 12;
        default:
          return 3;
      }
    },
    getWorkflows() {
      let self = this;
      this.$api.ListWorkflow().then(function(response) {
        self.workflows = response.result;
      });
    },
    setTitle() {
      let self = this;
      this.$api
        .GetSelf()
        .then(function(response) {
          if (response.result.full_name !== "") {
            self.title = response.result.full_name + "的" + self.workflow.name;
          } else {
            self.title = self.workflow.name;
          }
        })
        .catch(function(e) {
          self.title = self.workflow.name;
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
    handleBtn() {
      let self = this;
      let ticket_data = {};
      let params = {
        workflow: this.workflow.id,
        title: this.title,
        ticket_data: Object.assign({}, this.newForm)
      };
      // 附件,特殊处理,
      for (let i in this.initState.fields) {
        let t = this.initState.fields[i];
        if (t.field_type === 10) {
          params.ticket_data[t.field_key] = self.files[t.field_key];
        }
      }

      if (this.$refs.newForm.validate()) {
        this.$api.CreateTicket(params).then(function(response) {
          self.$message.success("流程提交成功!");
          self.$router.push("/ticket/my");
        });
      }
    },
    getUsers() {
      let self = this;
      this.$api.ListUser().then(function(response) {
        self.users = response.result;
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
