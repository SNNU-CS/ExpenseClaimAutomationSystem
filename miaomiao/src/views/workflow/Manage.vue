<template>
  <v-card>
    <v-card-title primary-title>
      <v-btn @click="showChart" text color="info">查看流程图</v-btn>
    </v-card-title>
    <v-card-text>
      <v-tabs grow icons-and-text dense>
        <v-tabs-slider></v-tabs-slider>
        <v-tab>状态管理<v-icon>mdi-phone</v-icon> </v-tab>
        <v-tab>流转配置<v-icon>mdi-phone</v-icon> </v-tab>
        <v-tab>自定义字段配置<v-icon>mdi-phone</v-icon> </v-tab>
        <v-tab-item>
          <state-set></state-set>
        </v-tab-item>
        <v-tab-item>
          <tran-set></tran-set>
        </v-tab-item>
        <v-tab-item>
          <custom-field></custom-field>
        </v-tab-item>
      </v-tabs>
    </v-card-text>
  </v-card>
</template>

<script>
import StateSet from "./components/StateSet";
import CustomField from "./components/CustomField";
import TranSet from "./components/TranSet";

export default {
  components: {
    "state-set": StateSet,
    "custom-field": CustomField,
    "tran-set": TranSet
  },
  data() {
    return {
      workflowId: this.$route.params.id
    };
  },
  methods: {
    showChart() {
      this.$router.push("/workflow/" + this.workflowId + "/flow-chart");
    }
  }
};
</script>

<style></style>
