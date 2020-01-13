<template>
  <v-app>
    <ToolBar></ToolBar>
    <Menu></Menu>
    <v-content>
      <v-container fluid>
        <transition name="move" mode="out-in">
          <router-view></router-view>
        </transition>
      </v-container>
    </v-content>
    <Footer app>
    </Footer>
  </v-app>
</template>

<script>
import Menu from "../components/Menu";
import ToolBar from "../components/ToolBar";
import Footer from "../components/Footer";
export default {
  name: "main",
  data() {
    return {};
  },
  components: {
    Menu,
    ToolBar,
    Footer
  }
};
</script>