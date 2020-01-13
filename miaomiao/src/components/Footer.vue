<template>
  <v-footer
    color="primary lighten-1"
    padless
  >
    <v-row
      justify="center"
      no-gutters
    >
      <v-btn
        v-for="link in links"
        :key="link"
        color="black"
        text
        rounded
        class="my-2"
      >
        {{ link }}
      </v-btn>
    <v-btn icon="mdi-github-circle" href="https://github.com/snnucs/ExpenseClaimAutomationSystem">
      <v-icon size="26px">mdi-github-circle</v-icon>
    </v-btn>
    </v-row>
  </v-footer>
</template>
<script>
  export default {
    data: () => ({
      links: [
        '用户帮助|',
        '意见反馈|',
        '联系我们|',
      ],
    }),
  }
</script>