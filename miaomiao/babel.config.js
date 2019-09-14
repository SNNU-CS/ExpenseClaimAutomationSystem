module.exports = {
  presets: [
    '@vue/app'
  ],
  devServer: {
    proxy: {
      "/api": {
        target: "http://127.0.0.1:8000"
      }
    }
  }
}
