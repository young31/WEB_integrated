const path = require('path') // module.exports와 세트
const VueLoaderPlugin = require('vue-loader/lib/plugin')

module.exports = {
  mode: 'development',
  entry: {
    app: path.join(__dirname, 'src', 'main.js') // __dirname은 최상위 위치
  },
  module: {
    rules: [{
        test: /\.vue$/,
        use: 'vue-loader',
      },
      {
        test: /\.css$/,
        use: ['vue-style-loader', 'css-loader']
      }
    ]
  },
  plugins: [
    new VueLoaderPlugin(), // 인식할 수 있게 장착
  ],
  output: {
    filename: 'app.js',
    path: path.join(__dirname, 'dist')
  },
}