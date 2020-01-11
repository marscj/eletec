const path = require("path");
const webpack = require("webpack");
const createThemeColorReplacerPlugin = require("./config/plugin.config");
const CompressionPlugin = require("compression-webpack-plugin");

function resolve(dir) {
  return path.join(__dirname, dir);
}

const isProd = true; //process.env.NODE_ENV === "production";

const assetsCDN = {
  externals: {
    vue: "Vue",
    "vue-router": "VueRouter",
    vuex: "Vuex",
    axios: "axios",
    lodash: "_",
    moment: "moment"
  },
  css: ["unpkg.com/tailwindcss@^1.0/dist/tailwind.min.css"],
  js: [
    "//cdn.jsdelivr.net/npm/vue@2.6.11/dist/vue.min.js",
    "//cdn.jsdelivr.net/npm/vue-router@3.1.3/dist/vue-router.min.js",
    "//cdn.jsdelivr.net/npm/vuex@3.1.2/dist/vuex.min.js",
    "//cdn.jsdelivr.net/npm/axios@0.19.0/dist/axios.min.js",
    "//cdn.jsdelivr.net/npm/moment@2.24.0/moment.min.js",
    "//cdn.jsdelivr.net/npm/lodash@4.17.15/lodash.min.js"
  ]
};

const vueConfig = {
  configureWebpack: {
    plugins: [
      new webpack.IgnorePlugin(/^\.\/locale$/, /moment$/),
      new CompressionPlugin({
        test: /\.js$|\.html$|\.css/,
        threshold: 10240,
        deleteOriginalAssets: false
      })
    ],
    externals: isProd ? assetsCDN.externals : {}
  },

  chainWebpack: config => {
    config.resolve.alias.set("@$", resolve("src"));

    const svgRule = config.module.rule("svg");
    svgRule.uses.clear();
    svgRule
      .oneOf("inline")
      .resourceQuery(/inline/)
      .use("vue-svg-icon-loader")
      .loader("vue-svg-icon-loader")
      .end()
      .end()
      .oneOf("external")
      .use("file-loader")
      .loader("file-loader")
      .options({
        name: "assets/[name].[hash:8].[ext]"
      });

    if (isProd) {
      config.plugin("html").tap(args => {
        args[0].cdn = assetsCDN;
        return args;
      });
    }
  },

  css: {
    loaderOptions: {
      less: {
        modifyVars: {},
        javascriptEnabled: true
      }
    }
  },

  devServer: {
    port: 8000,
    proxy: {
      "/api": {
        target: "http://127.0.0.1:8000",
        ws: false,
        changeOrigin: true
      }
    }
  },

  productionSourceMap: false,
  lintOnSave: undefined,
  transpileDependencies: []
};

if (process.env.VUE_APP_PREVIEW === "true") {
  console.log("VUE_APP_PREVIEW", true);
  vueConfig.configureWebpack.plugins.push(createThemeColorReplacerPlugin());
}

module.exports = vueConfig;
