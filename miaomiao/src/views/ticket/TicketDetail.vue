<template>
  <v-col>
    <v-card>
      <v-card-title>
        <v-icon medium left>
          mdi-map
        </v-icon>
        流程图
      </v-card-title>
      <v-card-text>
        <v-stepper v-model="stepp">
          <v-stepper-header>
            <template v-for="(item, index) in steps">
              <v-stepper-step :key="`${index}-step`" :step="index + 1" :complete="stepp > index + 1">{{
                item.name
              }}</v-stepper-step>
              <!-- <v-stepper-step :key="index" :step="item + 1" v-else>{{ item.name }}</v-stepper-step> -->
              <v-divider :key="`${index}-d`" v-if="index !== steps.length - 1"></v-divider>
            </template>
          </v-stepper-header>
        </v-stepper>
      </v-card-text>
    </v-card>
    <v-card class="mt-4">
      <v-card-title>
        <v-icon medium left>
          mdi-clipboard
        </v-icon>
        {{ title }}
      </v-card-title>
      <v-card-text>
        <v-form ref="newForm" :model="newForm">
          <v-container fluid>
            <v-row>
              <v-col cols="3">
                <v-text-field label="标题" placeholder="标题" v-model="ticket.title"></v-text-field>
              </v-col>
              <v-col cols="3">
                <v-text-field disabled label="流水号" placeholder="流水号" v-model="ticket.sn"></v-text-field>
              </v-col>
              <v-col cols="3">
                <v-text-field disabled type="datetime" label="创建时间" v-model="ticket.created"></v-text-field>
              </v-col>
              <v-col cols="3">
                <v-text-field disabled type="datetime" label="更新时间" v-model="ticket.modified"></v-text-field>
              </v-col>
              <template v-for="item in fields">
                <v-col :key="item.field_key" :cols="get_cols(item.field_type)">
                  <v-text-field
                    v-if="[0, 1, 3, 4].indexOf(item.field_type) != -1"
                    :label="item.field_name"
                    v-model="newForm[item.field_key]"
                    :value="newForm[item.field_key]"
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
                  <div v-if="item.field_type === 10">
                    <template v-for="(item, index) in newForm[item.field_key]">
                      <v-chip :key="(index = +'chip')" @click="download(item)"> 附件 - {{ item }}</v-chip>
                    </template>
                  </div>
                </v-col>
              </template>
              <v-divider></v-divider>
              <v-col cols="12" class="mt-3">
                <v-textarea v-model="suggestion" outlined label="审核意见" placeholder=" "></v-textarea>
              </v-col>
            </v-row>
          </v-container>
        </v-form>
      </v-card-text>
      <v-card-actions>
        <div class="mx-auto">
          <v-btn
            v-for="btn in transitions"
            :color="btn.attribute_type === '同意' ? 'success' : btn.attribute_type === '拒绝' ? 'error' : 'warning'"
            :key="btn.id"
            @click="dealTicket(btn.id)"
            >{{ btn.attribute_type }}</v-btn
          >
        </div>
      </v-card-actions>
    </v-card>
    <v-card class="mt-4">
      <v-card-title>
        <v-icon medium left>
          mdi-note
        </v-icon>
        流程操作日志
      </v-card-title>
      <v-card-text>
        <v-data-table
          :headers="headers"
          :items="logs"
          :loading="loading"
          :sort-by.sync="sortBy"
          :sort-desc.sync="sortDesc"
        >
        </v-data-table
      ></v-card-text>
    </v-card>
  </v-col>
</template>

<script>
export default {
  data() {
    return {
      ticketId: this.$route.params.id,
      ticket: "",
      logs: [],
      headers: [
        { text: "节点名称", value: "state" },
        { text: "处理人", value: "participant" },
        { text: "处理类型", value: "participant_type" },
        { text: "处理结果", value: "transition.attribute_type" },
        { text: "操作时间", value: "created" },
        { text: "处理意见", value: "suggestion" }
      ],
      loading: false,
      sortBy: "created",
      rules: {
        required: [(value) => !!value || "这是一个必填项."]
      },
      sortDesc: true,
      transitions: [],
      users: [],
      steps: [],
      newForm: "",
      stepp: 0,
      fields: {},
      suggestion: ""
    };
  },
  computed: {
    title() {
      return this.ticket.title + " " + "详情";
    }
  },
  mounted() {
    this.getUsers();
    this.getTicket();
    this.getTicketLogs();
    this.getTicketTransitions();
    this.getTicketStep();
  },
  methods: {
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
    getTicket() {
      let self = this;
      this.$api.DetailTicket(this.ticketId).then(function(response) {
        self.ticket = response.result;
        self.fields = self.ticket.fields;
        self.newForm = {};
        for (let item of self.fields) {
          self.newForm[item.field_key] = self.ticket.ticket_data[item.field_key];
          if (item.field_type !== 10) {
          }
        }
      });
    },
    getTicketLogs() {
      let self = this;
      self.loading = true;
      this.$api.TicketLogs(this.ticketId).then(function(response) {
        self.logs = response.result;
        self.loading = false;
      });
    },
    getTicketTransitions() {
      let self = this;
      this.$api.TicketTransitions(this.ticketId).then(function(response) {
        self.transitions = response.result;
      });
    },
    getTicketStep() {
      let self = this;
      this.$api.TicketStep(this.ticketId).then(function(response) {
        self.steps = response.result.steps;
        self.stepp = response.result.index + 1;
      });
    },
    dealTicket(transId) {
      this.$message.success("假装审核成功!");
    },
    getUsers() {
      let self = this;
      this.$api.ListUser().then(function(response) {
        self.users = response.result;
      });
    },
    download(item) {
      this.$message.warning("暂不支持下载!");
    }
  }
};
</script>

<style></style>
