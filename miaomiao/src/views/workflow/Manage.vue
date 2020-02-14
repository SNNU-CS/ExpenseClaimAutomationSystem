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
          <v-btn color="success">text</v-btn>
        </v-tab-item>
        <v-tab-item>
          <v-btn color="success">text</v-btn>
        </v-tab-item>
      </v-tabs>
    </v-card-text>
  </v-card>
</template>

<script>
import StateSet from "./components/StateSet";
export default {
  components: {
    "state-set": StateSet
  },
  data() {
    return {};
  },
  methods: {}
};
</script>

<style></style>
