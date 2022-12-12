const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true
})

const IS_DEV = !process.env.NODE_ENV === 'production'
module.exports = {
    // 是否生成map文件
    productionSourceMap: IS_DEV ? true : true,
    outputDir: "./web"
}