<template>
  <v-app>
    <ToolBar @changeDrawer="drawer = !drawer"></ToolBar>
    <Menu :drawer="drawer"></Menu>
    <v-content>
      <v-container fluid>
        <transition name="move" mode="out-in">
          <router-view></router-view>
        </transition>
      </v-container>
    </v-content>
    <Footer></Footer>
  </v-app>
</template>

<script>
import Menu from "../components/Menu";
import ToolBar from "../components/ToolBar";
import Footer from "../components/Footer";
export default {
  name: "main",
  data() {
    return {
      drawer: false
    };
  },
  components: {
    Menu,
    ToolBar,
    Footer
  }
};
</script>
