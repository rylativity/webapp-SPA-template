module.exports = {
  publicPath: '/home',
  outputDir: './dist/',

  lintOnSave: false,

  chainWebpack: (config) => {
    config.output.filename('bundle.js')

    config.optimization.splitChunks(false)

    config.resolve.alias.set('__STATIC__', 'static')

    config.devServer
      .hotOnly(true)
      .watchOptions({ poll: 1000 })
      .https(false)
      .port(3000)
      .disableHostCheck(true)
      .headers({ 'Access-Control-Allow-Origin': ['*'] })
  },

  // devServer: {
  //   port: 3000
  // },

  transpileDependencies: [
    'vuetify'
  ]
}
