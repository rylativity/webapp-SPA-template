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
    
    config.module
          .rule('mjs$')
          .test(/\.mjs$/)
          .include
            .add(/node_modules/)
            .end()
          .type('javascript/auto');
  },
  configureWebpack: {
    resolve: {
      extensions: ['*', '.mjs', '.js', '.vue', '.json']
    }
  },

  // devServer: {
  //   port: 3000
  // },

  transpileDependencies: [
    'vuetify'
  ]
}
