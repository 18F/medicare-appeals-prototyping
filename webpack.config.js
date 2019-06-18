const webpack = require('webpack');

module.exports = {
  entry: {
    dashboard: './src/pages/dashboard.js',
    reports: './src/pages/reports.js'
  },
  mode: 'development',
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        use: ['babel-loader']
      },
      {
        test: /\.css$/i,
        use: ['style-loader', 'css-loader'],
      }
    ]
  },
  resolve: {
    extensions: ['*', '.js', '.jsx']
  },
  output: {
    filename: 'Build.[name].js',
    path: __dirname + '/medicare_appeals/static/dist',
    library: ['Build','[name]'],
    libraryTarget: 'var',
    globalObject: 'this'
  },
  plugins: [
    new webpack.HotModuleReplacementPlugin()
  ]
};
