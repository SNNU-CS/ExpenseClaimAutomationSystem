<template>
  <v-card>
    <v-card-text>
      <v-tabs grow icons-and-text>
        <v-tabs-slider></v-tabs-slider>
        <v-tab>状态管理<v-icon>mdi-phone</v-icon> </v-tab>
        <v-tab>流转配置<v-icon>mdi-phone</v-icon> </v-tab>
        <v-tab>自定义字段配置<v-icon>mdi-phone</v-icon> </v-tab>
        <v-tab-item>
          <state-set></state-set>
        </v-tab-item>
        <v-tab-item>
          <custom-field></custom-field>
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
export default {
  components: {
    "state-set": StateSet,
    "custom-field": CustomField
  },
  data() {
    return {};
  },
  methods: {}
};
</script>

<style></style>
