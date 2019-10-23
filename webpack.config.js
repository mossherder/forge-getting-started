module.exports = {
  mode: 'development',
  entry: './app/static/js/src/index.js',
  output: {
    path: __dirname + '/app/static/js/dist',
    filename: 'bamcore.bundle.js',
  },
  module: {
    rules: [
      {
        test: /\.tsx?$/,
        use: 'ts-loader',
        exclude: /node_modules/,
      },
    ],
  },
  resolve: {
    extensions: ['.ts', '.js'],
  },
};