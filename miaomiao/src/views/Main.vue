<template>
  <v-app>
    <div class="box">
      <Menu></Menu>
    </div>
    <div class="content-view">
      <transition name="move" mode="out-in">
        <router-view></router-view>
      </transition>
    </div>
  </v-app>
</template>

<script>
import Menu from "../components/Menu";
export default {
  name: "main",
  data() {
    return {};
  },
  components: {
    Menu
  }
};
</script>